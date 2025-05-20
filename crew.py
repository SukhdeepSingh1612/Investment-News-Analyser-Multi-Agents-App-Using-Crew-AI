# from crewai import Crew,Process
# from tools import yt_tool
# from agents import blog_researcher, blog_writer
# from tasks import research_task, writing_task

# ## Forming the tech-focused crew with some enhanced configurations
# crew = Crew(
#     agents=[blog_researcher, blog_writer],
#     tasks=[research_task, writing_task],
#     process=Process.sequential,
#     cache = True,
#     max_rpm = 100,
#     share_crew = True,
#     memory=True,
    
# )


# ## Start the task execution process with enhanced feedback

# result = crew.kickoff(inputs={"topic" : "AI VS ML VS DL vs Data Science"})
# print(result)

from crewai import Crew, Process
from agents import NewsFetcherAgent, SentimentAnalyzerAgent, PortfolioMapperAgent
from tasks import NewsFetchTask, SentimentTask, ImpactTask

crew = Crew(
    agents=[NewsFetcherAgent, SentimentAnalyzerAgent, PortfolioMapperAgent],
    tasks=[NewsFetchTask, SentimentTask, ImpactTask],
    process=Process.sequential,
    verbose=True
)
