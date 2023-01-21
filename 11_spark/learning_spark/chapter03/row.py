"""A row in Spark is a generic Row object, containing one or more columns.
Each column may be of the same data type or they can have different types.
Because Row is an object is Spark and an ordered collection of fields, you can
instantiate a Row in each os Spark's supported languages and access its fields
by an index starting at 0."""

from pyspark import Row
from pyspark.sql.types import *
from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession.builder.appName("Authors").getOrCreate()

    schema = StructType(
        [
            StructField("Author", StringType(), False),
            StructField("State", StringType(), False),
        ]
    )

    rows = [Row("Rodrigo Azevedo", "RJ"), Row("Reynold Xin", "CA")]
    authors_df = spark.createDataFrame(rows, schema)
    authors_df.show()
