output "aws_subnet_ids" {
  value = [
    aws_subnet.subnet_nginx.id,
    aws_subnet.subnet_apache.id,
    aws_subnet.subnet_jenkins.id
  ]

}

output "aws_vpc_id" {
  value = aws_vpc.custom_vpc.id

}

output "aws_security_group_ids" {
  value = [
    aws_security_group.nginx_sg.id,
    aws_security_group.apache_sg.id,
    aws_security_group.jenkins_sg.id
  ]
}
