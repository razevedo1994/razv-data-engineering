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

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="workspace",
    table_name="accelerometer_landing",
    transformation_ctx="AccelerometerLanding_node1",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1686394484728 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://roazesi-lake-house/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="CustomerTrusted_node1686394484728",
)

# Script generated for node Customer Privacy Filter
CustomerPrivacyFilter_node1686394595644 = Join.apply(
    frame1=AccelerometerLanding_node1,
    frame2=CustomerTrusted_node1686394484728,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="CustomerPrivacyFilter_node1686394595644",
)

# Script generated for node Drop Fields
DropFields_node1686394994593 = DropFields.apply(
    frame=CustomerPrivacyFilter_node1686394595644,
    paths=[
        "serialNumber",
        "shareWithPublicAsOfDate",
        "birthDay",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithFriendsAsOfDate",
    ],
    transformation_ctx="DropFields_node1686394994593",
)

# Script generated for node Amazon S3
AmazonS3_node1687234306305 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1686394994593,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://roazesi-lake-house/accelerometer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1687234306305",
)

job.commit()
