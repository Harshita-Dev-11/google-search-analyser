from src.fetch_trends import fetch_trend_data
from src.visualize import plot_trends
from src.utils import save_to_csv

if __name__ == "__main__":
    keyword = "Cloud Computing"  # Change this to any keyword
    data = fetch_trend_data(keyword)

    if data is not None:
        save_to_csv(data, keyword.replace(" ", "_") + "_trends")
        plot_trends(data, keyword)
