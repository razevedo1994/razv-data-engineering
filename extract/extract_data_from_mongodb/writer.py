from botocore.exceptions import ClientError
import csv
import boto3


def write_file_local(events, filename):
    export_file_events = filename

    with open(export_file_events, "w") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(events)


def write_file_on_s3(access_key, secret_key, export_file_events, bucket_name):

    s3 = boto3.client(
        "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key
    )

    s3_file = export_file_events

    try:
        s3.upload_file(export_file_events, bucket_name, s3_file)
    except ClientError as e:
        print(str(e))
        return False
    return True
