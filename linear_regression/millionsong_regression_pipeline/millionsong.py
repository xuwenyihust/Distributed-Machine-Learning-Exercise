# Millionsong
# WenyiXu

# Load libraries
from pyspark import SparkContext
from pyspark.sql import SQLContext
import os.path
from pyspark.mllib.regression import LabeledPoint
import numpy as np
from pyspark.sql import functions as sql_functions

# Biolerplate Spark stuff
sc = SparkContext("local", "Millionsong")
sqlContext = SQLContext(sc)

# Load the data
file_name = 
raw_data_df = 

# Preview the dataset
def preview(df):
	num_points = df.count()
	print "Number of rows in the dataframe", num_points
	first_5_rows = df.take(5)
	print "First 5 rows of the dataframe: ", first_5_rows








