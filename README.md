# Smart Supply Chain Dashboard

## Overview
The **Smart Supply Chain Dashboard** is a machine learning-powered analytics tool that forecasts demand, monitors inventory levels, and provides real-time insights for efficient supply chain management. The system integrates **Python, SQLite, Scikit-learn, and Power BI** to ensure real-time data processing and visualization.

## Features
- **Real-time Data Integration**: Fetches inventory and demand data from an SQLite database.
- **Machine Learning-Based Demand Forecasting**: Uses Random Forest Regression to predict future demand.
- **Inventory Alert System**: Identifies low stock levels and raises alerts.
- **Data Visualization**: Plots actual vs. predicted demand using Matplotlib.
- **Power BI Integration**: Processes data for interactive dashboards and automated updates.

## Tech Stack
- **Python** (Data Processing, ML Model, Visualization)
- **SQLite** (Real-time Data Storage)
- **Pandas, NumPy, Scikit-learn** (Data Handling & ML)
- **Matplotlib** (Visualization)
- **Power BI** (Dashboard & Reporting)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- SQLite
- Power BI (for visualization)
- Required Python libraries:
  ```bash
  pip install pandas numpy matplotlib scikit-learn sqlite3
  ```

### Database Setup
1. Create an SQLite database `supply_chain.db` and a table `inventory_data` with the following structure:
   ```sql
   CREATE TABLE inventory_data (
       Date TEXT,
       Inventory_Level INTEGER,
       Past_Demand INTEGER,
       Future_Demand INTEGER
   );
   ```
2. Populate it with inventory and demand data.

### Running the Model
Run the Python script to process data and generate insights:
```bash
python smart_supply_chain.py
```

### Power BI Integration
1. Open **Power BI** and import `processed_supply_chain_data.csv`.
2. Create visuals:
   - Line chart for **Actual vs. Predicted Demand**.
   - Table with **Low Stock Alerts**.
   - KPI Cards for **Mean Absolute Error (MAE)** and inventory levels.
3. Enable **Auto-Refresh** for real-time updates.

## Usage
1. **Predict Future Demand**: The ML model analyzes historical data and forecasts demand trends.
2. **Monitor Inventory Levels**: Alerts highlight when stock levels are critically low.
3. **Visualize Insights**: Power BI dashboards enhance decision-making.

## Future Enhancements
- **Live API Integration** for dynamic data updates.
- **Enhanced ML Models** for improved prediction accuracy.
- **Automated Reporting** via scheduled Power BI reports.

## Contributing
Feel free to fork this repository and submit pull requests to enhance functionality.

## License
This project is licensed under the MIT License.

---
**Developed by:** Abdullah Ejaz
