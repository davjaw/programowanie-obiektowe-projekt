import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from customtkinter import *

# Load the CSV file
file_path = '../scrapedMovies/imdb.csv'
data = pd.read_csv(file_path)

# Remove any non-numeric values from the 'Rating amount' column
data = data[data['Rating amount'] != 'Rating amount']

# Adjust the conversion function to handle both string and numeric values
def convert_rating_amount(amount):
    try:
        if isinstance(amount, str) and 'K' in amount:
            return float(amount.replace('K', '')) * 1e3
        return float(amount)
    except ValueError:
        return 0

data['Rating amount'] = data['Rating amount'].apply(convert_rating_amount)

# Convert the 'Rating' column to numeric, forcing errors to NaN
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Base class for charts
class ChartStrategy:
    def __init__(self, frame, data):
        self.frame = frame
        self.data = data

    def plot(self):
        pass

# Concrete strategy for Average Rating per Year Chart
class AvgRatingPerYearChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Calculate the average rating by year
        avg_rating_per_year = self.data.groupby('Year')['Rating'].mean().reset_index()

        # Create the column chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.bar(avg_rating_per_year['Year'], avg_rating_per_year['Rating'], color='#C0256F')
        ax.set_xlabel('Year', color="white")
        ax.set_ylabel('Average Rating', color="white")
        ax.set_title('Average Rating per Year', color="white")
        ax.set_xticklabels(avg_rating_per_year['Year'], rotation=45, color="white")
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

# Concrete strategy for Average Rating per Genre Chart
class AvgRatingPerGenreChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Calculate the average rating for each genre
        avg_rating_per_genre = self.data.groupby('Genre')['Rating'].mean().reset_index()

        # Create the column chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.bar(avg_rating_per_genre['Genre'], avg_rating_per_genre['Rating'], color='#C0256F')
        ax.set_xlabel('Genre', color="white")
        ax.set_ylabel('Average Rating', color="white")
        ax.set_title('Average Rating per Genre', color="white")
        ax.set_xticklabels(avg_rating_per_genre['Genre'], rotation=45, color="white")
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

# Concrete strategy for Genre Distribution Chart
class GenreDistributionChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Calculate the percentage of each genre
        genre_counts = self.data['Genre'].value_counts(normalize=True) * 100

        # Create the pie chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors, textprops={'color':"white"})
        ax.set_title('Genre Distribution (%)', color="white")

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

# Concrete strategy for Percentage Distribution of Each Genre per Year
class GenrePercentagePerYearChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Calculate the percentage distribution of each genre per year
        genre_percentage_per_year = self.data.groupby(['Year', 'Genre']).size().unstack(fill_value=0)
        genre_percentage_per_year = genre_percentage_per_year.div(genre_percentage_per_year.sum(axis=1), axis=0) * 100

        # Create the scatter plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        for genre in genre_percentage_per_year.columns:
            ax.scatter(genre_percentage_per_year.index, genre_percentage_per_year[genre], label=genre)

        ax.set_xlabel('Year', color="white")
        ax.set_ylabel('Percentage', color="white")
        ax.set_title('Genre Percentage per Year', color="white")
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="top", fill=tk.BOTH, expand=1)

        # Create legend outside of the chart below it
        handles, labels = ax.get_legend_handles_labels()
        fig_legend = plt.figure(figsize=(10, 0.5))
        fig_legend.legend(handles, labels, loc='upper center', ncol=5, fontsize='small', facecolor='#1b243a', edgecolor='white', labelcolor="white")
        fig_legend.patch.set_facecolor('#1b243a')
        canvas_legend = FigureCanvasTkAgg(fig_legend, master=self.frame)
        canvas_legend.draw()
        canvas_legend.get_tk_widget().configure(background='#1b243a')
        canvas_legend.get_tk_widget().pack(side="top", fill=tk.BOTH, expand=1)

# Concrete strategy for Total Ratings per Year Scatter Plot
class TotalRatingsPerYearChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Sum the rating amounts by year
        ratings_per_year = self.data.groupby('Year')['Rating amount'].sum().reset_index()

        def format_yaxis_shorten(x, pos):
            if x >= 1e15:
                return f'{x / 1e15:.1f}Q'
            elif x >= 1e12:
                return f'{x / 1e12:.1f}T'
            elif x >= 1e9:
                return f'{x / 1e9:.1f}B'
            elif x >= 1e6:
                return f'{x / 1e6:.1f}M'
            elif x >= 1e3:
                return f'{x / 1e3:.1f}K'
            else:
                return f'{x:.0f}'
            
        # Create the scatter plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.scatter(ratings_per_year['Year'], ratings_per_year['Rating amount'], color='#C0256F')
        ax.set_xlabel('Year', color="white")
        ax.set_ylabel('Total Rating Amount', color="white")
        ax.set_title('Total Ratings per Year', color="white")
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        # Set custom formatter for y-axis labels
        formatter = FuncFormatter(format_yaxis_shorten)
        ax.yaxis.set_major_formatter(formatter)

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

# Concrete strategy for Percentage of Ratings Based on Genre Pie Chart
class RatingsPercentagePerGenreChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Calculate the percentage of ratings for each genre
        ratings_per_genre = self.data.groupby('Genre')['Rating amount'].sum()
        ratings_percentage_per_genre = (ratings_per_genre / ratings_per_genre.sum()) * 100

        # Create the pie chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.pie(ratings_percentage_per_genre, labels=ratings_percentage_per_genre.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors, textprops={'color':"white"})
        ax.set_title('Ratings Percentage per Genre (%)', color="white")

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

# Concrete strategy for Percentage of Ratings in a Year Pie Chart
class RatingsPercentagePerYearChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Calculate the percentage of ratings for each year
        ratings_per_year = self.data.groupby('Year')['Rating amount'].sum()
        ratings_percentage_per_year = (ratings_per_year / ratings_per_year.sum()) * 100

        # Create the pie chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.pie(ratings_percentage_per_year, labels=ratings_percentage_per_year.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors, textprops={'color':"white"})
        ax.set_title('Ratings Percentage per Year (%)', color="white")

        fig.patch.set_facecolor('#1b243a')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='#1b243a')
        canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

# Function to plot chart based on the selected strategy
def plot_chart(chart_type, frame, checkbox):
    if checkbox.get() == 0:
        for widget in frame.winfo_children():
            widget.destroy()
        return

    if chart_type == "avg_rating_per_year":
        strategy = AvgRatingPerYearChart(frame, data)
    elif chart_type == "avg_rating_per_genre":
        strategy = AvgRatingPerGenreChart(frame, data)
    elif chart_type == "genre_distribution":
        strategy = GenreDistributionChart(frame, data)
    elif chart_type == "genre_percentage_per_year":
        strategy = GenrePercentagePerYearChart(frame, data)
    elif chart_type == "total_ratings_per_year":
        strategy = TotalRatingsPerYearChart(frame, data)
    elif chart_type == "ratings_percentage_per_genre":
        strategy = RatingsPercentagePerGenreChart(frame, data)
    elif chart_type == "ratings_percentage_per_year":
        strategy = RatingsPercentagePerYearChart(frame, data)
    else:
        return

    strategy.plot()

