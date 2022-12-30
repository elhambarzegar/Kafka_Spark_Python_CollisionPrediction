scala_version = '2.12'
spark_version = '3.1.2'
packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}',
    'org.apache.kafka:kafka-clients:3.2.1'
]


kafka_url = 'broker:9092'

kafka_batch_size = 10
kafka_timeout_ms = 200
kafka_record_size = 20
kafka_predication_record_size = 100


input_topics = ['weather', 'collisions']

pg_user = "postgres"
pg_password = "ALItheKING"
pg_db = "postgres_pyspark"
pg_port = "5432"
pg_address = "135.181.40.211"


mongo_address = "mongodb://135.181.40.211:27017"
mongo_db_name = "travel_times"
mongo_collection_name = "travel_times"