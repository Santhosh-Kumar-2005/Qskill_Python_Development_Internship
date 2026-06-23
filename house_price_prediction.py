import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset (download from Kaggle, e.g., "House Prices: Advanced Regression Techniques")
data = pd.read_csv("house_prices.csv")

# Select relevant features
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF']
X = data[features]
y = data['SalePrice']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Example prediction
sample_house = [[7, 2000, 2, 800]]  # Quality=7, Size=2000 sqft, Garage=2, Basement=800 sqft
predicted_price = model.predict(sample_house)
print(f"Predicted House Price: ${predicted_price[0]:,.2f}")
