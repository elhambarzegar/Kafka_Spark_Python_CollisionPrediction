import io
from fastavro.io.binary_decoder import BinaryDecoder
from kafka import KafkaConsumer
from constants import *
from datetime import datetime
import psycopg2
from schema_input import *
from utils import *

connection = psycopg2.connect(user=pg_user,
                              password=pg_password,
                              host=pg_address,
                              port=pg_port,
                              database=pg_db)
cursor = connection.cursor()


def insert_to_database(topic, keys, values):
    columns = ",".join(["\"" + key + "\"" for key in keys])
    vals = ",".join(["%s" for _ in keys])
    insert_query = f"INSERT INTO {topic} ({columns}) VALUES ({vals})"
    cursor.execute(insert_query, values)
    connection.commit()


def process_data(rows: list):
    # print(data)
    print('-----------------------------')
    for row in rows:
        data = None
        topic = row.topic
        created = datetime.utcnow()
        timestamp = row.timestamp
        if topic == 'weather':
            data = decode_method_2(row.value, weather_reader)

        elif topic == 'collisions':
            data = decode_method_2(row.value, collision_reader)

        if data is not None:
            keys = list(data.keys())
            values = list(data.values())
            # keys.append("create_at")
            # values.append(str(datetime.utcnow()))
            # keys.append("status")
            # values.append("pre_process")
            insert_to_database(topic, keys, values)
            # insert_to_database(topic, data)
            print(topic, timestamp, data)


def start_subscribe():
    consumer = KafkaConsumer(bootstrap_servers=[kafka_url],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)

    consumer.subscribe(input_topics)
    print(f'Start listening to {consumer.subscription()}')
    while True:
        # poll messages each certain ms
        raw_messages = consumer.poll(timeout_ms=kafka_timeout_ms,
                                     max_records=kafka_record_size,
                                     update_offsets=True)
        # for each message's batch
        for topic_partition, messages in raw_messages.items():
            process_data(messages)


if __name__ == '__main__':
    start_subscribe()
    print('finished')
