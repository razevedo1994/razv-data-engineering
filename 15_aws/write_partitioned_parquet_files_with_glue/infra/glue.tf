resource "aws_glue_job" "glue_job" {
  name              = "glue_script"
  role_arn          = aws_iam_role.glue_job.arn
  glue_version      = "3.0"
  worker_type       = "Standard"
  number_of_workers = 2
  timeout           = 5

  command {
    script_location = "s3://${local.glue_bucket}/job/write_parquet_job.py"
    python_version  = "3"
  }