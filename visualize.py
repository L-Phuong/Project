import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C:/Fruit-Prices-2022.csv')

# Set up the figure size
plt.figure(figsize=(10, 6))


# 1. Line Chart
plt.plot(data['Fruit'], data['RetailPrice'], linestyle='-', color='b')
plt.title('Line Chart: RetailPrice vs Fruit')
plt.xticks(rotation=90)
plt.xlabel('Fruit')
plt.ylabel('RetailPrice Per Pound/Pint')
plt.show()

# 2. Bar Chart
plt.bar(data['Fruit'], data['RetailPrice'], color='g')
plt.title('Bar Chart: RetailPrice vs Fruit')
plt.xticks(rotation=90)
plt.xlabel('Fruit')
plt.ylabel('RetailPrice Per Pound/Pint')
plt.show()

# 3. Histogram
plt.hist(data['RetailPrice'], bins=10, color='orange')
plt.title('Histogram: RetailPrice')
plt.xlabel('RetailPrice Per Pound/Pint')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot
plt.scatter(data['Fruit'], data['RetailPrice'], color='r')
plt.title('Scatter Plot: RetailPrice vs Fruit')
plt.xticks(rotation=90)
plt.xlabel('Fruit')
plt.ylabel('RetailPrice Per Pound/Pint')
plt.show()

# 5. Pie Chart
plt.pie(data['RetailPrice'], labels= data['Fruit'])
plt.title('Pie Chart: RetailPrice Distribution')
plt.show()
