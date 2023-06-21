import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="workspace",
    table_name="step_trainer_trusted",
    transformation_ctx="StepTrainerTrusted_node1",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1687311329489 = glueContext.create_dynamic_frame.from_catalog(
    database="workspace",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1687311329489",
)

# Script generated for node Join
Join_node1687311372357 = Join.apply(
    frame1=AccelerometerTrusted_node1687311329489,
    frame2=StepTrainerTrusted_node1,
    keys1=["timestamp"],
    keys2=["sensorreadingtime"],
    transformation_ctx="Join_node1687311372357",
)

# Script generated for node Drop Fields
DropFields_node1687311401787 = DropFields.apply(
    frame=Join_node1687311372357,
    paths=["user"],
    transformation_ctx="DropFields_node1687311401787",
)

# Script generated for node Amazon S3
AmazonS3_node1687311498542 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1687311401787,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://roazesi-lake-house/machine_learning/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1687311498542",
)

job.commit()
