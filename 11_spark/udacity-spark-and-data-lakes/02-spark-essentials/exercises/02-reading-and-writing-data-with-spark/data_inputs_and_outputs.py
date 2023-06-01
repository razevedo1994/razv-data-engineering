from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Data input and output").getOrCreate()

path = "./udacity-spark-and-data-lakes/02-spark-essentials/exercises/data/sparkify_log_small.json"
user_log_df = spark.read.json(path=path)

user_log_df.printSchema()
user_log_df.show(1, truncate=False)

output_path = "./udacity-spark-and-data-lakes/02-spark-essentials/exercises/data/sparkify_log_small.csv"
user_log_df.write.mode("overwrite").save(output_path, format="csv", header=True)


user_log_csv_df = spark.read.csv(output_path, header=True)
user_log_csv_df.printSchema()
user_log_csv_df.show(1, truncate=False)

user_log_csv_df.select("userID").show()