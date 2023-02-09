variable "bucket_names" {
    description = "s3 buckets names"
    type        = list(string)
    default     = [ 
        "temp-zone",
        "landing-zone" ]
}

variable "prefix" {
    description = "objects prefix"
    default     = "razv"
  
}

variable "account_id" {
    default = 333302406330
  
}

locals {
  prefix        = var.prefix
  common_tags   = {
    Project     = "event-driven-data-processing"
  }
}