# This provider block specifies that we are using the AWS provider, s3 backend for state management,
# and sets the region to us-west-2.
# This file is used to configure the AWS provider for Terraform.
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "custom-bucket-for-terraform-state"
    key    = "terraform/state"
    region = "us-west-2"
  }
}


provider "aws" {
  region = "us-west-2"
}

