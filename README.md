# Investment News Analyzer

## Overview
The Investment News Analyzer is a Streamlit-based web application that fetches the latest financial news for a user's stock portfolio, analyzes the sentiment of the news, and maps the impact of the news on the user's stocks.

## Features
- **Real-time News Fetching:** Fetches the latest financial news for the user's stock tickers using the NewsAPI.
- **Sentiment Analysis:** Analyzes the sentiment (positive, negative, or neutral) of each news item.
- **Portfolio Impact Mapping:** Maps each news article to the affected stocks in the user's portfolio.
- **User-friendly UI:** Built with Streamlit for a clean and intuitive user experience.

  
## Technologies Used
- **Streamlit:** For building the web application and user interface.
- **CrewAI:** For orchestrating the multi-agent system to fetch and analyze news.
- **NewsAPI:** For fetching real-time financial news data.
- **Python:** The primary programming language used for the project.
- **Pydantic:** For data validation and settings management.
- **Requests:** For making HTTP requests to the NewsAPI.
- **Dotenv:** For managing environment variables.

  
## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/investment-news-analyzer.git
   cd investment-news-analyzer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the root directory and add your NewsAPI key and OpenAI API key:**
   ```
   NEWS_API_KEY=your_news_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   **Note:** The application requires an OpenAI API key to function, as CrewAI relies on it for the agents to work.


4. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage
1. Open the application in your web browser.
2. Enter your stock tickers (comma-separated, e.g., AAPL, TSLA, GOOG) in the input field.
3. Click the "Analyze News" button to fetch and analyze the latest news for your portfolio.
4. View the news impact summary displayed on the screen.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
