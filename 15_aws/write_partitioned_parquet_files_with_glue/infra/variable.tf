variable "environment" {
  default = "dev"
}

variable "prefix" {
  description = "objects prefix"
  default     = "razv"
}

locals {
  glue_bucket = "${var.prefix}-scripts-${var.environment}"
  prefix      = var.prefix
  common_tags = {
    Environment = "dev"
    Project     = "write-with-glue"
  }
}