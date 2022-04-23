# Spark

## Spark Context


The first component of each Spark Program is the SparkContext. `The SparkContext is the main entrypoint for Spark functionality and connects the cluster with the application.`

If we would like o use lower level abstractions, we will create objects with `SparkContext`. To create a SparkContext, we first need a `SparkConf` object to specify some information about the application such as its name and the master's nodes IP address.
```
from pyspark import SparkContext, SparkConf

configure = SparkConf().setAppName("name").setMaster("IP Address")

sc = SparkContext(conf=configure)
```
If we run Spark in local mode, we can just hte string `local` as master.

To read dataframes, we need to use `SparkContext`, `Spark SQL` equivalent the `SparkSession`. Similarity to the SparkConf, we can specify some parameters to create a SparkSession.
```
from pyspark sql import SparkSession

spark = SparkSession \
.builder \
.appName("app name") \
.config("config option", "confg value") \
.getOrCreate()
```
`GetOrCreate` for example, means that if you already have a SparkSession running, instead of creating a new one, the old one will be returned and its parameters will be modified to the new configurations. 

