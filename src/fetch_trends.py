import pandas as pd
from pytrends.request import TrendReq
import time
import random

def fetch_trend_data(keyword, timeframe='today 12-m'):
    """
    Fetch Google Trends data for a given keyword.
    :param keyword: The search keyword
    :param timeframe: The timeframe for search interest data
    :return: Pandas DataFrame with trend data
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Introducing a random delay between requests to avoid hitting rate limits
    time.sleep(random.randint(10, 20))  # Random sleep time between 10 and 20 seconds
    pytrends.build_payload([keyword], cat=0, timeframe=timeframe)
    
    try:
        # Adding retry mechanism in case of rate-limiting
        data = pytrends.interest_over_time()
        if data.empty:
            print(f"No data found for {keyword}")
            return None
        return data
    except pytrends.exceptions.TooManyRequestsError:
        # Handle rate-limiting by waiting and retrying
        print(f"Rate limit hit for {keyword}. Retrying...")
        time.sleep(random.randint(30, 60))  # Sleep for 30-60 seconds before retrying
        return fetch_trend_data(keyword, timeframe)
    except KeyError:
        print(f"No data available for {keyword}")
        return None
