#!/bin/bash

# Break after first error
set -ex

# Preparation
sudo apt update

# Instalation
sudo apt install nginx ufw -y

# Firewall Set up
sudo ufw allow 'Nginx HTTP'
# Nginx Full: This profile opens both port 80 (normal, unencrypted web traffic) and port 443 (TLS/SSL encrypted traffic)
# Nginx HTTP: This profile opens only port 80 (normal, unencrypted web traffic)
# Nginx HTTPS: This profile opens only port 443 (TLS/SSL encrypted traffic)
sudo ufw allow 'OpenSSH' # Just in case ssh not allowed
echo "y" | sudo ufw enable

# Print Result
echo "All available App"
sudo ufw app list
echo "All enabled App"
sudo ufw status