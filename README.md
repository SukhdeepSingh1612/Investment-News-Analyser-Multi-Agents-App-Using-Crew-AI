# Investment News Analyzer

## Overview
The Investment News Analyzer is a Streamlit-based web application that fetches the latest financial news for a user's stock portfolio, analyzes the sentiment of the news, and maps the impact of the news on the user's stocks.

## Features
- **Real-time News Fetching:** Fetches the latest financial news for the user's stock tickers using the NewsAPI.
- **Sentiment Analysis:** Analyzes the sentiment (positive, negative, or neutral) of each news item.
- **Portfolio Impact Mapping:** Maps each news article to the affected stocks in the user's portfolio.
- **User-friendly UI:** Built with Streamlit for a clean and intuitive user experience.

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

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your NewsAPI key:
   ```
   NEWS_API_KEY=your_news_api_key_here
   ```

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