provider "aws" {
    region = "us-east-2"
}

resource "aws_s3_bucket" "terraform_state" {
    bucket = "razv-terraform-up-and-running-state"

    # Prevent accidental deletion of this s3 bucket
    # lifecycle {
    #   prevent_destroy = true
    # }

    # force_destroy = true
}

# Enable versioning so you can see the full revision history of your state files
resource "aws_s3_bucket_versioning" "enabled" {
    bucket = aws_s3_bucket.terraform_state.id
    versioning_configuration {
      status = "Enabled"
    }
}

# Enabled server-side encryption by default
resource "aws_s3_bucket_server_side_encryption_configuration" "default" {
    bucket = aws_s3_bucket.terraform_state.id

    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
}

# Explicitly block all public access to the s3 bucket
resource "aws_s3_bucket_public_access_block" "public_access" {
    bucket                  = aws_s3_bucket.terraform_state.id
    block_public_acls       = true
    block_public_policy     = true
    ignore_public_acls      = true
    restrict_public_buckets = true
}

# Create a DynamoDB for locking
resource "aws_dynamodb_table" "terraform_locks" {
    name            = "terraform-up-and-running-locks"
    billing_mode    = "PAY_PER_REQUEST"
    hash_key        = "LockID"

    attribute {
      name = "LockID"
      type = "S"
    }
}

# Define the backend to use
# terraform {
#   backend "s3" {
#     bucket          = "razv-terraform-up-and-running-state"
#     key             = "global/s3/terraform.tfstate"
#     region          = "us-east-2"

#     dynamodb_table  = "terraform-up-and-running-locks"
#     encrypt         = true
#   }
# }