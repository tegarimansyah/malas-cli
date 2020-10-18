#!/bin/bash

# Break after first error
set -ex

# Preparation
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
source /etc/lsb-release # Get current version codename 
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $DISTRIB_CODENAME stable"
sudo apt update

# Install and check
sudo apt install -y docker-ce

# Docker without sudo
sudo usermod -aG docker $USER

# Docker Compose
# To Do: automatically install newest release
COMPOSE_URL=$(curl -sSL https://api.github.com/repos/docker/compose/releases/latest \
            | grep browser_download_url \
            | cut -d '"' -f 4 \
            | grep docker-compose-$(uname -s)-$(uname -m) \
            | grep -v .sha256)
sudo curl -sSL $COMPOSE_URL -o /usr/local/bin/docker-compose
# sudo curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-`uname -s`-`uname -m` 
sudo chmod +x /usr/local/bin/docker-compose

# Check Version
echo
echo "======================================="
echo "Installation Done, checking version.."
echo "======================================="
echo
docker -v
docker-compose --version