
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_live_data():
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        raise ValueError("NEWS_API_KEY is missing from your .env file.")

    url = "https://newsapi.org/v2/top-headlines"

    headers = {
        "X-Api-Key": api_key
    }

    params = {
        "country": "us",
        "pageSize": 5
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=15
    )

    response.raise_for_status()
    result = response.json()

    data = {
        "status": result.get("status", "unknown"),
        "total_results": result.get("totalResults", 0)
    }

    for number, article in enumerate(result.get("articles", []), start=1):
        data[f"headline_{number}"] = article.get("title", "No title")
        data[f"source_{number}"] = article.get("source", {}).get("name", "Unknown")

    return data
