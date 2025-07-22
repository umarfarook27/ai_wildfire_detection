import pandas as pd

# Load dataset (make sure the file is in the same directory as this script)
data = pd.read_csv("sample_wildfire_data.csv")

# Display first few rows
print("🔥 First 5 Rows of the Dataset:")
print(data.head())

# Show dataset information
print("\n📊 Dataset Info:")
print(data.info())

# Check for missing values
print("\n🔍 Missing Values in Each Column:")
print(data.isnull().sum())
