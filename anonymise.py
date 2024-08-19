from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col

spark = SparkSession.builder.appName("DataAnonymization").getOrCreate()

df = spark.read.csv("dataset.csv", header=True)

anonymized_df = df.withColumn("first_name", sha2(col("first_name"), 256)) \
                  .withColumn("last_name", sha2(col("last_name"), 256)) \
                  .withColumn("address", sha2(col("address"), 256))

anonymized_df.write.csv("anonymized_output.csv", mode="overwrite", header=True)

spark.stop()
