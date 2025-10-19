import streamlit as st
import requests
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Navigation Links
st.markdown("""
<div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 20px;">
    <h4>📖 เนื้อหาทั้งหมด:</h4>
    <p>
        <a href="/" target="_self">🏠 หน้าหลัก</a> | 
        <a href="/1_Basics_of_Investment" target="_self">📘 พื้นฐานการลงทุน</a> | 
        📊 <strong>วิเคราะห์ข้อมูลหุ้น</strong> | 
        <a href="/3_Forex_and_Risk" target="_self">💱 ค่าเงินและความเสี่ยง</a> | 
        <a href="/4_About_and_Tips" target="_self">💡 เคล็ดลับและแหล่งความรู้</a>
    </p>
</div>
""", unsafe_allow_html=True)

st.header("📊 วิเคราะห์ข้อมูลหุ้นจริง")
st.write("ลองดูกราฟราคาหุ้นแบบเรียลไทม์กันเถอะ!")

# เลือกแหล่งข้อมูล
data_source = st.radio("เลือกแหล่งข้อมูล:", ["Alpha Vantage (API)", "Yahoo Finance (yfinance)"], index=1)

symbol = st.text_input("กรอกรหัสหุ้น (เช่น AAPL, MSFT):", "AAPL")

if data_source == "Yahoo Finance (yfinance)" and symbol:
    try:
        # ใช้ yfinance ดึงข้อมูล
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if not hist.empty:
            st.subheader(f"📈 ข้อมูลหุ้น {symbol.upper()}")
            
            # สร้างกราฟด้วย Plotly
            fig = go.Figure()
            fig.add_trace(go.Candlestick(
                x=hist.index,
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'],
                name=symbol.upper()
            ))
            
            fig.update_layout(
                title=f"กราฟเทียน {symbol.upper()}",
                yaxis_title="ราคา (USD)",
                xaxis_title="วันที่",
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # แสดงข้อมูลสรุป
            col1, col2, col3, col4 = st.columns(4)
            latest = hist.iloc[-1]
            prev_close = hist.iloc[-2]['Close']
            change = latest['Close'] - prev_close
            change_pct = (change / prev_close) * 100
            
            with col1:
                st.metric("ราคาปิด", f"${latest['Close']:.2f}", f"{change:+.2f}")
            with col2:
                st.metric("เปลี่ยนแปลง %", f"{change_pct:+.2f}%")
            with col3:
                st.metric("สูงสุด", f"${latest['High']:.2f}")
            with col4:
                st.metric("ต่ำสุด", f"${latest['Low']:.2f}")
                
            # แสดงตารางข้อมูล 5 วันล่าสุด
            st.subheader("📊 ข้อมูล 5 วันล่าสุด")
            st.dataframe(hist.tail().round(2))
            
        else:
            st.error("❌ ไม่พบข้อมูลหุ้น กรุณาตรวจสอบรหัสหุ้น")
            
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")
        st.info("💡 ลองใช้ Alpha Vantage API แทน")

elif data_source == "Alpha Vantage (API)" and symbol:
    API_KEY = "81WH16M23KTGFE8G"
    
    try:
        # ดึงข้อมูลแบบ Daily Time Series จาก Alpha Vantage
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={API_KEY}"
        r = requests.get(url)
        data = r.json()
        
        if "Time Series (Daily)" in data:
            df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
            df = df.rename(columns={
                "1. open":"Open",
                "2. high":"High",
                "3. low":"Low",
                "4. close":"Close",
                "6. volume":"Volume"
            })
            df = df.astype(float)
            df.index = pd.to_datetime(df.index)
            df = df.sort_index()
            
            st.subheader(f"📈 ข้อมูลหุ้น {symbol.upper()} (Alpha Vantage)")
            
            # แสดงกราฟเส้น
            st.line_chart(df["Close"])
            
            # แสดงข้อมูลสรุปล่าสุด
            latest = df.iloc[-1]
            prev_close = df.iloc[-2]['Close'] if len(df) > 1 else latest['Close']
            change = latest['Close'] - prev_close
            change_pct = (change / prev_close) * 100 if prev_close != 0 else 0
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("ราคาปิด", f"${latest['Close']:.2f}", f"{change:+.2f}")
            with col2:
                st.metric("เปลี่ยนแปลง %", f"{change_pct:+.2f}%")
            with col3:
                st.metric("สูงสุด", f"${latest['High']:.2f}")
            with col4:
                st.metric("ต่ำสุด", f"${latest['Low']:.2f}")
            
            # แสดงตารางข้อมูล 5 วันล่าสุด
            st.subheader("📊 ข้อมูล 5 วันล่าสุด")
            st.dataframe(df.tail().round(2))
            
        else:
            st.error("❌ ไม่พบข้อมูล - ตรวจสอบรหัสหุ้น / API Key")
            if "Note" in data:
                st.warning("⚠️ API Rate limit - ลองใช้ Yahoo Finance แทน")
                
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาดใน Alpha Vantage: {str(e)}")
        st.info("💡 ลองใช้ Yahoo Finance แทน")

# Popular Stock Examples
st.markdown("### 📈 หุ้นยอดนิยม")
col1, col2, col3, col4 = st.columns(4)

popular_stocks = [
    ("AAPL", "Apple"),
    ("MSFT", "Microsoft"), 
    ("TSLA", "Tesla"),
    ("GOOGL", "Google")
]

for i, (ticker, name) in enumerate(popular_stocks):
    with [col1, col2, col3, col4][i]:
        if st.button(f"{ticker}\n{name}", use_container_width=True):
            st.rerun()

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← ก่อนหน้า: พื้นฐาน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")

with col3:
    if st.button("ถัดไป: ความเสี่ยง →", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
