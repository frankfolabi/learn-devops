#!/bin/bash
# Update package list and install Apache2
sudo apt update -y
sudo apt install -y apache2

# Enable and start Apache2 service
sudo systemctl enable apache2
sudo systemctl start apache2


echo "<h1>Welcome to Apache on $(hostname)</h1>" | sudo tee /var/www/html/index.html

