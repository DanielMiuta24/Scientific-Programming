import pandas as pd

class SalesDataHandler:
    def __init__(self, file_path):
        """
        Initializes the class with the file path to the CSV file.
        :param file_path: str, path to the CSV file.
        """
        self.file_path = file_path
        self.data = None

    def read_csv(self):
        """
        Reads the CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.file_path, encoding='ISO-8859-1')
            print("Data loaded successfully from:", self.file_path)
        except FileNotFoundError:
            print(f"The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV: {e}")

    def preprocess_data(self):
        """
        Converts 'Order Date' to datetime and fills missing 'Sales' values with 0.
        """
        if self.data is not None:
            # Convert 'Order Date' to datetime
            self.data['Order Date'] = pd.to_datetime(self.data['Order Date'], errors='coerce')
            
            # Fill missing values in 'Sales' with 0
            self.data['Sales'] = self.data['Sales'].fillna(0)
            print("Data preprocessing complete: 'Order Date' converted and 'Sales' filled with 0.")
        else:
            print("No data available to preprocess. Please load the data first.")

    def get_sales_by_category(self):
        """
        Creates a pivot table to calculate total sales for each combination of Region and Category.
        :return: Pivot table with sales by region and category.
        """
        if self.data is not None:
            region_category_sales = self.data.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum', fill_value=0)
            return region_category_sales
        else:
            print("No data available to get sales by category.")
            return None

    def get_monthly_sales(self):
        """
        Creates a pivot table to get the total sales for each month.
        :return: Pivot table of sales aggregated by month.
        """
        if self.data is not None:
            # Extract month from 'Order Date'
            self.data['Month'] = self.data['Order Date'].dt.to_period('M')
            
            # Pivot table to sum sales by month
            pivot_monthly_sales = self.data.pivot_table(values='Sales', index='Month', aggfunc='sum')
            
            # Fill missing sales data with 0
            pivot_monthly_sales = pivot_monthly_sales.fillna(0)
            return pivot_monthly_sales
        else:
            print("No data available to get monthly sales.")
            return None

    def display_sales_by_category(self):
        """
        Displays the sales data by region and category.
        """
        region_category_sales = self.get_sales_by_category()
        if region_category_sales is not None:
            print("\nSales by Region and Category:")
            print(region_category_sales)
        else:
            print("Unable to display sales by category.")

    def display_monthly_sales(self):
        """
        Displays the monthly sales trends.
        """
        monthly_sales = self.get_monthly_sales()
        if monthly_sales is not None:
            print("\nMonthly Sales Trends:")
            print(monthly_sales)
        else:
            print("Unable to display monthly sales.")

# Example Usage
if __name__ == "__main__":
    # File path for the Superstore CSV file
    file_path = 'Superstore.csv'

    # Create an object of SalesDataHandler with the file path
    sales_data_handler = SalesDataHandler(file_path)

    # Read the CSV data
    sales_data_handler.read_csv()

    # Preprocess the data (convert 'Order Date' to datetime and fill missing 'Sales' values)
    sales_data_handler.preprocess_data()

    # Display the sales by region and category using pivot table
    sales_data_handler.display_sales_by_category()

    # Display the monthly sales trends using pivot table
    sales_data_handler.display_monthly_sales()
