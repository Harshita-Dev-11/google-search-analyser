import matplotlib.pyplot as plt
import pandas as pd

def plot_trends(data, keyword):
    """
    Plot the search interest trend over time for a given keyword.
    :param data: Pandas DataFrame containing search trend data
    :param keyword: The search keyword
    """
    if data is not None and keyword in data.columns:
        data[keyword].plot(figsize=(10, 5), kind="line", title=f"Google Search Trend for '{keyword}'", color='b')
        plt.xlabel("Date")
        plt.ylabel("Search Interest")
        plt.grid()
        plt.show()
    else:
        print("No data available for visualization.")
