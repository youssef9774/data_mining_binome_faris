# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:23:55 2022

@author: FELF3L
"""

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import mysql.connector
from pyspark.sql import Sparksession

db_connection = mysql.connector.connect(user='user', database='BigData', password='vitrygtr', host="192.168.33.9",port=3306)
db_cursor = db_connection.cursor()

sc = SparkContext("local[2]","Network")
ssc = StreamingContext(sc, 1)
socket_stream = ssc.socketTextStream("192.168.33.13", 9999)


def test1(rdd) :

  num = 9999999999
  taken = rdd.take(num)
  for record in taken[:num]:
	  print(record)
	  db_cursor.execute("INSERT INTO DATA(name) VALUES " + "('" + str(record) + "')" + ";") 
	  db_cursor.execute("FLUSH TABLES;")

socket_stream.foreachRDD(test1)

ssc.start()
ssc.awaitTermination() 