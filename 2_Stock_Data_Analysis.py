import streamlit as st
import requests
import pandas as pd

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

API_KEY = "81WH16M23KTGFE8G"
symbol = st.text_input("กรอกรหัสหุ้น (เช่น AAPL, MSFT):", "AAPL")

if symbol:
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
        st.line_chart(df["Close"])
        st.write(df.head())
    else:
        st.error("ไม่พบข้อมูล - ตรวจสอบรหัสหุ้น / API Key")

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
