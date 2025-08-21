module "networking" {
  source = "../networking"

}

# Create IAM role for SSM

resource "aws_iam_role" "ssm_role" {
  name = "ec2-ssm-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })

}

resource "aws_iam_role_policy_attachment" "ssm_policy_attachment" {
  role       = aws_iam_role.ssm_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"

}

resource "aws_iam_instance_profile" "ssm_profile" {
  name = "ec2-ssm-instance-profile"
  role = aws_iam_role.ssm_role.name

}


# Create EC2 instances for Nginx, Apache, and Jenkins
resource "aws_instance" "nginx_instance" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = var.instance_type
  iam_instance_profile = aws_iam_instance_profile.ssm_profile.name
  subnet_id            = module.networking.aws_subnet_ids[0]
  security_groups      = [module.networking.aws_security_group_ids[0]]
  user_data            = file("nginx_user_data.sh")
  tags = {
    Name = "NginxInstance"
  }
}


resource "aws_instance" "apache_instance" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = var.instance_type
  iam_instance_profile = aws_iam_instance_profile.ssm_profile.name
  subnet_id            = module.networking.aws_subnet_ids[1]
  security_groups      = [module.networking.aws_security_group_ids[1]]
  user_data            = file("apache_user_data.sh")
  tags = {
    Name = "ApacheInstance"
  }
}

resource "aws_instance" "jenkins_instance" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = "t2.medium"
  iam_instance_profile = aws_iam_instance_profile.ssm_profile.name
  subnet_id            = module.networking.aws_subnet_ids[2]
  security_groups      = [module.networking.aws_security_group_ids[2]]

  user_data = file("jenkins_user_data.sh")
  tags = {
    Name = "JenkinsInstance"
  }
}
