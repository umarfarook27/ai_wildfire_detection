import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load the dataset
data = pd.read_csv("sample_wildfire_data.csv")  # Make sure the CSV file is in the same folder as this script

# Step 2: Remove missing values (if any)
data.dropna(inplace=True)

# Step 3: Define features (X) and target labels (y)
X = data[['temperature', 'humidity', 'wind_speed', 'vegetation_dryness']]  # Features
y = data['fire_risk']  # Target variable (0 = Low Risk, 1 = High Risk)

# Step 4: Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Display dataset sizes
print("✅ Data Splitting Completed!")
print(f"Training Data Size: {X_train.shape}")
print(f"Testing Data Size: {X_test.shape}")
