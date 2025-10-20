import streamlit as st
import requests
import pandas as pd
import sys
import os

# เพิ่ม path สำหรับ import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import ALPHA_VANTAGE_API_KEY, DEFAULT_STOCK_SYMBOLS, ALPHA_VANTAGE_BASE_URL
from css_loader import load_all_styles

try:
    import yfinance as yf
    import plotly.graph_objects as go
    from datetime import datetime, timedelta
    ADVANCED_FEATURES = True
except ImportError:
    ADVANCED_FEATURES = False
    st.warning("⚠️ ไลบรารี yfinance และ plotly ยังไม่ได้ติดตั้ง กรุณารันคำสั่ง: pip install yfinance plotly")

# Configuration
st.set_page_config(
    page_title="Stock Analysis - Global Stock Guide", 
    page_icon="📊", 
    layout="wide"
)

# Load external CSS
load_all_styles()

# Add FontAwesome CDN
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
""", unsafe_allow_html=True)

menu_icons = {
    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",
    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",
    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",
    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",
    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"
}

# Modern Menu Bar
st.markdown("""
<div class="menu-container">
    <div class="menu-nav">
        <div class="logo"><i class='fa-solid fa-earth-americas'></i> Global Stocks</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Menu
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("⌂ หน้าหลัก", use_container_width=True):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("◉ พื้นฐานการลงทุน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")
with col3:
    if st.button("� วิเคราะห์หุ้น", use_container_width=True, type="primary"):
        st.rerun()
