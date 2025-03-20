#!/bin/bash
# Exit on error
set -e

# Variables – update these values for your environment
RESOURCE_GROUP="DECcontainer"
LOCATION="eastus"
ACR_NAME="deccontainerregistry"          #must be globally unique and 5-50 lowercase letters and numbers
IMAGE_NAME="decimage"                 #name for your container image
CONTAINERAPPS_ENV="deccontainerenv"
CONTAINER_APP_NAME="deccontainerapp"
API_PORT=8000                          #the port your Python API listens on

#Path to the .env file in another folder (where the env variables are stored)
ENV_FILE="../.venv/.env"

#Load environment variables from the .env file and format them for the CLI command.
#This will ignore lines that are comments (starting with '#') or blank.
if [ -f "$ENV_FILE" ]; then
  ENV_VARS=$(grep -v '^#' "$ENV_FILE" | grep -v '^\s*$' | xargs)
  echo "Loaded environment variables: $ENV_VARS"
else
  echo ".env file not found at $ENV_FILE"
  exit 1
fi

#Log in to Azure (if not already logged in)
az login
echo "Login Completed"

#Create a resource group
az group create --name $RESOURCE_GROUP --location $LOCATION
echo "Resource group creation completed"

#Create an Azure Container Registry
az acr create --resource-group $RESOURCE_GROUP --name $ACR_NAME --sku Basic --location $LOCATION
echo "ACR creation completed"

#Build and push the container image to ACR
#Make sure you have a Dockerfile in the current directory!
az acr build --registry $ACR_NAME --image $IMAGE_NAME:latest .
echo "Build creation completed"

#Create a Container Apps environment
az containerapp env create --name $CONTAINERAPPS_ENV --resource-group $RESOURCE_GROUP --location $LOCATION
echo "Container App Environment completed"

#Deploy the container app
az containerapp create \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --environment $CONTAINERAPPS_ENV \
  --image ${ACR_NAME}.azurecr.io/${IMAGE_NAME}:latest \
  --target-port $API_PORT \
  --ingress external \
  --cpu 0.5 \
  --memory 1.0Gi \
  --min-replicas 1 \
  --max-replicas 3 \
  --registry-server ${ACR_NAME}.azurecr.io \
  --env-vars $ENV_VARS #Here we pass the env variables containing connection credentials and other sensitive information
echo "App deployment completed"

#Output the URL of the deployed container app
echo "Container App is deployed at:"
az containerapp show --name $CONTAINER_APP_NAME --resource-group $RESOURCE_GROUP --query properties.configuration.ingress.fqdn -o tsv
