# Data Engineer Challenge

A REST API built with **FastAPI**, running on **Uvicorn**, containerized via **Docker**, and powered by a **MySQL** database. All running in the **Azure** cloud services.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [API Guide](#api-guide)
- [Setup & Installation](#setup--installation)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
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

### Libraries

We will use the following libraries in the project:
- fastapi
- uvicorn
- sqlalchemy
- pandas
- azure-storage-blob
- mysql-connector-python

The dependencies tree will end as shown below:

data-engineer-challenge v0.1.0
├── azure-storage-blob v12.25.0
│   ├── azure-core v1.32.0
│   │   ├── requests v2.32.3
│   │   │   ├── certifi v2025.1.31
│   │   │   ├── charset-normalizer v3.4.1
│   │   │   ├── idna v3.10
│   │   │   └── urllib3 v2.3.0
│   │   ├── six v1.17.0
│   │   └── typing-extensions v4.12.2
│   ├── cryptography v44.0.2
│   │   └── cffi v1.17.1
│   │       └── pycparser v2.22
│   ├── isodate v0.7.2
│   └── typing-extensions v4.12.2
├── fastapi[standard] v0.115.11
│   ├── pydantic v2.10.6
│   │   ├── annotated-types v0.7.0
│   │   ├── pydantic-core v2.27.2
│   │   │   └── typing-extensions v4.12.2
│   │   └── typing-extensions v4.12.2
│   ├── starlette v0.46.1
│   │   ├── anyio v4.8.0
│   │   │   ├── exceptiongroup v1.2.2
│   │   │   ├── idna v3.10
│   │   │   ├── sniffio v1.3.1
│   │   │   └── typing-extensions v4.12.2
│   │   └── typing-extensions v4.12.2
│   ├── typing-extensions v4.12.2
│   ├── email-validator v2.2.0 (extra: standard)
│   │   ├── dnspython v2.7.0
│   │   └── idna v3.10
│   ├── fastapi-cli[standard] v0.0.7 (extra: standard)
│   │   ├── rich-toolkit v0.13.2
│   │   │   ├── click v8.1.8
│   │   │   │   └── colorama v0.4.6
│   │   │   ├── rich v13.9.4
│   │   │   │   ├── markdown-it-py v3.0.0
│   │   │   │   │   └── mdurl v0.1.2
│   │   │   │   ├── pygments v2.19.1
│   │   │   │   └── typing-extensions v4.12.2
│   │   │   └── typing-extensions v4.12.2
│   │   ├── typer v0.15.2
│   │   │   ├── click v8.1.8 (*)
│   │   │   ├── rich v13.9.4 (*)
│   │   │   ├── shellingham v1.5.4
│   │   │   └── typing-extensions v4.12.2
│   │   ├── uvicorn[standard] v0.34.0
│   │   │   ├── click v8.1.8 (*)
│   │   │   ├── h11 v0.14.0
│   │   │   ├── typing-extensions v4.12.2
│   │   │   ├── colorama v0.4.6 (extra: standard)
│   │   │   ├── httptools v0.6.4 (extra: standard)
│   │   │   ├── python-dotenv v1.0.1 (extra: standard)
│   │   │   ├── pyyaml v6.0.2 (extra: standard)
│   │   │   ├── watchfiles v1.0.4 (extra: standard)
│   │   │   │   └── anyio v4.8.0 (*)
│   │   │   └── websockets v15.0.1 (extra: standard)
│   │   └── uvicorn[standard] v0.34.0 (extra: standard) (*)
│   ├── httpx v0.28.1 (extra: standard)
│   │   ├── anyio v4.8.0 (*)
│   │   ├── certifi v2025.1.31
│   │   ├── httpcore v1.0.7
│   │   │   ├── certifi v2025.1.31
│   │   │   └── h11 v0.14.0
│   │   └── idna v3.10
│   ├── jinja2 v3.1.6 (extra: standard)
│   │   └── markupsafe v3.0.2
│   ├── python-multipart v0.0.20 (extra: standard)
│   └── uvicorn[standard] v0.34.0 (extra: standard) (*)
├── mysql-connector-python v9.2.0
├── pandas v2.2.3
│   ├── numpy v2.0.2
│   ├── python-dateutil v2.9.0.post0
│   │   └── six v1.17.0
│   ├── pytz v2025.1
│   └── tzdata v2025.1
└── sqlalchemy v2.0.39
    ├── greenlet v3.1.1
    └── typing-extensions v4.12.2

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rogarol/data_engineer_challenge.git
   cd yourproject

2. **Install uv and initialize the project folder:**
- Follow the instructions to install uv according to your operating system (https://docs.astral.sh/uv/getting-started/installation/)
- Once installed, run the following command to use uv with this application (this creates the application layout and the pyproject.toml file)
    ```bash
     uv init --app

3. **Install the libraries needed:**
   ```bash
   uv add fastapi --extra standard 
   uv add uvicorn
   ...

4. **Install the libraries needed:**
   ```bash
   uv add fastapi --extra standard 
   uv add uvicorn
   ...

### Deployment