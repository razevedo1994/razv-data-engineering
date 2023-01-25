resource "aws_s3_object" "etl" {
  bucket = "razv-scripts-dev"
  key    = "job/write_parquet_job.py"
  source = "./glue_job/write_parquet_job.py"
  etag   = filemd5("./glue_job/write_parquet_job.py")
}