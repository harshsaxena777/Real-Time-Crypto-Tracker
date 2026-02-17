import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="QuantPulse", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 24px; color: #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 QuantPulse: Real-Time Crypto Intelligence")

# Header Metrics
col1, col2, col3, col4 = st.columns(4)
btc = yf.Ticker("BTC-USD").fast_info['last_price']
eth = yf.Ticker("ETH-USD").fast_info['last_price']

col1.metric("BTC/USD", f"${btc:,.2f}", "1.2%")
col2.metric("ETH/USD", f"${eth:,.2f}", "-0.5%")
col3.metric("Market Volatility", "Medium", "Stable")
col4.metric("AI Sentiment", "Bullish", "High")

# Technical Charting
symbol = st.text_input("Enter Asset Symbol (e.g. BTC-USD, TSLA, AAPL)", "BTC-USD")
df = yf.download(symbol, period="1mo", interval="1d")

fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])])

fig.update_layout(template="plotly_dark", title=f"{symbol} Technical View", xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)