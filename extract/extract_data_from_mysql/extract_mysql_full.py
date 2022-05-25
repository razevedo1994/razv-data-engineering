import pymysql
import csv
import boto3
import configparser

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")

conn = pymysql.connect(
    host=hostname, user=username, password=password, db=dbname, port=int(port)
)

if conn is None:
    print("Error connecting to the MySQL databse")
else:
    print("MySQL connection established!")

query = "SELECT * FROM Orders.Orders;"
local_filename = "order_extracted.csv"

cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()

with open(local_filename, "w") as file_:
    csv_w = csv.writer(file_, delimiter=",")
    csv_w.writerows(results)
    file_.close()
    cursor.close()
    conn.close()

access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

s3_file = local_filename

s3.upload_file(local_filename, bucket_name, s3_file)
