# Provider Setupt
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.99.1"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "4.0.6"
    }

  }
}

provider "aws" {
  region = var.region
  }
