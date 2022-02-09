# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:48:07 2022

@author: FELF3L
"""

#Envoie un fichier json ligne ligne par ligne dans le bus Kafka
import json
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='192.168.33.13:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

with open('country_vaccinations_by_manufacturer', 'r') as f:
    listusers= f.readlines()


for i in listusers:
    user=i.strip()
    print(user)
    producer.send('Projetbd', user)
    time.sleep(5)