#!/bin/bash
# Update package list and install Nginx
sudo apt update -y
sudo apt install -y nginx

# Enable Nginx to start on boot and start it now
sudo systemctl enable nginx
sudo systemctl start nginx

# Replace default index.html
echo "<h1>Welcome to Nginx on $(hostname)</h1>" | sudo tee /var/www/html/index.html

