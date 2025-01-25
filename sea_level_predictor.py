import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"],
        color="blue",
        alpha=0.6,
        label="Data",
    )

    # Create first line of best fit
    line_1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = range(1880, 2051)
    y = line_1.slope * x + line_1.intercept
    plt.plot(x, y, "r", label="Best Fit Line 1")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    line_2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_2000 = range(2000, 2051)
    y_2000 = line_2.slope * x_2000 + line_2.intercept
    plt.plot(x_2000, y_2000, "g", label="Best Fit Line 2")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
