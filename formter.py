try:
    sc.stop()
except:
    pass
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

sc = SparkContext()
spark = SparkSession(sparkContext=sc)
