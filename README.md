# Data Engineer Challenge

A high-performance REST API built with **FastAPI**, running on **Uvicorn**, containerized via **Docker**, and powered by a **SQL** database.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project is designed to provide a robust REST API that can scale and integrate with modern applications. It leverages the asynchronous capabilities of FastAPI along with the high performance of Uvicorn, while ensuring portability and consistency through Docker containers. The SQL-based database ensures reliable data storage and retrieval.

## Features

- **DB Migration:** Load historical data of 3 tables (departments, jobs, employees).
    - Receive historical data from CSV files
    - Upload these files to the new DB
    - Be able to insert batch transactions (1 up to 1000 rows) with one request

- **Business Metrics:** Efficient request handling with FastAPI and Uvicorn.

## Architecture

The application follows a modular and layered architecture:
- **API Layer:** Exposes endpoints using FastAPI.
- **Service Layer:** Contains business logic.
- **Data Access Layer:** Interacts with the SQL database (consider using an ORM like SQLAlchemy).
- **Server:** Uvicorn serves the API asynchronously.
- **Containerization:** Docker ensures environment consistency across development, testing, and production.

A simplified diagram:

+--------------------+ | Client | +---------+----------+ | v +--------------------+ Docker | FastAPI | <-----------------+ | (Endpoints & API) | | +---------+----------+ | | | v | +--------------------+ | | Business Logic | | +---------+----------+ | | | v | +--------------------+ | | SQL Database | | +--------------------+ |

## Tech Stack

- **FastAPI:** For building the REST API.
- **Uvicorn:** ASGI server for running the application.
- **Docker:** For containerization and deployment.
- **SQL Database:** Any SQL RDBMS (e.g., PostgreSQL, MySQL, SQLite) based on your requirements.

## Setup & Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9
- Git

### Libraries

We will add to uv two libraries with the following commands:
- fastapi
- uvicorn

The dependencies tree will end as shown below:

    data-engineer-challenge v0.1.0
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
    │   │   │   ├── rich v13.9.4
    │   │   │   │   ├── markdown-it-py v3.0.0
    │   │   │   │   │   └── mdurl v0.1.2
    │   │   │   │   ├── pygments v2.19.1
    │   │   │   │   └── typing-extensions v4.12.2
    │   │   │   └── typing-extensions v4.12.2
    │   │   ├── typer v0.15.2
    │   │   │   ├── click v8.1.8
    │   │   │   ├── rich v13.9.4 (*)
    │   │   │   ├── shellingham v1.5.4
    │   │   │   └── typing-extensions v4.12.2
    │   │   ├── uvicorn[standard] v0.34.0
    │   │   │   ├── click v8.1.8
    │   │   │   ├── h11 v0.14.0
    │   │   │   ├── typing-extensions v4.12.2
    │   │   │   ├── httptools v0.6.4 (extra: standard)
    │   │   │   ├── python-dotenv v1.0.1 (extra: standard)
    │   │   │   ├── pyyaml v6.0.2 (extra: standard)
    │   │   │   ├── uvloop v0.21.0 (extra: standard)
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
    └── uvicorn v0.34.0 (*)

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