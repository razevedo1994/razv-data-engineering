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

# Script generated for node Customer Curated
CustomerCurated_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="workspace",
    table_name="customer_curated",
    transformation_ctx="CustomerCurated_node1",
)

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1687224513098 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://roazesi-lake-house/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerLanding_node1687224513098",
)

# Script generated for node Join
Join_node1687224578436 = Join.apply(
    frame1=CustomerCurated_node1,
    frame2=StepTrainerLanding_node1687224513098,
    keys1=["serialnumber"],
    keys2=["serialNumber"],
    transformation_ctx="Join_node1687224578436",
)

# Script generated for node Drop Fields
DropFields_node1687224735786 = DropFields.apply(
    frame=Join_node1687224578436,
    paths=[
        "customername",
        "email",
        "phone",
        "birthday",
        "serialnumber",
        "registrationdate",
        "lastupdatedate",
        "sharewithpublicasofdate",
        "sharewithresearchasofdate",
        "sharewithfriendsasofdate",
    ],
    transformation_ctx="DropFields_node1687224735786",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1687224735786,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://roazesi-lake-house/step_trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="StepTrainerTrusted_node3",
)

job.commit()
