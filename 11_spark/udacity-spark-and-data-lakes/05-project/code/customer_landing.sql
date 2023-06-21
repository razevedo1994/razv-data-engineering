CREATE EXTERNAL TABLE IF NOT EXISTS `workspace`.`customer_landing` (
  `serialnumber` string,
  `sharewithpublicasofdate` bigint,
  `birthday` string,
  `registrationdate` bigint,
  `sharewithresearchasofdate` bigint,
  `customername` string,
  `email` string,
  `lastupdatedate` bigint,
  `phone` string,
  `sharewithfriendsasofdate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://roazesi-lake-house/customer/landing/'
TBLPROPERTIES ('classification' = 'json');