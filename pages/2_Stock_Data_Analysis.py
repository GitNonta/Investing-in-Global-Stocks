import streamlit as st
import requests
import pandas as pd
import sys
import os

# เพิ่ม path สำหรับ import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import ALPHA_VANTAGE_API_KEY, DEFAULT_STOCK_SYMBOLS, ALPHA_VANTAGE_BASE_URL

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

# Icons for menu items
menu_icons = {
    "home": "<img src='https://cdn-icons-png.flaticon.com/512/1946/1946436.png' width='20' style='vertical-align:middle;margin-right:6px;'>",
    "basics": "<img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='20' style='vertical-align:middle;margin-right:6px;'>",
    "analysis": "<img src='https://cdn-icons-png.flaticon.com/512/2721/2721297.png' width='20' style='vertical-align:middle;margin-right:6px;'>",
    "forex": "<img src='https://cdn-icons-png.flaticon.com/512/3135/3135706.png' width='20' style='vertical-align:middle;margin-right:6px;'>",
    "tips": "<img src='https://cdn-icons-png.flaticon.com/512/1828/1828884.png' width='20' style='vertical-align:middle;margin-right:6px;'>"
}

# Modern Menu Bar
st.markdown(f"""
<style>
.menu-container {{background: linear-gradient(90deg, #2C3E50 0%, #3498DB 50%, #9B59B6 100%);padding: 0.8rem 0;margin: -1rem -1rem 2rem -1rem;box-shadow: 0 2px 10px rgba(0,0,0,0.1);position: sticky;top: 0;z-index: 999;}}
.menu-nav {{max-width: 1200px;margin: 0 auto;display: flex;justify-content: space-between;align-items: center;padding: 0 2rem;}}
.logo {{font-size: 1.5rem;font-weight: bold;color: white;text-decoration: none;}}
.menu-items {{display: flex;gap: 2rem;align-items: center;}}
.menu-item {{color: white;text-decoration: none;padding: 0.5rem 1rem;border-radius: 20px;transition: all 0.3s ease;font-weight: 500;font-size: 0.95rem;display: flex;align-items: center;}}
.menu-item:hover {{background: rgba(255,255,255,0.2);color: white;transform: translateY(-2px);text-decoration: none;}}
.menu-item.active {{background: rgba(255,255,255,0.3);color: white;}}
.menu-icon {{margin-right: 0.5rem;}}
@media (max-width: 768px) {{.menu-nav {{flex-direction: column;padding: 1rem;}}.menu-items {{margin-top: 1rem;flex-wrap: wrap;gap: 1rem;}}}}
</style>

<div class="menu-container">
    <div class="menu-nav">
        <div class="logo">🌍 Global Stocks</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Menu
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 หน้าหลัก", use_container_width=True):
        st.switch_page("streamlit_app.py")
with col2:
    if st.button("📘 พื้นฐานการลงทุน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")
with col3:
    if st.button("📊 วิเคราะห์หุ้น", use_container_width=True, type="primary"):
        st.rerun()
with col4:
    if st.button("💱 ความเสี่ยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True):
        st.switch_page("pages/4_About_and_Tips.py")

st.divider()

st.header("📊 วิเคราะห์ข้อมูลหุ้นจริง")
st.write("ลองดูกราฟราคาหุ้นแบบเรียลไทม์กันเถอะ!")

# เลือกแหล่งข้อมูล
if ADVANCED_FEATURES:
    data_source = st.radio("เลือกแหล่งข้อมูล:", ["Alpha Vantage (API)", "Yahoo Finance (yfinance)"], index=1)
else:
    data_source = "Alpha Vantage (API)"
    st.info("📌 ใช้ Alpha Vantage API (ไลบรารีพิเศษยังไม่ได้ติดตั้ง)")

symbol = st.text_input("กรอกรหัสหุ้น (เช่น AAPL, MSFT):", "AAPL")

# แสดงตัวเลือกหุ้นยอดนิยม
st.markdown("### 📈 หุ้นยอดนิยม (คลิกเพื่อเลือก)")
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
            
            st.subheader(f"📈 ข้อมูลหุ้น {symbol.upper()} - Alpha Vantage")
            
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
            st.subheader("📊 ข้อมูล 10 วันล่าสุด")
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
    - ✅ ข้อมูลแม่นยำและเชื่อถือได้
    - ⚠️ จำกัด 5 requests ต่อนาที และ 500 requests ต่อวัน (ฟรี)
    - 📊 ข้อมูลหุ้นจากตลาดหลักทรัพย์สหรัฐฯ
    
    **Yahoo Finance (yfinance):**
    - ✅ ไม่จำกัดการใช้งาน
    - ✅ กราฟแบบ Interactive
    - ⚠️ ต้องติดตั้งไลบรารีเพิ่มเติม: `pip install yfinance plotly`
    """)

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← ก่อนหน้า: พื้นฐาน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")

with col3:
    if st.button("ถัดไป: ความเสี่ยง →", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
