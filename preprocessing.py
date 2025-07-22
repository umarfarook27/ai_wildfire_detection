import pandas as pd

# Load dataset (use the correct file path if needed)
data = pd.read_csv("sample_wildfire_data.csv")

# Step 1: Remove missing values (if any)
data.dropna(inplace=True)

# Step 2: Define features (X) and target labels (y)
X = data[['temperature', 'humidity', 'wind_speed', 'vegetation_dryness']]  # Features
y = data['fire_risk']  # Target variable (0 = Low Risk, 1 = High Risk)

# Step 3: Display dataset information after preprocessing
print("✅ Data Preprocessing Completed!")
print("\n🔥 First 5 Rows of Preprocessed Data:")
print(data.head())

print("\n📊 Summary of Dataset:")
print(data.describe())

print("\n🔍 Checking for Missing Values (After Cleanup):")
print(data.isnull().sum())
