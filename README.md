# Prathmesh_Bhokare_Data_engg_capstone_project
Weather Data Analysis and Forecasting System
Project Overview

This project collects historical weather data for Nanded using the Open-Meteo API, stores it in a PostgreSQL database, analyzes the collected data, and predicts future temperatures using a Machine Learning model.

The system consists of three main modules:

Weather Data Collection and Storage
Temperature Forecasting using Linear Regression
Weather Data Visualization
Objectives
Fetch historical weather data from Open-Meteo API.
Store weather information in PostgreSQL.
Analyze temperature trends over time.
Predict future temperatures for the next 7 days.
Visualize temperature and precipitation patterns.
Technologies Used
Programming Language
Python
Database
PostgreSQL
Libraries
requests
psycopg2
pandas
numpy
matplotlib
scikit-learn
API
Open-Meteo Historical Weather API
Database Schema
Table: weather_data
Column	Data Type	Description
id	SERIAL	Primary Key
city	TEXT	City Name
temperature	REAL	Average Daily Temperature
humidity	REAL	Precipitation Value
wind_speed	REAL	Wind Speed
datetime	DATE	Weather Date
Module 1: Weather Data Collection
Description

This module fetches the last 30 days of historical weather data for Nanded from the Open-Meteo API.

Data Collected
Maximum Temperature
Minimum Temperature
Precipitation
Processing

The average temperature is calculated using:

Average Temperature = (Maximum Temperature + Minimum Temperature) / 2

The processed data is then stored in the PostgreSQL database.

Output
Weather records inserted into weather_data table.
Automatic table creation if it does not exist.
Module 2: Temperature Forecasting
Description

This module retrieves historical temperature data from PostgreSQL and trains a Linear Regression model.

Steps
Load temperature data from database.
Convert dates into numerical values.
Train Linear Regression model.
Predict temperatures for the next 7 days.
Display forecasted temperatures.
Machine Learning Algorithm

Linear Regression

Output
Predicted temperatures for next 7 days.
Forecast graph showing actual and predicted temperatures.
Module 3: Data Visualization
Description

This module creates visual representations of weather data.

Visualizations
Temperature Trend Graph

Shows average temperature variation over the last 30 days.

Precipitation Bar Chart

Shows daily precipitation values collected from the API.

Output
Temperature trend line chart.
Precipitation bar graph.
Project Workflow
Fetch weather data from Open-Meteo API.
Store data in PostgreSQL database.
Retrieve data for analysis.
Train Linear Regression model.
Predict future temperatures.
Visualize historical and forecasted weather trends.
Installation
Install Required Packages
pip install requests psycopg2 pandas numpy matplotlib scikit-learn
PostgreSQL Setup

Create a database named:

CREATE DATABASE smart_retail;

Update the database credentials in all Python files:

host="localhost"
dbname="smart_retail"
user="postgres"
password="your_password"
How to Run
Step 1: Collect Weather Data
python weather_data_collection.py
Step 2: Generate Temperature Forecast
python temperature_forecasting.py
Step 3: Visualize Weather Data
python weather_visualization.py
Sample Output
Forecast
Date	Predicted Temperature (°C)
Day 1	32.5
Day 2	32.8
Day 3	33.0
Day 4	33.2
Day 5	33.4
Day 6	33.6
Day 7	33.8
Future Enhancements
Use advanced forecasting models such as ARIMA or LSTM.
Store additional weather parameters.
Build a web dashboard using Flask or Streamlit.
Add real-time weather monitoring.
Improve prediction accuracy using larger datasets.
Conclusion

This project demonstrates an end-to-end weather analytics pipeline using Python, PostgreSQL, APIs, Data Visualization, and Machine Learning. Historical weather data is collected, stored, analyzed, visualized, and used to forecast future temperatures, providing useful insights into local weather trends.
