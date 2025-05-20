# from crewai_tools import YoutubeChannelSearchTool

# ## initialize the tool with a specific Youtube channel handle to target the search
# yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="@krishnaik06")


import requests
import os
from dotenv import load_dotenv
from crewai.tools import BaseTool

load_dotenv()

def fetch_news_for_stocks(query: str = "AAPL,TSLA"):
    api_key = os.getenv("NEWS_API_KEY")
    combined_query = " OR ".join([q.strip() for q in query.split(",")])
    url = f"https://newsapi.org/v2/everything?q={combined_query}&sortBy=publishedAt&pageSize=5&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()
    print("API Response:", data)  # Debug print
    results = []

    for article in data.get('articles', []):
        results.append(f"Title: {article['title']}\nSummary: {article['description']}\n")

    return "\n".join(results) if results else "No articles found."

class FetchNewsTool(BaseTool):
    name: str = "fetch_news_for_stocks"
    description: str = "Fetches news for given stock tickers using NewsAPI"

    def _run(self, query="AAPL,TSLA"):
        return fetch_news_for_stocks(query)

fetch_news_tool = FetchNewsTool()
tools = [fetch_news_tool]

# Now pass `tools` to crew task/agent creation

