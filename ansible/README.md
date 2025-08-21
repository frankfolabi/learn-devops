# Configuring Linux Servers with Ansible
Learning Ansible as an IaC for server configuration. 

To set up the environment,
1. Install Ansible on a central server or workstation.
2. Create a user for Ansible on each machine you want to manage configuration on.
3. Create the same user on your central server or your local machine.
4. Set up the Ansible user on the server so that it can connect to clients via SSH without a password.
5. Configure `sudo` on the client machine so that the Ansible user can execute commands with `sudo` with no password.
