
from Helper import Helper
from sklearn.tree import DecisionTreeRegressor # type: ignore
import pandas as pd

# Example dataset
data = {
    'budget': [100, 150, 200, 120, 300],
    'genre_encoded': [0, 1, 0, 1, 1],
    'director_encoded': [2, 3, 1, 2, 3],
    'revenue': [550, 700, 900, 600, 1200]
}
movies = pd.DataFrame(data)

# Initialize helper
helper = Helper(movies)

# Preprocess data
X_train, X_test, y_train, y_test = helper.preprocess_data()

# Train and evaluate Decision Tree
model = DecisionTreeRegressor(random_state=42)
helper.train_model(model, X_train, y_train)
y_pred, mse, r2 = helper.evaluate_model(model, X_test, y_test)
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared: {r2}")
