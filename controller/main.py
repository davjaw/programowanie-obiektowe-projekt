import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk  # Import tkinter

# Define a global variable to hold the canvas
canvas = None

def plot_chart(frame, checkbox):
    global canvas

    # Clear previous content in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    if checkbox.get()==0:
        return  # If checkbox is unchecked, don't plot anything

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

    # Sum the rating amounts by year
    ratings_per_year = data.groupby('Year')['Rating amount'].sum().reset_index()

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
    canvas = FigureCanvasTkAgg(fig, master=frame)

    # Embed the plot into the Tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().configure(background='#1b243a')
    canvas.get_tk_widget().pack(side="left", fill=tk.BOTH, expand=1)

    # Adjust checkbox command to plot or hide the chart
    checkbox.configure(command=lambda: plot_chart(frame, checkbox))
