# 1. Import necessary libraries

import pandas as pd 
import requests
from sqlalchemy import create_engine
import urllib
import time

# 2. Set up API key and link

API_KEY = API_KEY # To include your API key here
CITY = 'Taipei'
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

# 3. Fetch data from API 
for _ in range(4):

    response = requests.get(API_URL)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        continue
    data = response.json()

# 4. Process data


    weather_data = {
        'city': CITY,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'timestamp': pd.Timestamp.now()
    }

    df = pd.DataFrame([weather_data])


# Below are codes relevant for an Azure SQL database deployment:

    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=SERVER.database.windows.net;" # Inlcude relevant information
        "DATABASE=DATABASE;" # Inlcude relevant information
        "UID=USERNAME;" # Inlcude relevant information
        "PWD=PWD;" # Inlcude relevant information
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Load data into the SQL Server table. This snippet is relevant for local / cloud DB deployment
    try:
        df.to_sql('weather_data', engine, if_exists='append', index=False)
        print("Data loaded successfully")
    except Exception as e:
        print(f"Error loading data: {e}")
    
    time.sleep(30)
