# Smart Supply Chain Dashboard
# Tech Stack: Python, Pandas, Scikit-learn, Power BI (for visualization)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import sqlite3

# Database Connection for Real-Time Data
def get_realtime_data():
    conn = sqlite3.connect('../database/supply_chain.db')  # Adjusted path
    query = "SELECT * FROM inventory_data"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Load dataset
data = get_realtime_data()

# Data Preprocessing
data = data.dropna()
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')

# Feature Engineering
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Selecting Features and Target
features = ['Month', 'Year', 'Inventory_Level', 'Past_Demand']
target = 'Future_Demand'

X = data[features]
y = data[target]

# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Inventory Alert System
threshold = data['Inventory_Level'].quantile(0.1)
data['Low_Stock_Alert'] = data['Inventory_Level'] < threshold

# Visualization Placeholder (To be developed in Power BI)
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Future_Demand'], label='Actual Demand')
plt.plot(data['Date'].iloc[-len(y_pred):], y_pred, label='Predicted Demand', linestyle='dashed')
plt.legend()
plt.show()

# Export processed data for Power BI integration
data.to_csv('../data/processed_supply_chain_data.csv', index=False)

print("Dashboard Data Ready for Power BI Visualization!")
