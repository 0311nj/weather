# 1. Import necessary libraries

# pip install pyodbc
# pip install pandas

import pandas as pd 
import requests
from sqlalchemy import create_engine
import urllib

# 2. Set up API key and link

API_KEY = '2e5728419e6e085790cba040a01e5467'
CITY = 'Taipei'
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

# 3. Fetch data from API 

response = requests.get(API_URL)
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


# Below are codes relevant for a local SQL server database (hosted in SSMS). Commented out as this is not necessary: 

# params = urllib.parse.quote_plus(
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=TEO\SQLEXPRESS;"  # Adjust SERVER as needed (e.g., SERVER=.\SQLEXPRESS)
#     "DATABASE=WeatherDB;"  # Replace with your database name
#     "Trusted_Connection=yes;"
# )

# engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Below are codes relevant for an Azure SQL database deployment:

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=serverfortesting.database.windows.net;"
    "DATABASE=WeatherDB;"
    "UID=administrator_test;"
    "PWD=Database123;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Load data into the SQL Server table. This snippet is relevant for local / cloud DB deployment
df.to_sql('weather_data', engine, if_exists='append', index=False)
print("Data loaded successfully")
