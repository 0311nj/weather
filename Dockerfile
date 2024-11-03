FROM python:3.9-slim

WORKDIR /app

# Copy the script into the container
COPY import.py .

# Install necessary dependencies
RUN pip install requests pandas sqlalchemy pyodbc

RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get install -y unixodbc-dev \
    && pip install requests pandas sqlalchemy pyodbc \
    && apt-get clean


# Command to run the Python script
CMD ["python", "import.py"]

