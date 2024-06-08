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

# Base class for charts
class ChartStrategy:
    def __init__(self, frame, data):
        self.frame = frame
        self.data = data

    def plot(self):
        pass

# Concrete strategy for Total Ratings per Year Chart
class TotalRatingsPerYearChart(ChartStrategy):
    def plot(self):
        # Clear previous content in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Sum the rating amounts by year
        ratings_per_year = self.data.groupby('Year')['Rating amount'].sum().reset_index()

        # Create the column chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_facecolor("#1b243a")
        ax.bar(ratings_per_year['Year'], ratings_per_year['Rating amount'], color='#C0256F')
        ax.set_xlabel('Year', color="white")
        ax.set_ylabel('Total Rating Amount', color="white")
        ax.set_title('Total Ratings per Year', color="white")
        ax.set_xticklabels(ratings_per_year['Year'], rotation=45, color="white")
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        # Format the y-axis to show numbers in a compact format
        def format_yaxis(x, pos):
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

        formatter = FuncFormatter(format_yaxis)
        ax.yaxis.set_major_formatter(formatter)
        ax.grid(axis='y')

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

# Context class to use the strategy
class ChartContext:
    def __init__(self, strategy, frame, data):
        self.strategy = strategy
        self.frame = frame
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def plot(self):
        self.strategy.plot()

# Function to plot chart based on the selected strategy
def plot_chart(chart_type, frame, checkbox):
    if checkbox.get() == 0:
        for widget in frame.winfo_children():
            widget.destroy()
        return

    if chart_type == "total_ratings_per_year":
        strategy = TotalRatingsPerYearChart
    elif chart_type == "avg_rating_per_genre":
        strategy = AvgRatingPerGenreChart
    elif chart_type == "genre_distribution":
        strategy = GenreDistributionChart
    else:
        return

    chart_context = ChartContext(strategy(frame, data), frame, data)
    chart_context.plot()
