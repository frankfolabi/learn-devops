
# Automate Your Environment Setup 

Using Terraform to provision the Ubuntu VM

#### ☁️ Terraform Files

The `.tf` files are the configuration files in HCL. 
> Note: The Terraform HCP was used for the backend to store the statefile. 
You may need to run `terraform login` to retrieve your token to authenticate to HCP
---

## 📦 Setup Instructions

### 0. Create the Infrastructure

- Clone this repository. 
```
git clone https://github.com/frankfolabi/learn-devops.git
cd jenkins/setup
```

- Run the following commands to initialize Terraform
```terraform
terraform init
terraform plan
terraform apply
```
> **Note:** Terrafom output displays the Public IP and marks the private key as a sensitive data. 

- Obtain the private key and connect to the Ubuntu instance:
```
terraform output private_key_pem > jenkins.pem
chmod 0600 jenkins.pem
ssh -i jenkins.pem ubuntu@<Public IP>
```
> **Note:** The `jenkins.pem` is a sensitive data. Never add it to your version control system.

### 1. Upgrade System and Install Docker

You may use scp to first transfer the [docker-setup.sh](./docker-setup.sh) script to the VM and execute or copy and run the script in the SSH terminal session.

***⚠️ The script logs you out for the Docker group to apply. Start a new SSH session to continue.***

### 2. Install Jenkins
After the Docker is installed, run the official Jenkins images

```bash
docker run -p 8080:8080 -p 50000:50000 -d \
-v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
- Port 8080 - For browser access
- Port 50000 - Jenkins master and worker nodes cluster 
- jenkins_home - Mount Volumes for persisting data on the host (Named volume)

### 3. System Check 
The image would be pulled and container running. Check with

```
docker ps
```

### 4. Access Jenkins
You can now access Jenkin on a web browser.
```
<public_ip>:8080
```
Get the admin password.

Option 1. From the host
```
docker volume inspect jenkins_home
```
`cd` to the mountpoint and obtain the secret

Option 2. From the container

```
docker exec -it <container-name> bash
```
`cd` to the secret's path and obtain the initial password to login and finish the Jenkins setup on the UI

### 5.  Stopping the VM

In order to save cost, you can start and stop the instance when not in use. You can configure the [start-stop-instance.sh](./start-stop-instance.sh) to reflect the region you are using. 


> Note: Always remember to stop your instances when not in use. Cloud cost can quickly accumulate.

```
bash start-stop-instance.sh
```

### 6.  Clean Up

After the project clean up your environment 

```
terraform destroy
``` 

Enjoy the Jenkins learning.