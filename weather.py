import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class WeatherDataHandler:
    def __init__(self, file_path: str):
        """
        Initializes the WeatherDataHandler with a file path.
        
        :param file_path: Path to the weather data CSV file.
        """
        self.file_path = file_path
        self.data = None

    def read_csv(self) -> bool:
        """
        Reads the CSV file into the data attribute.
        
        :return: True if data was loaded successfully, False otherwise.
        """
        try:
            self.data = pd.read_csv(self.file_path, encoding='ISO-8859-1')
            print("Data loaded successfully from:", self.file_path)
            return True
        except FileNotFoundError:
            print(f"The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV: {e}")
        return False

    def prepare_data(self) -> bool:
        """
        Prepares the data for plotting by converting 'Date_Time' to datetime and 'Temperature_C' to numeric.
        
        :return: True if data preparation was successful, False otherwise.
        """
        if self.data is None:
            print("No data available to prepare.")
            return False
        
        # Ensure required columns exist
        required_columns = ['Date_Time', 'Temperature_C']
        if not all(column in self.data.columns for column in required_columns):
            print("The data is missing required columns.")
            return False
        
        # Ensure 'Date_Time' is a datetime column
        self.data['Date_Time'] = pd.to_datetime(self.data['Date_Time'], errors='coerce')
        
        # Convert 'Temperature_C' to numeric, coerce invalid values to NaN
        self.data['Temperature_C'] = pd.to_numeric(self.data['Temperature_C'], errors='coerce')
        
        # Drop rows with NaN values in 'Temperature_C' or 'Date_Time'
        self.data.dropna(subset=['Temperature_C', 'Date_Time'], inplace=True)
        
        # Extract year and month from 'Date_Time' into 'YearMonth'
        self.data['YearMonth'] = self.data['Date_Time'].dt.to_period('M')
        
        return True

    def plot_monthly_temperature_trends(self) -> None:
        """
        Plots the monthly temperature trends.
        """
        if not self.prepare_data():
            print("Data preparation failed. Cannot plot temperature trends.")
            return
        
        # Group by YearMonth and calculate the average temperature for each month
        monthly_avg_temp = self.data.groupby('YearMonth')['Temperature_C'].mean().reset_index()
        
        # Convert 'YearMonth' to string to avoid plotting issues
        monthly_avg_temp['YearMonth'] = monthly_avg_temp['YearMonth'].astype(str)
        
        # Plot the temperature trends using sns.lineplot()
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='YearMonth', y='Temperature_C', data=monthly_avg_temp, marker='o', color='blue')
        plt.title('Monthly Temperature Trends')
        plt.xlabel('Month')
        plt.ylabel('Average Temperature (°C)')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to avoid label clipping
        plt.show()

    def plot_humidity_temperature_relationship(self) -> None:
        """
        Plots the relationship between humidity and temperature using a scatter plot.
        """
        if not self.prepare_data():
            print("Data preparation failed. Cannot plot humidity-temperature relationship.")
            return
        
        # Plot the humidity-temperature relationship using sns.scatterplot()
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='Humidity_pct', y='Temperature_C', data=self.data, color='blue')
        plt.title('Humidity-Temperature Relationship')
        plt.xlabel('Humidity')
        plt.ylabel('Temperature (°C)')
        plt.show()
    

if __name__ == "__main__":
    # File path for the weather dataset (replace with your dataset's path)
    file_path = 'weather_data.csv'  # Update this with your file's path
    
    # Create an instance of WeatherDataHandler
    weather_data_handler = WeatherDataHandler(file_path)
    
    # Read data from the CSV file
    if not weather_data_handler.read_csv():
        print("Failed to load data. Exiting.")
        exit()
    
    # Plot the monthly temperature trends
    weather_data_handler.plot_monthly_temperature_trends()
    weather_data_handler.plot_humidity_temperature_relationship()