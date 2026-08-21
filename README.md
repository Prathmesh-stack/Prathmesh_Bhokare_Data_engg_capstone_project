# Smart Retail Insights with Weather Integration

A data engineering and analytics project that collects historical weather data using the **Open-Meteo Archive API**, stores structured data in **PostgreSQL**, visualizes weather trends using **Matplotlib**, and applies **Linear Regression** to forecast temperature for the next 7 days.

## 📌 Project Overview

Weather conditions can influence customer behavior, product demand, inventory planning, and retail operations. This project demonstrates a simple end-to-end data pipeline that transforms raw weather API data into structured, analyzable data and generates basic predictive insights.

The pipeline focuses on weather data for **Nanded, Maharashtra**, using the previous 30 days of historical data.

### Pipeline

```text
Open-Meteo Archive API
        ↓
Data Extraction
        ↓
Python Data Processing
        ↓
PostgreSQL Database
        ↓
Data Analysis
        ↓
Matplotlib Visualization
        ↓
Linear Regression
        ↓
7-Day Temperature Forecast
```

## 🎯 Objectives

* Fetch historical weather data from a public API.
* Process and structure the collected data using Python.
* Store weather data in a PostgreSQL database.
* Visualize temperature and precipitation trends for the last 30 days.
* Apply a basic machine learning model for temperature forecasting.
* Generate a 7-day temperature forecast from historical observations.

## 🛠️ Tech Stack

| Category                | Technologies                |
| ----------------------- | --------------------------- |
| Programming Language    | Python                      |
| API                     | Open-Meteo Archive API      |
| Database                | PostgreSQL                  |
| Data Processing         | Pandas                      |
| Data Visualization      | Matplotlib                  |
| Machine Learning        | Scikit-learn                |
| ML Algorithm            | Linear Regression           |
| Database Connectivity   | Python PostgreSQL libraries |
| Development Environment | VS Code / Jupyter Notebook  |

## 📊 Data Pipeline

### 1. Data Extraction

Historical weather data is retrieved from the **Open-Meteo Archive API**.

The project collects weather information for **Nanded** covering the previous 30 days.

The extraction process is implemented using:

```text
fetch_history.py
```

The collected data includes weather attributes such as:

* Temperature
* Humidity
* Wind Speed
* Precipitation
* Date

### 2. Data Storage

The processed weather data is stored in a PostgreSQL database named:

```text
smart_retail
```

The primary table used in the project is:

```text
weather_data
```

### Database Schema

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    datetime DATE
);
```

The database provides a structured storage layer for the extracted weather information and allows the data to be queried for analysis and visualization.

## 📈 Data Visualization

The project uses **Matplotlib** to analyze weather trends over the 30-day period.

### Temperature Trend

A time-series visualization is generated to analyze the change in average temperature over the selected period.

```text
Temperature vs Date
```

### Precipitation Analysis

A precipitation chart is also generated to visualize daily precipitation levels throughout the 30-day period.

The visualizations help identify changes and patterns in weather conditions over time.

## 🤖 Machine Learning Forecasting

A basic **Linear Regression** model from Scikit-learn is used to demonstrate predictive analysis.

### Model Workflow

```text
Historical Temperature Data
          ↓
Data Preparation
          ↓
Linear Regression
          ↓
Model Training
          ↓
Future Date Generation
          ↓
7-Day Temperature Forecast
```

The model is trained using the historical temperature data collected for the previous 30 days and is used to generate temperature predictions for the following **7 days**.

The results are visualized by comparing:

* Actual temperature values
* Predicted temperature values

> **Note:** The Linear Regression model is implemented as a basic forecasting demonstration and should not be considered a production-grade weather forecasting model.

## 📊 Results

The project successfully demonstrates the complete workflow from data collection to predictive analysis.

### Key Outcomes

* Historical weather data successfully extracted from the Open-Meteo Archive API.
* 30 days of weather data collected for Nanded.
* Structured weather data stored in PostgreSQL.
* Temperature trends visualized using Matplotlib.
* Precipitation patterns visualized over the selected period.
* Linear Regression applied to historical temperature data.
* Temperature forecast generated for the next 7 days.

## 📁 Project Structure

```text
Smart-Retail-Insights/
│
├── fetch_history.py
│
├── README.md
│
├── requirements.txt
│
├── data/
│
├── visualizations/
│
└── notebooks/
```

> The exact directory structure may vary depending on the files included in the repository.

## ⚙️ Installation

### 1. Clone the Repository

Clone the repository to your local machine and navigate to the project directory.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the required libraries:

```bash
pip install pandas matplotlib scikit-learn requests psycopg2-binary
```

## 🗄️ PostgreSQL Setup

Create the PostgreSQL database:

```sql
CREATE DATABASE smart_retail;
```

Connect to the database and create the weather table:

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    datetime DATE
);
```

Update the PostgreSQL connection configuration in the Python script according to your local database credentials.

## ▶️ Running the Project

Run the data extraction script:

```bash
python fetch_history.py
```

The script retrieves historical weather data and inserts the processed records into PostgreSQL.

After the data has been stored, the visualization and forecasting scripts can be executed to generate the analytical outputs.

## 📷 Project Outputs

The project generates visualizations including:

### 30-Day Temperature Trend

A line chart showing the temperature variation across the previous 30 days.

### 30-Day Precipitation Trend

A bar chart showing daily precipitation during the selected period.

### 7-Day Temperature Forecast

A comparison between historical/actual temperature values and the Linear Regression predictions for the following 7 days.

## 🔑 Key Data Engineering Concepts Demonstrated

This project demonstrates several fundamental data engineering concepts:

* API-based data ingestion
* Data extraction and transformation
* Structured data storage
* Relational database design
* PostgreSQL data management
* Data processing with Python
* Data visualization
* Basic predictive analytics
* End-to-end data pipeline development

## 🚀 Future Improvements

The current implementation can be extended into a more robust data engineering and analytics platform.

Possible improvements include:

* Automating daily data ingestion with scheduled jobs.
* Implementing incremental data loading instead of manually fetching historical data.
* Adding data validation and error handling.
* Creating an automated ETL pipeline.
* Adding more weather variables and locations.
* Building an interactive dashboard using Power BI, Streamlit, or similar tools.
* Implementing more advanced time-series forecasting models.
* Adding automated database backups and logging.
* Containerizing the application using Docker.
* Deploying the pipeline to a cloud environment.

## 🧠 Learning Outcomes

Through this project, I gained practical experience in:

* Working with external REST APIs.
* Designing and working with PostgreSQL databases.
* Building Python-based data ingestion workflows.
* Transforming and analyzing structured datasets.
* Creating data visualizations from historical data.
* Applying machine learning to a real-world dataset.
* Developing an end-to-end data pipeline.

## 👨‍💻 Author

**Prathmesh Bhagwat Bhokare**

B.Tech — Computer Science & Engineering
Artificial Intelligence & Edge Computing

GitHub: `Prathmesh-stack`

---

## ⭐ Project Summary

**Smart Retail Insights with Weather Integration** demonstrates an end-to-end workflow for collecting, storing, analyzing, visualizing, and forecasting weather data using Python, PostgreSQL, APIs, and machine learning.

The project combines **Data Engineering + Data Analytics + Machine Learning** into a single practical pipeline.
