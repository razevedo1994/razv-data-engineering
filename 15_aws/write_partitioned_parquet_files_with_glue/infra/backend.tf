terraform {
  backend "s3" {
    bucket = "glue-job-terraform"
    key = "terraform-glue-job.tfstate"
    region = "us-east-1"
  }
}