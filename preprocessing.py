from json import dumps

import pandas as pd
import geopandas as gpd
from kafka import KafkaProducer
from matplotlib import pyplot as plt
import numpy as np
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
from constants import *


def read_shape():
    return gpd.read_file("./datasets/bluetooth-routes/bluetooth_routes_wgs84.shp")


def init_mongo_context():
    spark_context = SparkSession \
        .builder \
        .appName("mongoDbReadData") \
        .master('local[*]') \
        .config("spark.mongodb.input.uri", f"{mongo_address}/{mongo_db_name}.{mongo_collection_name}") \
        .config("spark.mongodb.output.uri", f"{mongo_address}/{mongo_db_name}.{mongo_collection_name}") \
        .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
        .config("spark.sql.debug.maxToStringFields", "200") \
        .config("spark.jars", "postgresql-42.2.5.jar") \
        .getOrCreate()
    # spark_context1 = SparkSession.builder.getOrCreate().newSession()
    # spark_context2 = SparkSession.builder.getOrCreate().newSession()

    content = spark_context.read.format("mongo").load().toPandas()
    spark_context.stop()
    return content


def init_postgres_table(tableName):
    spark_context2 = SparkSession.builder.getOrCreate()
    data = spark_context2.read \
        .format("jdbc") \
        .option("url", f"jdbc:postgresql://{pg_address}:{pg_port}/{pg_db}") \
        .option("dbtable", tableName) \
        .option("user", pg_user) \
        .option("password", pg_password) \
        .option("driver", "org.postgresql.Driver") \
        .load()
    return data


def read_mongo_data(spark_context):
    return spark_context


def refine_weather(df):
    df['Date'] = pd.to_datetime(df['Date'] + " " + df['Time'])
    df.loc[df["Wind"] == "No", "Wind"] = 0
    return df


def refine_collisions(df):
    original_df = df.copy()
    df['YEAR'] = df['YEAR'].astype(int)
    df = df[df['YEAR'] == 2014]

    df['LONGITUDE'] = df['LONGITUDE'].astype(np.double)
    df['LOCCOORD'] = df['LOCCOORD'].astype(np.double)
    df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['LONGITUDE'], df['LOCCOORD']))
    return df, original_df


def refine_density(df):
    df = df[(df['updated'] > '2014-10-01T00:00:00-05')]
    df.index = pd.to_datetime(df['updated'].map(lambda x: x[0:-3]))

    return df


def init_kafka_producer():
    return KafkaProducer(bootstrap_servers=[kafka_url], value_serializer=lambda x: dumps(x).encode('utf-8'))


def publish_to_kafka(producer, row, data):
    producer.send('processed_data_2', data)


if __name__ == '__main__':
    shape_file = read_shape()
    df_travel_times = init_mongo_context()
    df_travel_times = refine_density(df_travel_times)


    df_weather = init_postgres_table("weather").toPandas()
    df_weather = refine_weather(df_weather)

    df_collisions = init_postgres_table("collisions").toPandas()

    df_collisions, df_collisions_original = refine_collisions(df_collisions)


    kafka_producer = init_kafka_producer()


    df_travel_times.index = pd.to_datetime(df_travel_times['updated'].map(lambda x: x[0:-3]))

    for id, geometry in enumerate(shape_file.geometry):
        row = shape_file.iloc[id].resultId
        temp = df_travel_times[(df_travel_times['resultId'] == row)]

        ## aggregate temp every hour
        aggregated = temp.groupby(by=[
            temp.index.month,
            temp.index.day,
            temp.index.hour
        ]).aggregate({'density': 'mean', 'speed': 'mean', 'updated': 'min'})
        # aggregated.index = pd.to_datetime(aggregated['updated'].map(lambda x: x[0:-3]))

        ##############################

        route = geometry.buffer(0.002)

        imp_collisions = df_collisions.within(route)

        coll_loc = df_collisions_original[imp_collisions == True]
        coll_loc.index = pd.to_datetime(coll_loc['DATE'].astype(str) + " " + coll_loc['HOUR'].astype(str) + ":00")
        coll_loc = coll_loc[(coll_loc.index > '2014-10-01 00:00:00')]
        # print(coll_loc['ObjectId'].count())
        finalData = aggregated.join(df_weather, how='outer') .join(coll_loc, how='outer', rsuffix='_right')

        data = finalData.filter(
            ['resultId', 'density', 'speed', 'Temp', 'Weather', 'Wind', 'Visibility', 'VISIBILITY', 'LIGHT', 'ACCLASS',
             'LONGITUDE', 'LATITUDE'])

        for key, value in data.iterrows():
            item_json = {
                'resultId': row,
                'density': value['density'],
                'speed': value['speed'],
                'Temp': value['Temp'],
                'Weather': value['Weather'],
                'Wind': value['Wind'],
                'Visibility': value['Visibility'],
                'VISIBILITY': value['VISIBILITY'],
                'ACCLASS': value['ACCLASS'],
                'LONGITUDE': value['LONGITUDE'],
                'LATITUDE': value['LATITUDE'],
            }
            publish_to_kafka(kafka_producer, row, item_json)
