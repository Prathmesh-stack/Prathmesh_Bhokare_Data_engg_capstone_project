![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)
![Open-Meteo](https://img.shields.io/badge/Open--Meteo-Weather%20API-4CAF50)
![Psycopg2](https://img.shields.io/badge/Psycopg2-PostgreSQL%20Connector-336791)
![License](https://img.shields.io/badge/License-Educational-orange)

# 🌦️ Weather Data Engineering & Forecasting Pipeline

An end-to-end **Data Engineering and Machine Learning project** that extracts historical weather data for **Nanded, Maharashtra**, processes and stores the data in PostgreSQL, generates analytical visualizations, and forecasts temperature for the next 7 days using Linear Regression.

---

## 📌 Project Overview

This project demonstrates a complete data pipeline starting from **API-based data ingestion** to **database storage, visualization, and machine learning forecasting**.

Historical weather data is collected from the **Open-Meteo Archive API**, processed using Python, stored in PostgreSQL, and analyzed through visualizations. A Linear Regression model is then used as a baseline forecasting approach to estimate temperature for the upcoming 7 days.

### 🔄 Data Pipeline

```text
Open-Meteo API
      │
      ▼
Data Extraction
      │
      ▼
Data Processing
      │
      ▼
PostgreSQL Database
      │
      ├──────────────► Data Visualization
      │
      └──────────────► ML Forecasting
                              │
                              ▼
                       7-Day Forecast
```

---

## 🚀 Key Features

### 🌐 Data Ingestion

* Fetch historical weather data using the Open-Meteo Archive API
* Retrieve approximately 30 days of weather observations
* Collect daily maximum temperature, minimum temperature, and precipitation
* Process API responses using Python

### 🗄️ Data Engineering

* Transform raw API data into structured records
* Calculate daily average temperature
* Handle missing temperature values
* Store processed data in PostgreSQL
* Use Python and Psycopg2 for database connectivity

### 📊 Data Visualization

* Historical average temperature analysis
* Precipitation trend visualization
* Matplotlib-based analytical charts
* Historical data visualization for Nanded

### 🤖 Machine Learning

* Linear Regression-based temperature forecasting
* Convert historical dates into numerical values
* Train the model using historical temperature observations
* Generate predictions for the next 7 days
* Visualize historical and forecasted temperatures

---

## 🏗️ System Architecture

```text
                 ┌─────────────────────────┐
                 │   Open-Meteo API        │
                 │ Historical Weather Data │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Python Extraction     │
                 │       Requests          │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │    Data Processing      │
                 │                         │
                 │ • Temperature Average   │
                 │ • Date Processing       │
                 │ • Missing Value Check   │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │      PostgreSQL         │
                 │     weather_data        │
                 └────────────┬────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
          ┌──────────────────┐  ┌──────────────────┐
          │  Visualization   │  │ ML Forecasting   │
          │    Matplotlib    │  │ Linear Regression│
          └──────────────────┘  └────────┬─────────┘
                                         │
                                         ▼
                                ┌─────────────────┐
                                │  7-Day Forecast │
                                └─────────────────┘
```

---

## 🛠️ Tech Stack

### Programming & Data Processing

* Python 3.11
* Pandas
* Requests

### Database

* PostgreSQL
* Psycopg2

### Machine Learning

* Scikit-learn
* Linear Regression

### Visualization

* Matplotlib

### Data Source

* Open-Meteo Archive API

### Development

* VS Code
* Jupyter Notebook
* Git & GitHub

---

## 📂 Project Structure

```text
Prathmesh_Bhokare_Data_engg_capstone_project/
│
├── fetch_history.py
├── forcast.py
├── visulise.py
│
├── images/
│   ├── Nanded Perception.png
│   ├── Nanded temprature.png
│   └── Nanded temprature 2.png
│
├── Prathmesh_bhokare_41_capstone_project_DE.pdf
├── README.md
└── .gitignore
```

---

## 🗄️ Database Design

The project uses PostgreSQL to persist the processed weather observations.

### `weather_data`

| Column        | Type        | Description                           |
| ------------- | ----------- | ------------------------------------- |
| `id`          | SERIAL      | Primary key                           |
| `city`        | VARCHAR(50) | City name                             |
| `temperature` | FLOAT       | Calculated average temperature        |
| `humidity`    | FLOAT       | Currently used to store precipitation |
| `wind_speed`  | FLOAT       | Currently not populated               |
| `datetime`    | DATE        | Observation date                      |

### Temperature Transformation

The average daily temperature is calculated using:

```text
Average Temperature =
(Maximum Temperature + Minimum Temperature) / 2
```

> **Implementation Note:** The current database schema uses a column named `humidity` to store precipitation values. This can be renamed to `precipitation` in a future cleanup of the schema and scripts.

---

## 📡 Data Source

### Open-Meteo Archive API

The project uses historical weather data for **Nanded, Maharashtra**.

```text
Latitude  : 19.1485
Longitude : 77.3191
```

The pipeline retrieves:

* Daily maximum temperature
* Daily minimum temperature
* Daily precipitation

The extracted data is then transformed before being inserted into PostgreSQL.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Prathmesh-stack/Prathmesh_Bhokare_Data_engg_capstone_project.git

cd Prathmesh_Bhokare_Data_engg_capstone_project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install requests psycopg2 pandas matplotlib scikit-learn
```

---

## 🗄️ PostgreSQL Configuration

Create a PostgreSQL database:

```text
smart_retail
```

Create the required table:

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

Update the PostgreSQL connection settings in the Python scripts before running the project.

> 🔐 **Security Recommendation:** Database credentials should be stored using environment variables rather than being hard-coded in source files.

---

## ▶️ Running the Project

### 1. Fetch Historical Weather Data

```bash
python fetch_history.py
```

This script:

* Connects to the Open-Meteo API
* Retrieves historical weather observations
* Calculates average temperature
* Stores processed records in PostgreSQL

---

### 2. Generate Visualizations

```bash
python visulise.py
```

This generates the project's historical weather visualizations.

---

### 3. Generate Temperature Forecast

```bash
python forcast.py
```

This trains the Linear Regression model and generates a **7-day temperature forecast**.

---

# 📸 Project Screenshots

## 🌧️ Weather / Precipitation Analysis

<p align="center">   <img src="images/Nanded%20Perception.png" alt="Nanded Weather Precipitation Analysis" width="900"> </p>

---

## 🌡️ Historical Temperature Analysis

<p align="center">   <img src="images/Nanded%20temprature.png" alt="Nanded Historical Temperature Analysis" width="900"> </p>

---

## 🔮 Temperature Forecast

<p align="center">   <img src="images/Nanded%20temprature%202.png" alt="Nanded Temperature Forecast" width="900"> </p>

---

## 🤖 Machine Learning Workflow

The forecasting component follows the workflow:

```text
Historical Temperature Data
            │
            ▼
      Date Conversion
            │
            ▼
   Numerical Date Features
            │
            ▼
   Linear Regression Model
            │
            ▼
      Future Dates
            │
            ▼
   7-Day Temperature
       Predictions
```

### Model

The project uses:

```python
from sklearn.linear_model import LinearRegression
```

The model learns a simple relationship between historical dates and average temperature and uses that relationship to generate future predictions.

> **Note:** Linear Regression is used as a baseline forecasting model for demonstrating machine learning integration within the pipeline. It is not intended to be a production-grade meteorological forecasting model.

---

## 🧠 Learning Outcomes

Through this project, I gained practical experience in:

* REST API integration
* Data extraction and ingestion
* Data transformation using Python
* PostgreSQL database integration
* Relational database design
* Data visualization with Matplotlib
* Machine Learning with Scikit-learn
* Basic predictive analytics
* Building an end-to-end data pipeline
* Connecting data engineering workflows with machine learning

---

## 🔮 Future Enhancements

* Automated daily weather data ingestion
* Incremental data loading
* Improved data validation
* Logging and error handling
* Support for multiple cities
* Interactive dashboard using Streamlit or Power BI
* Advanced time-series forecasting models
* Docker containerization
* Cloud deployment
* Environment-variable based credential management

---

## 👨‍💻 Author

### Prathmesh Bhagwat Bhokare

**B.Tech Computer Science & Engineering**
**AI & Edge Computing**
**MIT ADT University**

---

## 📜 License

This project is developed for **educational and academic purposes**.
