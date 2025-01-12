#!/bin/bash

# Copy Secret Credentials to Mounted Volume
# echo "Attempting to copy secret credentials..."
# cp secrets.py assets/
# echo "Successfully copied secret credentials!"

# Run Latest Docker Images
echo "Attempting to Deploy MongoDB Docker images..."
docker compose down
docker compose up -d
echo "Successfully Deployed MongoDB Docker images!"