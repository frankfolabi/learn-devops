# This is to create the backend configuration for Terraform, 
# which specifies that the state will be stored in an S3 bucket.

resource "aws_s3_bucket" "state_bucket" {
  bucket = "custom-bucket-for-terraform-state"

  tags = {
    Name        = "Terraform"
    Environment = "Dev"
  }

}

resource "aws_s3_bucket_versioning" "state_bucket_versioning" {
  bucket = aws_s3_bucket.state_bucket.id

  versioning_configuration {
    status = "Enabled"
  }

}