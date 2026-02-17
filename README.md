# Real-Time-Crypto-Tracker

It is a high-performance financial monitoring dashboard built to provide real-time technical analysis for cryptocurrencies and global equities. By leveraging the Yahoo Finance API and Plotly's hardware-accelerated graphing library, it offers a "Bloomberg-lite" experience directly in the browser.

🚀 Key Features
Real-Time Data Ingestion: Uses the yfinance library to fetch live market prices with sub-second latency.

Interactive Candlestick Analytics: Implements high-fidelity OHLC (Open, High, Low, Close) charts for technical pattern recognition.

Multi-Asset Support: Seamlessly switch between Cryptocurrencies (e.g., BTC-USD), Stocks (e.g., TSLA), and Forex.

Custom UI Engine: Injects custom CSS into the Streamlit frontend to achieve a professional "Dark Mode" SaaS aesthetic.

Dynamic Volatility Tracking: Monitors real-time price fluctuations to provide instant market sentiment.

🏗️ System Architecture
The application follows a modular "Data-to-Insight" pipeline:

Request Layer: Captures user input (tickers) and formats API requests.

Ingestion Layer: Asynchronously fetches market data from Yahoo Finance servers.

Processing Layer: Cleans and structures raw JSON data into a Pandas DataFrame.

Visualization Layer: Renders the structured data into interactive Plotly objects.

Frontend: Serves the final dashboard via an optimized Streamlit server.


🛠️ Tech Stack
Language: Python 3.10+

Dashboarding: Streamlit (with Custom CSS Injection)

Financial Data: yFinance API

Visualization: Plotly (Candlestick & Indicator modules)

Data Manipulation: Pandas & NumPy
