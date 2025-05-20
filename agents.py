# from crewai import Agent
# from crewai import OpenAI


# from tools import yt_tool
# import os
# from dotenv import load_dotenv
# load_dotenv()




# api = os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"


# llm = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     model="gpt-4-0125-preview"
# )

# #llm  =  OpenAI(api_key=api, model="gpt-4-0125-preview")

# ### Create a senior blog content researcher


# blog_researcher = Agent(
#     role="senior blog researcher from Youtube Videos",
#     goal = "get the relevant video content fot the topic {topic} from Youtube channel",
#     verbose= True,
#     memory = True,
#     backstory = (
#         "Expert in understanding the videos in AI Data Science, Machine Learning and Gen AI and extracting relevant information. "
#     ),
#     tools = [
#         yt_tool
#     ],
#     allow_delegation = True
#     )


# ### Create a senior blog content writer agent with YT tool

# blog_writer = Agent(
#     role="senior blog writer",
#     goal = "Narrate compelling tech stories about the video {topic} from Youtube channel",
#     verbose= True,
#     memory = True,
#     backstory = (
#         "With a flair for simplifying complex topics, you craft engaging narratives that resonate with readers." \
#         "bringing new discoveries to light in an accessible manner."
#     ),
#     tools = [ 
#         yt_tool
#     ],
#     allow_delegation = False
#     )

from crewai import Agent

NewsFetcherAgent = Agent(
    role="News Fetcher",
    goal="Collect latest financial news headlines for the user's portfolio: {portfolio}",
    backstory="You scan multiple news sources to fetch the latest financial articles for the user's stock tickers.",
)

SentimentAnalyzerAgent = Agent(
    role="Sentiment Analyzer",
    goal="Analyze if news is positive, negative or neutral for a company in the user's portfolio: {portfolio}",
    backstory="You understand financial language and classify news accordingly for the user's stocks.",
)

PortfolioMapperAgent = Agent(
    role="Portfolio Impact Evaluator",
    goal="Check if any of the news affects the user's portfolio: {portfolio}",
    backstory="You know the user's stock holdings and can match news relevance to the user's portfolio.",
)
