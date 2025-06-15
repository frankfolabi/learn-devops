
# Task 1
You just qualify as a Junior cloud engineer and one of your tasks is to provision an architecture inside a custom VPC connected to an Internet Gateway. All three subnets are public and the entire infrastructure is to be provisioned using Terraform.

Breakdown of the resources are:

Servers | Subnets | Services
--------|---------|----------
server1 | subnet1 | nginx
server2 | subnet2 | apache2 
server3 | subnet3 | jenkins

Configure an s3 bucket to store the terraform statefile (for your terraform workload)

Once the above is completed and running now, create a load balancer on all three servers.