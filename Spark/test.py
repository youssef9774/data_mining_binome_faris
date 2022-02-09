from pyspark import Sparkcontext
from pyspark.streaming import Streami ngContext
import mysql.connector
from pyspark.sql import Sparksession

db_connection = mysql.connector.connect(user='user', database='BigData', password='vitrygtr', host="192.168.33.9",port=3306)
db_cursor = db_connection.cursor()

sc = Sparkcontext("local[2]","Network")
ssc = Streamingcontext(sc, 1)
socket_stream = ssc.socketTextStream("192.168.33.13, 9999)


def takeAndprint(rdd) :

  num = 9999999999
  taken = rdd.take(num)
  for record in taken[:num]:
	  print(record)
	  db_cursor.execute("INSERT INTO DATA(name) VALUES " + "('" + str(record) + "')" + ";") 
	  db_cursor.execute("FLUSH TABLES;")

socket_stream.foreachRDD(takeAndprint)

ssc.start()
ssc.awaitTermination() # Wait for the computation to terminate