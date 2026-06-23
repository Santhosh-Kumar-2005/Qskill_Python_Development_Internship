import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset
data = pd.read_csv("Housing.csv")

print(data.head())

# Convert categorical columns
data = pd.get_dummies(data, drop_first=True)

# Features
X = data.drop("price", axis=1)

# Target
y = data["price"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)

# Test Prediction
sample_house = X_test.iloc[0:1]
predicted_price = model.predict(sample_house)

print("\nPredicted House Price:", predicted_price[0])
