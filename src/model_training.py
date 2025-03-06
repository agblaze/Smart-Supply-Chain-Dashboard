import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load preprocessed data
data = pd.read_csv('../data/inventory_data.csv')

# Feature Engineering
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Selecting Features and Target
features = ['Month', 'Year', 'Inventory_Level', 'Past_Demand']
target = 'Future_Demand'

X = data[features]
y = data[target]

# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Save model for later use
import joblib
joblib.dump(model, '../models/supply_chain_model.pkl')

print("Model saved successfully!")
