import pytest
from src.fetch_trends import fetch_trend_data

def test_fetch_trend_data():
    keyword = "Cloud Computing"
    data = fetch_trend_data(keyword)
    assert data is not None, "Data should not be None"
    assert keyword in data.columns, "Keyword column should exist"
