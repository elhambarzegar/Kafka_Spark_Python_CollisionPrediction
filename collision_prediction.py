import json
from datetime import datetime

import pandas as pd
from kafka import KafkaConsumer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import os
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from constants import *
from utils import *
from schema_input import *

sc = preprocessing.StandardScaler()
le = preprocessing.LabelEncoder()
gnb = GaussianNB(var_smoothing=0.0001)


def start_learning(items):
    collisions = pd.DataFrame(items)
    collisions['ACCLASS'] = collisions['ACCLASS'].fillna(False)
    collisions.loc[collisions['ACCLASS'] != False, 'ACCLASS'] = True
    collisions = collisions.drop(['VISIBILITY',  'LONGITUDE', 'LATITUDE'], axis=1)
    # create a Gradient for continuous parameters
    collisions.fillna(method="ffill")
    collisions.replace([np.inf, -np.inf], np.nan, inplace=True)
    collisions = collisions.dropna()
    # convert text values to enum
    collisions['Weather'] = le.fit_transform(collisions['Weather'])
    y = collisions['ACCLASS']
    y = y.astype('int')
    X = collisions.drop('ACCLASS', axis=1)
    # standardize the feature scales
    X = sc.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # define the weigh to increase the observation of positive class
    weight_array = y_train
    weight_array = weight_array * 12 + 1
    gnb.fit(X_train, y_train, sample_weight=weight_array)
    y_pred = gnb.predict(X_test)
    cf_matrix = confusion_matrix(y_test, y_pred)
    print('Classification report:\n', classification_report(y_test, y_pred))
    print('Confusion matrix:\n', cf_matrix)
    sns.heatmap(cf_matrix, annot=True)
    plt.show()


import json

items = []


def process_data(rows: list):
    # print(data)
    print('-----------------------------')

    for row in rows:
        data = None
        topic = row.topic
        if topic == 'processed_data':
            data = json.loads(row.value.decode('utf-8'))

        if data is not None:
            items.append(data)
    # if len(items) > 100000:
    start_learning(items)


def start_subscribe():
    consumer = KafkaConsumer('processed_data', bootstrap_servers=[kafka_url],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)
    print(f'Start listening to {consumer.subscription()}')
    while True:
        # poll messages each certain ms
        raw_messages = consumer.poll(timeout_ms=kafka_timeout_ms,
                                     max_records=kafka_predication_record_size,
                                     update_offsets=True)
        # for each message's batch
        for topic_partition, messages in raw_messages.items():
            process_data(messages)


if __name__ == '__main__':
    start_subscribe()
    print('finished')
