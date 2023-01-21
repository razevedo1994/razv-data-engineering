import pymysql
import csv
import boto3
import configparser
import psycopg2

# get db Redshift connection
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
dbname = parser.get("aws_creds", "database")
user = parser.get("aws_creds", "username")
password = parser.get("aws_creds", "username")
host = parser.get("aws_creds", "host")
port = parser.get("aws_creds", "port")

# connect to the redshift cluster
redshift_conn = psycopg2.connect(
    "dbname="
    + dbname
    + " user="
    + user
    + " password="
    + password
    + " host="
    + host
    + " port="
    + port
)

redshift_sql = """SELECT COALESCE(MAX(LastUpdated), '1900-01-01') FROM Orders;"""

redshift_cursor = redshift_conn.cursor()
redshift_cursor.execute(redshift_sql)
result = redshift_cursor.fetchone()

last_updated_warehouse = result[0]

redshift_cursor.close()
redshift_conn.commit()

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

mysql_query = """SELECT * FROM Orders WHERE LastUpdated > %s;"""

local_filename = "order_extracted.csv"

mysql_cursor = conn.cursor()
mysql_cursor.execute(mysql_query, (last_updated_warehouse,))
results = mysql_cursor.fetchall()

with open(local_filename, "w") as file_:
    csv_w = csv.writer(file_, delimiter=",")
    csv_w.writerows(results)

mysql_cursor.close()
conn.close()

access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

s3_file = local_filename

s3.upload_file(local_filename, bucket_name, s3_file)
