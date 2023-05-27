
if __name__ == "__main__":
    
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("maps_code_example").getOrCreate()

    log_of_songs = [
        "Despacito",
        "Nice for what",
        "No tears left to cry",
        "Despacito",
        "Havana",
        "In my feelings",
        "Nice for what",
        "despacito",
        "All the stars"
    ]

    # parallelize the log_of_songs to use with Spark
    distributed_log_of_songs = spark.sparkContext.parallelize(log_of_songs)

    # show the original input data is preserved
    distributed_log_of_songs.foreach(print)

    # create a python function to convert strings to lowercase
    def convert_song_to_lowercase(song):
        return song.lower()
    
    # use the map function to transform the list of songs with the python function that converts strings to lowercase
    lower_case_songs=distributed_log_of_songs.map(convert_song_to_lowercase)
    lower_case_songs.foreach(print)


    # Show the original input data is still mixed case
    distributed_log_of_songs.foreach(print)

    # Use lambda functions instead of named functions to do the same map operation
    distributed_log_of_songs.map(lambda song: song.lower()).foreach(print)
