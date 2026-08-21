# 🌦️ Smart Retail Insights with Weather Integration

> An end-to-end **Data Engineering + Analytics + Machine Learning** project that collects historical weather data, stores it in PostgreSQL, visualizes weather trends, and generates a 7-day temperature forecast using Linear Regression.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-009688?style=for-the-badge)

</div>

---

## 📌 Overview

**Smart Retail Insights with Weather Integration** demonstrates a complete data pipeline for collecting, processing, storing, analyzing, visualizing, and forecasting weather data.

The project uses the **Open-Meteo Archive API** to collect historical weather data for **Nanded, Maharashtra**, processes the data using Python, stores it in a PostgreSQL database, and generates analytical visualizations using Matplotlib.

A basic **Linear Regression** model is then trained on historical temperature data to generate a **7-day temperature forecast**.

---

## 🎯 Project Objectives

- 🌐 Fetch historical weather data from a public REST API.
- 🐍 Process and transform data using Python.
- 🗄️ Store structured weather data in PostgreSQL.
- 📊 Visualize temperature and precipitation trends.
- 🤖 Apply Linear Regression for basic forecasting.
- 🔮 Generate temperature predictions for the next 7 days.
- 🔄 Demonstrate an end-to-end data engineering workflow.

---

## 🏗️ Data Pipeline Architecture

```text
                ┌─────────────────────────┐
                │   Open-Meteo Archive    │
                │           API           │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │     Data Extraction     │
                │         Python          │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │   Data Processing &     │
                │    Transformation       │
                │      Pandas / Python    │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │       PostgreSQL        │
                │      weather_data       │
                └────────────┬────────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
          ┌─────────────────┐  ┌─────────────────┐
          │  Visualization  │  │   ML Forecast   │
          │   Matplotlib    │  │ LinearRegression│
          └─────────────────┘  └────────┬────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │  7-Day Forecast │
                              └─────────────────┘
````

---

## 🛠️ Technology Stack

| Category          | Technology                 |
| ----------------- | -------------------------- |
| Programming       | Python                     |
| Data Source       | Open-Meteo Archive API     |
| Data Processing   | Pandas                     |
| Database          | PostgreSQL                 |
| Visualization     | Matplotlib                 |
| Machine Learning  | Scikit-learn               |
| ML Algorithm      | Linear Regression          |
| API Communication | REST API                   |
| Development       | VS Code / Jupyter Notebook |

---

## 📂 Project Structure

```text
Smart-Retail-Insights/
│
├── fetch_history.py
├── README.md
├── requirements.txt
│
├── images/
│   ├── temperature.png
│   ├── precipitation.png
│   └── forecast.png
│
└── ...
```

---

# 🔄 Data Engineering Workflow

## 1️⃣ Data Extraction

Historical weather data is collected using the **Open-Meteo Archive API**.

The project retrieves approximately **30 days of historical weather data for Nanded**.

The extraction process is implemented in:

```text
fetch_history.py
```

The collected dataset contains weather attributes such as:

* 🌡️ Temperature
* 💧 Humidity
* 💨 Wind Speed
* 🌧️ Precipitation
* 📅 Date

---

## 2️⃣ Data Storage

The processed weather data is stored in a PostgreSQL database named:

```text
smart_retail
```

The primary table is:

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

This provides a structured relational layer for querying and analyzing the collected weather data.

---

# 📊 Data Visualization

The project uses **Matplotlib** to analyze weather patterns across the collected 30-day dataset.

## 🌡️ Temperature Trend

The temperature trend visualization shows how the average temperature changed over the selected period.

<p align="center">
  <img src="images/Nanded temperature2.png" alt="30 Day Temperature Trend" width="850">
</p>

---

## 🌧️ Precipitation Analysis

The precipitation visualization shows the amount of precipitation recorded across the 30-day period.

<p align="center">
  <img src="images/Nanded precipitation.png" alt="30 Day Precipitation Trend" width="850">
</p>

---

# 🤖 Machine Learning Forecast

A **Linear Regression** model from Scikit-learn is used for basic temperature forecasting.

### Model Workflow

```text
Historical Temperature Data
            ↓
       Data Preparation
            ↓
     Feature Construction
            ↓
     Linear Regression
            ↓
       Model Training
            ↓
     Future Date Generation
            ↓
      7-Day Prediction
            ↓
      Visualization
