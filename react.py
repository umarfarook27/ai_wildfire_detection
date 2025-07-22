import pandas as pd

# Load dataset
data = pd.read_csv("sample_wildfire_data.csv")

# Display first few rows
print(data.head())

# Show dataset information
print(data.info())

# Check for missing values
print(data.isnull().sum())
