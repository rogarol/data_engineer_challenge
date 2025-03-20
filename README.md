# Data Engineer Challenge

A REST API built with **FastAPI**, running on **Uvicorn**, containerized via **Docker**, and powered by a **MySQL** database. All running in the **Azure** cloud services.

The API is already available on Azure in the following link:

https://deccontainerappv2.ambitioushill-fad7020d.eastus.azurecontainerapps.io/docs

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [API Guide](#api-guide)
- [Prerequisites](#prerequisites)
- [Libraries](#Libraries)
- [Deployment](#running-the-application)

## Features

- **DB Migration:** Load historical data of 3 tables (departments, jobs, employees).
    - Receive historical data from CSV files
    - Upload these files to the new DB
    - Be able to insert batch transactions (1 up to 1000 rows) with one request

- **Business Metrics:** Generate two reports for the following purposes (an endpoint for each one):
    - Number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.
    - List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).

## Architecture

![Arquitecture Diagram](/diagrams/DEC_ArquitectureDiagram.png)

## Tech Stack

- **FastAPI:** For building the REST API.
- **Uvicorn:** ASGI server for running the application.
- **Docker:** For containerization and deployment.
- **MySQL Database:** RDBMS open source database.
- **Azure:** For cloud services.

## API Guide

![Endpoints Guide](/diagrams/DEC_EndpointsGuide.png)

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9
- Git
- MySQL Workbench

### Libraries

We will use the following libraries in the project:
- fastapi
- uvicorn
- sqlalchemy
- pandas
- azure-storage-blob
- mysql-connector-python

### Deployment

For Local deployment you can run the following command on docker:
    
    ```bash
    docker build -t [image_name]
    docker run --env-file [env_variables_file] -p 80:80 [image_name]

For deployment in Azure execute the scripts in the deploy folder, the scripts should be executed on the following order:

    ```bash
    cd deploy
    sh create_resources.sh
    sh deploy.sh

After the first deployment, if you make changes on the app, just run the deploy script since all the Azure resources are already created.
