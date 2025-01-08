import pandas as pd
import seaborn as sns  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

class MoviesDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_csv(self):
        try:
            self.data = pd.read_csv(self.file_path, encoding='ISO-8859-1')
            print("Data loaded successfully from:", self.file_path)
        except FileNotFoundError:
            print(f"The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV: {e}")

    def get_movie_ratings(self):
        if self.data is not None:
            # Plotting the histogram for 'vote_average' column (movie ratings)
            sns.histplot(self.data['vote_average'], kde=True)
            plt.title('Distribution of Ratings')
            plt.xlabel('Ratings')
            plt.ylabel('Frequency')
            plt.show()  # Show the plot
        else:
            print("No data available to get movie ratings.")
    
    def get_top_genres_by_average_rating(self):
        if self.data is not None:
            # Ensure 'genres' and 'vote_average' columns exist
            if 'genres' in self.data.columns and 'vote_average' in self.data.columns:
                # Split the genres column into lists (assuming genres are stored as strings separated by '|')
                self.data['genres'] = self.data['genres'].apply(lambda x: x.split('|') if isinstance(x, str) else [])

                # Explode the 'genres' column so each genre gets its own row
                genre_exploded = self.data.explode('genres')

                # Calculate the average rating for each genre
                genre_ratings = genre_exploded.groupby('genres')['vote_average'].mean().reset_index()

                # Sort genres by average rating (descending order)
                genre_ratings_sorted = genre_ratings.sort_values(by='vote_average', ascending=False)

                # Plot the top genres by average rating
                plt.figure(figsize=(10, 6))
                sns.barplot(x='vote_average', y='genres', data=genre_ratings_sorted.head(10), palette='viridis')
                plt.title('Top 10 Genres by Average Rating')
                plt.xlabel('Average Rating')
                plt.ylabel('Genre')
                plt.show()
            else:
                print("Required columns ('genres' or 'vote_average') are missing.")
        else:
            print("No data available to get movie ratings.")

    def plot_correlation_heatmap(self):
        if self.data is not None:
            # Select numeric columns for correlation calculation
            numeric_columns = ['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count']
            
            # Ensure that these columns exist in the data before proceeding
            missing_cols = [col for col in numeric_columns if col not in self.data.columns]
            if missing_cols:
                print(f"Missing columns in data: {', '.join(missing_cols)}")
                return
            
            # Calculate correlation matrix
            correlation_matrix = self.data[numeric_columns].corr()

            # Plot the heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
            plt.title('Correlation Heatmap of Movie Features')
            plt.show()
        else:
            print("No data available to generate correlation heatmap.")

if __name__ == "__main__":
    # File path for the movie dataset
    file_path = 'movie_dataset.csv'  # Adjust this path to your file

    # Creating an instance of MoviesDataHandler
    movies_data_handler = MoviesDataHandler(file_path)
    
    # Read data from the CSV file
    movies_data_handler.read_csv()
    
    # Generate the movie ratings histogram
    movies_data_handler.get_movie_ratings()
    movies_data_handler.get_top_genres_by_average_rating()
    movies_data_handler.plot_correlation_heatmap()
