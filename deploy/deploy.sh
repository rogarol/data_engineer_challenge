#!/bin/bash
# Exit on error
set -e

# Variables – update these values for your environment
RESOURCE_GROUP="DECcontainer"
LOCATION="eastus"
ACR_NAME="deccontainerregistry"          #must be globally unique and 5-50 lowercase letters and numbers
IMAGE_NAME="decimage"                 #name for your container image
CONTAINERAPPS_ENV="deccontainerenv"
CONTAINER_APP_NAME="deccontainerappv2"
API_PORT=80                          #the port your Python API listens on

#Path to the .env file in another folder (where the env variables are stored)
ENV_FILE="../.venv/.env"

#Load environment variables from the .env file and format them for the CLI command.
#This will ignore lines that are comments (starting with '#') or blank.
if [ -f "$ENV_FILE" ]; then
  ENV_VARS=$(grep -v '^#' "$ENV_FILE" | grep -v '^\s*$' | xargs)
  echo "Loaded environment variables"
else
  echo ".env file not found at $ENV_FILE"
  exit 1
fi

#Get ACR User and Password from our env variables
ACR_USER=$(grep '^AZURE_ACR_USER=' "$ENV_FILE" | cut -d '=' -f2-)
ACR_PASS=$(grep '^AZURE_ACR_PASSWORD=' "$ENV_FILE" | cut -d '=' -f2-)

#Log in to Azure (if not already logged in)
az login
echo "Login Completed"

#Go to the project folder to find the Dockerfile
cd ..

#Build and push the container image to ACR
#Make sure you have a Dockerfile in the current directory!
az acr build --registry $ACR_NAME --image $IMAGE_NAME:latest .
echo "Build creation completed"

#Deploy the container app
az containerapp create \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --environment $CONTAINERAPPS_ENV \
  --image ${ACR_NAME}.azurecr.io/${IMAGE_NAME}:latest \
  --target-port $API_PORT \
  --ingress external \
  --cpu 2 \
  --memory 4.0Gi \
  --min-replicas 1 \
  --max-replicas 3 \
  --registry-server ${ACR_NAME}.azurecr.io \
  --registry-username $ACR_USER \
  --registry-password $ACR_PASS \
  --env-vars $ENV_VARS #Here we pass the env variables containing connection credentials and other sensitive information
echo "App deployment completed"

#Output the URL of the deployed container app
echo "Container App is deployed at:"
az containerapp show --name $CONTAINER_APP_NAME --resource-group $RESOURCE_GROUP --query properties.configuration.ingress.fqdn -o tsv

#--set properties.template.containers[0].startupProbe.httpGet.path="/health" \