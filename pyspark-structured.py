import json
from json import dumps

# import findspark

import pandas as pd
import geopandas as gpd
from pyspark.sql import SparkSession
import numpy as np
# findspark.init()
from constants import *
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=[kafka_url], value_serializer=lambda x: dumps(x).encode('utf-8'))

# spark = SparkSession.builder \
#     .master("local[*]") \
#     .appName("kafka-app") \
#     .config("spark.jars.packages", ",".join(packages)) \
#     .config("spark.sql.debug.maxToStringFields", "100") \
#     .getOrCreate()


travel_time = pd.read_csv('./datasets/travel-time-2014.csv')
shapefile = gpd.read_file("./datasets/bluetooth-routes/bluetooth_routes_wgs84.shp")

merged = shapefile.merge(travel_time, on='resultId')
merged.dropna()

density = (merged['count'] * merged['timeInSeconds']) / (merged['length_m'])
merged['density'] = density
merged['speed'] = merged['length_m'] / merged['timeInSeconds']

merged = merged[(merged['updated'] > '2014-10-01T00:00:00-05')]
merged.index = pd.to_datetime(merged['updated'].map(lambda x: x[0:-3]))

merged.replace([np.inf, -np.inf], np.nan, inplace=True)


for id, geometry in enumerate(shapefile.geometry):
    row = shapefile.iloc[id].resultId
    temp = merged[(merged['resultId'] == row)]

    # aggregate temp every hour
    aggregated = temp.groupby(by=[
        temp.index.month,
        temp.index.day,
        temp.index.hour
    ]).aggregate({'density': 'mean', 'speed': 'mean', 'updated': 'min'})
    aggregated.index = pd.to_datetime(aggregated['updated'].map(lambda x: x[0:-3]))
    aggregated.replace([np.inf, -np.inf], np.nan, inplace=True)
    data = aggregated.filter(['updated', 'density', 'speed', 'resultId'])
    for idx, value in data.iterrows():
        item = {'updated': value["updated"],
                'density': value["density"],
                'speed': value["speed"],
                'resultId': row}
        producer.send('travel_times_input_2', value=item)
