# This output the IDs and public IPs of the created instances
output "nginx_instance_id" {
  value       = aws_instance.nginx_instance.id
  description = "ID of the Nginx instance"
}

output "apache_instance_id" {
  value       = aws_instance.apache_instance.id
  description = "ID of the Apache instance"
}

output "jenkins_instance_id" {
  value       = aws_instance.jenkins_instance.id
  description = "ID of the Jenkins instance"
}

output "apache_instance_public_ip" {
  value       = aws_instance.apache_instance.public_ip
  description = "Public IP of the Apache instance"
}

output "nginx_instance_public_ip" {
  value       = aws_instance.nginx_instance.public_ip
  description = "Public IP of the Nginx instance"
}

output "jenkins_instance_public_ip" {
  value       = aws_instance.jenkins_instance.public_ip
  description = "Public IP of the Jenkins instance"
}

