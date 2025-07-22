import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
data = pd.read_csv("sample_wildfire_data.csv")  # Ensure the file is in the same folder

# Step 2: Remove missing values
data.dropna(inplace=True)

# Step 3: Define features (X) and target labels (y)
X = data[['temperature', 'humidity', 'wind_speed', 'vegetation_dryness']]
y = data['fire_risk']

# Step 4: Split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and Train the AI Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Predict on Test Data
y_pred = model.predict(X_test)

# Step 7: Evaluate Model Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"🔥 AI Model Accuracy: {accuracy * 100:.2f}%")
