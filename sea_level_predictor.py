# sea_level_predictor.py
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Observed Data')

    # Create a linear regression model for all data
    slope_all, intercept_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    years_extended = pd.Series(range(1880, 2051))  # Extend to 2050
    sea_level_pred_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, sea_level_pred_all, color='red', label='Best Fit Line (All Data)')

    # Create a linear regression model for data from year 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])[:2]
    sea_level_pred_recent = slope_recent * years_extended + intercept_recent
    plt.plot(years_extended, sea_level_pred_recent, color='green', label='Best Fit Line (2000+)')

    # Set labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

# Data Source: Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

