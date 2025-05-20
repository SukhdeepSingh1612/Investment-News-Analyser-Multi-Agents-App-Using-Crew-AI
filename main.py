from crew import crew

if __name__ == "__main__":
    print("Running Investment News Analyzer...")
    result = crew.kickoff()
    print("\n📰 Final Analysis:\n")
    print(result)
