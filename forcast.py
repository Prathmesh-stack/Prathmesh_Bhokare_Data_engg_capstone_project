import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import timedelta

conn = psycopg2.connect(
    host="localhost",
    dbname="smart_retail",
    user="postgres",
    password="pratham@180405"
)

query = """
SELECT datetime, temperature
FROM weather_data
WHERE city = 'Nanded'
ORDER BY datetime;
"""
df = pd.read_sql(query, conn)
conn.close()

print("Data loaded from DB:")
print(df.tail())

df['datetime'] = pd.to_datetime(df['datetime'])

df['date_only'] = df['datetime'].dt.normalize()

df['day_num'] = (df['date_only'] - df['date_only'].min()).dt.days

X = df[['day_num']]
y = df['temperature']

model = LinearRegression()
model.fit(X, y)

last_date = df['date_only'].max()
print("Last historical date:", last_date)

future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=7)
future_day_nums = (future_dates - df['date_only'].min()).days.values.reshape(-1, 1)

preds = model.predict(future_day_nums)

forecast_df = pd.DataFrame({
    "date": future_dates,
    "predicted_temp": preds
})

print("\nNext 7 days predicted temperatures:")
print(forecast_df)

plt.figure(figsize=(10,5))
plt.plot(df['datetime'], df['temperature'], marker='o', label='Actual Temp (°C)')
plt.plot(forecast_df['date'], forecast_df['predicted_temp'], marker='x', linestyle='--', color='red', label='Predicted Temp (°C)')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Nanded - Temperature Forecast (Next 7 Days)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()