with col4:
    if st.button("⚖ ความเสี่ยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True):
        st.switch_page("pages/4_About_and_Tips.py")

st.divider()

st.markdown("<h1><i class='fa-solid fa-chart-line'></i> วิเคราะห์ข้อมูลหุ้นจริง</h1>", unsafe_allow_html=True)
st.write("ลองดูกราฟราคาหุ้นแบบเรียลไทม์กันเถอะ!")

# เลือกแหล่งข้อมูล
if ADVANCED_FEATURES:
    data_source = st.radio("เลือกแหล่งข้อมูล:", ["Alpha Vantage (API)", "Yahoo Finance (yfinance)"], index=1)
else:
    data_source = "Alpha Vantage (API)"
    st.info("📌 ใช้ Alpha Vantage API (ไลบรารีพิเศษยังไม่ได้ติดตั้ง)")

symbol = st.text_input("กรอกรหัสหุ้น (เช่น AAPL, MSFT):", "AAPL")

# แสดงตัวเลือกหุ้นยอดนิยม
st.markdown("### <i class='fa-solid fa-chart-simple'></i> หุ้นยอดนิยม (คลิกเพื่อเลือก)", unsafe_allow_html=True)
cols = st.columns(4)
for i, stock in enumerate(DEFAULT_STOCK_SYMBOLS[:8]):
    with cols[i % 4]:
        if st.button(f"{stock}", key=f"stock_{stock}", use_container_width=True):
            # ใช้ st.rerun() เพื่อรีเฟรชแอปและเปลี่ยน symbol
            st.session_state.selected_symbol = stock
            st.rerun()

# ตรวจสอบว่ามีการเลือกหุ้นจาก button หรือไม่
if 'selected_symbol' in st.session_state:
    symbol = st.session_state.selected_symbol

if data_source == "Yahoo Finance (yfinance)" and symbol and ADVANCED_FEATURES:
    try:
        # ใช้ yfinance ดึงข้อมูล
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1y")
        
        if not hist.empty:
            st.markdown(f"<h2><i class='fa-solid fa-chart-area'></i> ข้อมูลหุ้น {symbol.upper()}</h2>", unsafe_allow_html=True)
            
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
            st.markdown("<h3><i class='fa-solid fa-table'></i> ข้อมูล 5 วันล่าสุด</h3>", unsafe_allow_html=True)
            st.dataframe(hist.tail().round(2))
            
        else:
            st.error("❌ ไม่พบข้อมูลหุ้น กรุณาตรวจสอบรหัสหุ้น")
            
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")
        st.info("💡 ลองใช้ Alpha Vantage API แทน")

elif (data_source == "Alpha Vantage (API)" and symbol) or (not ADVANCED_FEATURES and symbol):
    
    try:
        # ดึงข้อมูลแบบ Daily Time Series จาก Alpha Vantage
        url = f"{ALPHA_VANTAGE_BASE_URL}?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={ALPHA_VANTAGE_API_KEY}"
        
        with st.spinner(f"กำลังดึงข้อมูลหุ้น {symbol.upper()}..."):
            r = requests.get(url)
            data = r.json()
        
        if "Time Series (Daily)" in data:
            df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
            df = df.rename(columns={
                "1. open":"Open",
                "2. high":"High",  
                "3. low":"Low",
                "4. close":"Close",
                "5. adjusted_close":"Adj_Close",
                "6. volume":"Volume"
            })
            df = df.astype(float)
            df.index = pd.to_datetime(df.index)
            df = df.sort_index()
            
            st.markdown(f"<h2><i class='fa-solid fa-chart-area'></i> ข้อมูลหุ้น {symbol.upper()} - Alpha Vantage</h2>", unsafe_allow_html=True)
            
            # แสดงข้อมูลบริษัท (ถ้ามี)
            if "Meta Data" in data:
                meta = data["Meta Data"]
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**รหัสหุ้น:** {meta.get('2. Symbol', symbol)}")
                with col2:
                    st.info(f"**อัพเดตล่าสุด:** {meta.get('3. Last Refreshed', 'N/A')}")
            
            # แสดงกราฟเส้น
            st.line_chart(data=df[["Close"]], height=400)
            
            # แสดงข้อมูลสรุปล่าสุด
            latest = df.iloc[-1]
            prev_close = df.iloc[-2]['Close'] if len(df) > 1 else latest['Close']
            change = latest['Close'] - prev_close
            change_pct = (change / prev_close) * 100 if prev_close != 0 else 0
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("💰 ราคาปิด", f"${latest['Close']:.2f}", f"{change:+.2f}")
            with col2:
                st.metric("📊 เปลี่ยนแปลง %", f"{change_pct:+.2f}%")
            with col3:
                st.metric("⬆️ สูงสุดวัน", f"${latest['High']:.2f}")
            with col4:
                st.metric("⬇️ ต่ำสุดวัน", f"${latest['Low']:.2f}")
            
            # แสดงข้อมูลเพิ่มเติม
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📈 ราคาเปิด", f"${latest['Open']:.2f}")
            with col2:
                st.metric("🔄 ปริมาณซื้อขาย", f"{latest['Volume']:,.0f}")
            with col3:
                st.metric("🎯 ราคาปรับปรุง", f"${latest['Adj_Close']:.2f}")
            
            # แสดงตารางข้อมูล 10 วันล่าสุด
            st.markdown("<h3><i class='fa-solid fa-table'></i> ข้อมูล 10 วันล่าสุด</h3>", unsafe_allow_html=True)
            display_df = df.tail(10).copy()
            display_df.index = display_df.index.strftime('%Y-%m-%d')
            st.dataframe(display_df.round(2), use_container_width=True)
            
        else:
            st.error("❌ ไม่พบข้อมูล - ตรวจสอบรหัสหุ้น")
            if "Note" in data:
                st.warning("⚠️ API Rate limit - ลองใช้หุ้นอื่นหรือรอสักครู่")
            elif "Error Message" in data:
                st.warning(f"⚠️ {data['Error Message']}")
            st.info("💡 ลองเปลี่ยนเป็น Yahoo Finance หรือลองหุ้นยอดนิยมด้านบน")
                
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาดใน Alpha Vantage: {str(e)}")
        st.info("💡 ลองใช้ Yahoo Finance แทน")

# แสดงข้อมูลเพิ่มเติมเกี่ยวกับ API
st.markdown("---")
with st.expander("ℹ️ ข้อมูลเกี่ยวกับแหล่งข้อมูล"):
    st.markdown("""
    **Alpha Vantage API:**
    - <i class='fa-solid fa-check'></i> ข้อมูลแม่นยำและเชื่อถือได้
    - <i class='fa-solid fa-triangle-exclamation'></i> จำกัด 5 requests ต่อนาที และ 500 requests ต่อวัน (ฟรี)
    - <i class='fa-solid fa-chart-line'></i> ข้อมูลหุ้นจากตลาดหลักทรัพย์สหรัฐฯ
    
    **Yahoo Finance (yfinance):**
    - <i class='fa-solid fa-check'></i> ไม่จำกัดการใช้งาน
    - <i class='fa-solid fa-check'></i> กราฟแบบ Interactive
    - <i class='fa-solid fa-triangle-exclamation'></i> ต้องติดตั้งไลบรารีเพิ่มเติม: `pip install yfinance plotly`
    """, unsafe_allow_html=True)

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← ก่อนหน้า: พื้นฐาน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")

with col3:
    if st.button("ถัดไป: ความเสี่ยง →", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
