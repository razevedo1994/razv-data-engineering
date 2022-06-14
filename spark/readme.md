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
#
## General functions

- `select()`: returns a new DataFrame with the selected columns.
- `filter()`: filters rows using the given condition.
- `where()`: is just an alias for filter().
- `groupBy()`: groups the DataFrame using the specified columns, so we can run aggregation on them.
- `sort()`: returns a new DataFrame sorted by the specified column(s). By default the second parameter 'ascending' is True.
- `dropDuplicates()`: returns a new DataFrame with unique rows based on all or just a subset of columns.
- `withColumn()`: returns a new DataFrame by adding a column or replacing the existing column that has the same name. The first parameter is the name of the new column, the second is an expression of how to compute it.

### Aggregate functions

Spark SQL provides built-in methods for the most common aggregations such as `count()`, `countDistinct()`, `avg()`, `max()`, `min()`, etc. in the pyspark.sql.functions module. These methods are not the same as the built-in methods in the Python Standard Library, where we can find `min()` for example as well, hence you need to be careful not to use them interchangeably.

In many cases, there are multiple ways to express the same aggregations. For example, if we would like to compute one type of aggregate for one or more columns of the DataFrame we can just simply chain the aggregate method after a `groupBy()`. If we would like to use different functions on different columns, `agg()` comes in handy. For example agg`({"salary": "avg", "age": "max"})` computes the average salary and maximum age.

### User defined functions (UDF)

In Spark SQL we can define our own functions with the udf method from the pyspark.sql.functions module. The default type of the returned variable for UDFs is string. If we would like to return an other type we need to explicitly do so by using the different types from the pyspark.sql.types module.

### Window functions

Window functions are a way of combining the values of ranges of rows in a DataFrame. When defining the window we can choose how to sort and group (with the `partitionBy` method) the rows and how wide of a window we'd like to use (described by `rangeBetween` or `rowsBetween`).

For further information see the [Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) and the [Spark Python API Docs](https://spark.apache.org/docs/latest/api/python/index.html).
#
### Spark SQL

[Spark SQL built-in functions](https://spark.apache.org/docs/latest/api/sql/index.html)
[Spark SQL guide](https://spark.apache.org/docs/latest/sql-getting-started.html)





