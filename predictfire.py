import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
data = pd.read_csv("sample_wildfire_data.csv")

# Step 2: Remove missing values
data.dropna(inplace=True)

# Step 3: Define features (X) and target labels (y)
X = data[['temperature', 'humidity', 'wind_speed', 'vegetation_dryness']]
y = data['fire_risk']

# Step 4: Split data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train AI Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate Model Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ AI Model Trained Successfully! Accuracy: {accuracy * 100:.2f}%")

# Step 7: Predict Fire Risk for New Data
new_data = pd.DataFrame([[35, 20, 12, 80]], columns=['temperature', 'humidity', 'wind_speed', 'vegetation_dryness'])
prediction = model.predict(new_data)

# Convert output to readable text
risk_level = "🔥 High Fire Risk" if prediction[0] == 1 else "✅ Low Fire Risk"

# Step 8: Print Prediction Result
print(f"🚨 Predicted Fire Risk: {risk_level}")
