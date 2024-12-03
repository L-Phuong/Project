import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv('C:/Electric_Vehicle_Population_Data.csv')  # Replace with your CSV path

# Ensure 'City' is a string column and fill NaN values
data['City'] = data['City'].fillna('Unknown').astype(str)

# Ensure 'Legislative District' is numeric, fill NaN values with a placeholder or appropriate value
data['Legislative District'] = pd.to_numeric(data['Legislative District'], errors='coerce').fillna(0)

# Check the data types
print(data.dtypes)

# ------------------------------ 1. Line Chart ------------------------------
plt.figure(figsize=(10, 6))
plt.plot(data['City'], data['Legislative District'])
plt.title('Line Chart')
plt.xlabel('City')
plt.ylabel('Legislative District')
plt.xticks(rotation=90)
plt.show()
