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

#Log in to Azure (if not already logged in)
az login
echo "Login Completed"

#Create a resource group
az group create --name $RESOURCE_GROUP --location $LOCATION
echo "Resource group creation completed"

#Create an Azure Container Registry
az acr create --resource-group $RESOURCE_GROUP --name $ACR_NAME --sku Basic --location $LOCATION
echo "ACR creation completed"

#Register for Microsoft Operation Insigths to generate logs
az provider register -n Microsoft.OperationalInsights --wait

#Create a Container Apps environment
az containerapp env create --name $CONTAINERAPPS_ENV --resource-group $RESOURCE_GROUP --location $LOCATION
echo "Container App Environment completed"


