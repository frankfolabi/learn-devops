variable "instance_type" {
  description = "Type of the EC2 instance"
  type        = string
  default     = "t2.micro"

}

data "aws_ami" "ubuntu" {
  owners = ["099720109477"]
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}