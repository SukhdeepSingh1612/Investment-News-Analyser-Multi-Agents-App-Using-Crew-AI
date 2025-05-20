import streamlit as st
from crew import crew

st.set_page_config(page_title="Investment News Analyzer", layout="wide")

st.title("📈 Investment News Analyzer")
st.markdown("Analyze the latest financial news and its impact on your stock portfolio.")

portfolio_input = st.text_input(
    "Enter your stock tickers (comma separated, e.g., AAPL, TSLA, GOOG):", "AAPL, TSLA"
)

if st.button("Analyze News"):
    st.info("Fetching news and analyzing...")
    with st.spinner("Thinking..."):
        thought_process = st.empty()
        thought_process.markdown("🤔 Analyzing your portfolio...")
        result = crew.kickoff(inputs={"portfolio": portfolio_input})
        thought_process.markdown("✅ Analysis complete!")
    st.success("Analysis Complete!")
    st.markdown("### 📰 News Impact Summary")
    st.markdown(result.raw)