```

The model is trained using the historical temperature observations and generates predicted temperatures for the following **7 days**.

The project then compares the historical temperature values with the generated predictions.

> ⚠️ **Note:** Linear Regression is used here as a basic machine-learning forecasting demonstration. It is not intended to replace production-grade weather forecasting systems.

---

## 🔮 7-Day Temperature Forecast

<p align="center">
  <img src="images/Nanded Temprature.png" alt="7 Day Temperature Forecast" width="850">
</p>

The forecast visualization compares:

* 🔵 Actual temperature observations
* 🔴 Predicted temperature values

---

# 📈 Results

The project successfully demonstrates a complete workflow from **data ingestion to predictive analysis**.

### Key Results

✅ Historical weather data retrieved through a public API.

✅ 30-day weather dataset collected for Nanded.

✅ Structured data stored in PostgreSQL.

✅ Temperature trends visualized using Matplotlib.

✅ Precipitation trends analyzed through visualization.

✅ Linear Regression model trained on historical temperature data.

✅ 7-day temperature forecast generated.

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Prathmesh-stack/Prathmesh_Bhokare_Data_engg_capstone_project.git
```

```bash
cd Prathmesh_Bhokare_Data_engg_capstone_project
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install pandas matplotlib scikit-learn requests psycopg2-binary
```

---

# 🗄️ PostgreSQL Configuration

Create the database:

```sql
CREATE DATABASE smart_retail;
```

Connect to the database and create the table:

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

Update your PostgreSQL connection credentials in the Python configuration before running the pipeline.

---

# ▶️ Running the Project

Run the historical data extraction script:

```bash
python fetch_history.py
```

The script retrieves the weather data and inserts the processed records into PostgreSQL.

After the data has been loaded, execute the visualization and forecasting scripts available in the repository.

---

# 💡 Key Data Engineering Concepts

This project demonstrates practical implementation of:

* 🔹 API-based data ingestion
* 🔹 Data extraction
* 🔹 Data transformation
* 🔹 Data validation
* 🔹 Relational database storage
* 🔹 PostgreSQL schema design
* 🔹 Python data processing
* 🔹 Data visualization
* 🔹 Machine learning integration
* 🔹 Basic predictive analytics
* 🔹 End-to-end pipeline development

---

# 🚀 Future Improvements

The project can be extended into a more robust production-oriented data platform.

### Planned Enhancements

* ⏰ Automate daily weather data ingestion.
* 🔄 Implement incremental data loading.
* 🧹 Add stronger data validation and cleaning.
* 📋 Add pipeline logging and monitoring.
* 🌍 Support multiple cities.
* 📊 Build an interactive dashboard using Streamlit or Power BI.
* 🤖 Experiment with advanced time-series forecasting models.
* 🐳 Containerize the pipeline using Docker.
* ☁️ Deploy the data pipeline to a cloud platform.
* 🔐 Improve database credential management using environment variables.

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Working with REST APIs and external data sources.
* Building Python-based data ingestion workflows.
* Designing relational database schemas.
* Working with PostgreSQL.
* Processing structured datasets using Pandas.
* Creating analytical visualizations.
* Applying machine learning to real-world datasets.
* Building an end-to-end data pipeline.

---

# 👨‍💻 Author

### Prathmesh Bhagwat Bhokare

**B.Tech — Computer Science & Engineering**
**Artificial Intelligence & Edge Computing**

[![GitHub](https://img.shields.io/badge/GitHub-Prathmesh--stack-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/Prathmesh-stack)

---

## ⭐ Repository

If you find this project useful or interesting, consider giving the repository a ⭐.

**Repository:**
https://github.com/Prathmesh-stack/Prathmesh_Bhokare_Data_engg_capstone_project

---

<p align="center">
  <b>Built with Python • PostgreSQL • APIs • Data Engineering • Machine Learning</b>
</p>
```
