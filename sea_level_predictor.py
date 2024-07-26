import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    DATA_FILENAME = "epa-sea-level.csv"
    df = pd.read_csv(f"{DATA_FILENAME}", sep=",", skipinitialspace=True)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.ylim(0, 16)
    plt.xlim(1850,2075)
    
    # Create first line of best fit
    years_list = np.arange(1880, 2051)
    
    lr1 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.plot(years_list, lr1.intercept + lr1.slope * years_list, "r")

    # Create second line of best fit
    years_list = np.arange(2000, 2051)
    lr2 = linregress(x=df["Year"][df["Year"] >= 2000], y=df["CSIRO Adjusted Sea Level"][df["Year"] >= 2000])
    plt.plot(years_list, lr2.intercept + lr2.slope * years_list, "g")


    # Add labels and title
    ticks_list_label = [1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075]
    ticks_list_int = [int(s) for s in ticks_list_label]
    
    plt.title("Rise in Sea Level", fontsize=14)
    plt.xlabel("Year", fontsize=11)
    plt.ylabel("Sea Level (inches)", fontsize=11)
    plt.xticks(fontsize=11, ticks=ticks_list_int, labels=ticks_list_label)
    plt.yticks(fontsize=11)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
