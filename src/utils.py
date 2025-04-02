import os

def save_to_csv(data, filename):
    """
    Save DataFrame to a CSV file.
    :param data: Pandas DataFrame
    :param filename: File path for saving
    """
    if data is not None:
        os.makedirs("data", exist_ok=True)
        data.to_csv(f"data/{filename}.csv")
        print(f"Data saved to data/{filename}.csv")
    else:
        print("No data to save.")
