# from crewai import Task
# from tools import yt_tool
# from agents import blog_researcher, blog_writer



# ## Research Task
# research_task = Task(
#     description=(
#         "Identify the video {topic}. "
#         "Get detailed information about the video from the channel."
#     ),
#     expected_output="A comprehensive 3 paragraph long report based on the {topic} of the video content",
#     agent=blog_researcher,
#     tools=[yt_tool]
# )

# ## Writing Task
# writing_task = Task(
#     description=(
#         "get the infor from the youtube channel on the {topic}." \
#     ),
#     expected_output= "A well-structured blog post with an introduction, body, and conclusion with the summarirized info on the topic {topic} from the youtube channel.",
#     agent=blog_writer,
#     tools=[yt_tool],
#     async_execution = False,
#     output_file = 'new-blog-post.md'
# )


from crewai import Task
from agents import NewsFetcherAgent, SentimentAnalyzerAgent, PortfolioMapperAgent
from news_tools import fetch_news_tool

NewsFetchTask = Task(
    agent=NewsFetcherAgent,
    description="Fetch the latest financial news for the user's portfolio.",
    tools=[fetch_news_tool],
    expected_output="A list of news articles with summaries.",
)

SentimentTask = Task(
    agent=SentimentAnalyzerAgent,
    description="Analyze the tone (positive, negative, or neutral) of each news item.",
    expected_output="A list of news items with their sentiment (positive, negative, or neutral).",
)

ImpactTask = Task(
    agent=PortfolioMapperAgent,
    description="Map each news article to stocks in the user's portfolio.",
    expected_output="A mapping of news articles to affected stocks in the user's portfolio.",
)
