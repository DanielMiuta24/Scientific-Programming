import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore # type: ignore
from sklearn.tree import DecisionTreeRegressor # type: ignore
from sklearn.ensemble import RandomForestRegressor # type: ignore
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score # type: ignore
import matplotlib.pyplot as plt

class Helper:
    def __init__(self, df):
        self.df = df
        self.df_encoded = None

    def preprocess_data(self):
        self.df_encoded = pd.get_dummies(self.df, drop_first=True)
        X = self.df_encoded.drop(columns=['tip'])
        y = self.df_encoded['tip']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, model, X_train, y_train):
        model.fit(X_train, y_train)
        return model

    def evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        return y_pred, mae, mse

    def visualize_results(self, y_test, y_pred, title):
        plt.scatter(y_test, y_pred)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.title(title)
        plt.xlabel('Actual Tip')
        plt.ylabel('Predicted Tip')
        plt.show()

    def feature_importance(self, model, X_train):
        if hasattr(model, 'feature_importances_'):
            feature_importances = model.feature_importances_
            features = X_train.columns
            importances_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances}).sort_values(by='Importance', ascending=False)
            plt.barh(importances_df['Feature'], importances_df['Importance'])
            plt.title('Feature Importance')
            plt.show()

    def residuals_plot(self, y_test, y_pred):
        residuals = y_test - y_pred
        plt.scatter(y_pred, residuals)
        plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), color='red')
        plt.title('Residuals')
        plt.xlabel('Predicted Tip')
        plt.ylabel('Residuals')
        plt.show()