# Real-Time Weather Data Dashboard

## Objective: 
Develop a real-time weather pipeline that retrieves data from a public weather API, processes this data, and loads it into a cloud data warehouse. The project also includes the creation of a Power BI dashboard to visualize current weather conditions and trends.

## Tech Stack:
- Data Ingestion: Python (using `requests` for API data fetching)
- Data Storage: Azure SQL Database
- Orchestration and Scheduling: Docker
- Dashboarding: Power BI
- Pre-requisites: Obtain an API key and set up Azure environments with Azure SQL Database to facilitate data ingestion

## Project Files:

1. import.py
- This Python script is designed to fetch weather data from an API and subsequently load it into an Azure SQL Database.
- The API allows us to extract weather data for a specific city of interest.
  
2. Dockerfile
- The Dockerfile is a script that outlines the instructions for building the Docker image, including customizations for the environment in which the application will run.
- It contains the base image, necessary dependencies, and application code.

3. docker-compose.yml
- This file defines and manages the Docker application.
- It is utilized to schedule the application to run at regular intervals (e.g., pulling data every 10 minutes over the course of 1 hour)


## Running the code snippets:
Run the following commands:
- `docker build -t weather-pipeline .`
- `docker run --rm weather-pipeline`
- `docker-compose build`
- `docker-compose up`


  

