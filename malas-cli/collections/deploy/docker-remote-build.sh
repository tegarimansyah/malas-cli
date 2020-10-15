#!/bin/bash

# Break after first error
set -ex

# User Input
SSH_KEY_FILE=$1
USERNAME_IPADDRESS=$2
TAG=$3
DOCKERFILE=$4
CONTEXT=$5

# Run
ssh-add $SSH_KEY_FILE
export DOCKER_HOST=$USERNAME_IPADDRESS
docker build -t $TAG -f $DOCKERFILE $CONTEXT

unset DOCKER_HOST