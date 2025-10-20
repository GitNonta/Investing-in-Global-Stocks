import streamlit as st
import datetime
import requests
import sys
import os

# เพิ่ม path สำหรับ import config
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_BASE_URL

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False

# Add FontAwesome CDN (ต้องอยู่ก่อนเมนูบาร์เสมอ)
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
""", unsafe_allow_html=True)

# Configuration
st.set_page_config(
    page_title="Global Stock Investment Guide", 
    page_icon="<i class='fa-solid fa-globe'></i>", 
    layout="wide",
    initial_sidebar_state="expanded"
)

menu_icons = {
    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",
    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",
    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",
    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",
    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"
}

# Modern Menu Bar
st.markdown(f"""
<style>
.menu-container {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(44,62,80,0.92);
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 24px 0 rgba(44,62,80,0.12);
    padding: 0.7rem 0;
    margin: 0 0 1.5rem 0;
    transition: background 0.3s;
}}
.menu-nav {{
    max-width: 1100px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 1.5rem;
}}
.logo {{
    font-size: 1.3rem;
    font-weight: bold;
    color: #fff;
    text-decoration: none;
    display: flex;
    align-items: center;
    letter-spacing: 1px;
    transition: transform 0.2s;
}}
.logo:hover {{
    transform: scale(1.07) rotate(-2deg);
    color: #ffd700;
}}
.menu-items {{
    display: flex;
    gap: 1.2rem;
    align-items: center;
    transition: gap 0.2s;
}}
.menu-item {{
    color: #fff;
    text-decoration: none;
    padding: 0.35rem 1.1rem;
    border-radius: 18px;
    font-weight: 500;
    font-size: 1.05rem;
    display: flex;
    align-items: center;
    position: relative;
    transition: background 0.18s, color 0.18s, transform 0.18s;
    overflow: hidden;
}}
.menu-item .fa-solid {{
    transition: transform 0.25s cubic-bezier(.68,-0.55,.27,1.55), color 0.18s;
}}
.menu-item:hover .fa-solid {{
    transform: scale(1.18) rotate(-10deg);
    color: #ffd700;
}}
.menu-item:hover {{
    background: #3b4a5a;
    color: #ffd700;
    transform: translateY(-2px) scale(1.04);
    box-shadow: 0 2px 8px 0 rgba(44,62,80,0.10);
}}
.menu-item.active {{
    background: linear-gradient(90deg, #667eea 60%, #764ba2 100%);
    color: #fff;
    box-shadow: 0 2px 12px 0 rgba(102,126,234,0.10);
    font-weight: 700;
}}
.menu-item.active .fa-solid {{
    color: #ffd700;
}}
.menu-icon {{
    margin-right: 0.5rem;
    font-size: 1.1em;
}}
/* Hamburger for mobile (checkbox hack) */
#menu-toggle {{
    display: none;
}}
.menu-hamburger {{
    display: none;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 36px;
    height: 36px;
    cursor: pointer;
    margin-left: 1rem;
    z-index: 101;
}}
.menu-hamburger span {{
    width: 24px;
    height: 3px;
    background: #fff;
    margin: 3px 0;
    border-radius: 2px;
    transition: all 0.3s;
}}
@media (max-width: 900px) {{
    .menu-nav {{
        flex-direction: column;
        padding: 1rem;
    }}
    .menu-items {{
        margin-top: 1rem;
        flex-direction: column;
        width: 100%;
        gap: 0.7rem;
        display: none;
    }}
    #menu-toggle:checked + .menu-hamburger + .menu-items {{
        display: flex;
    }}
    .menu-hamburger {{
        display: flex;
    }}
    .logo {{
        font-size: 1.1rem;
    }}
}}
</style>

<div class="menu-container">
    <div class="menu-nav">
        <div class="logo"><i class='fa-solid fa-globe'></i>&nbsp;Global Stocks</div>
        <input type="checkbox" id="menu-toggle" style="display:none;" />
        <label class="menu-hamburger" for="menu-toggle">
            <span></span>
            <span></span>
            <span></span>
        </label>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Menu using Streamlit
st.markdown("### 📚 เนื้อหาทั้งหมด")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 หน้าหลัก", use_container_width=True, type="primary"):
        st.rerun()

with col2:
    if st.button("📘 พื้นฐานการลงทุน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")

with col3:
    if st.button("📊 วิเคราะห์หุ้น", use_container_width=True):
        st.switch_page("pages/2_Stock_Data_Analysis.py")

with col4:
    if st.button("💱 ความเสี่ยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")

with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True):
        st.switch_page("pages/4_About_and_Tips.py")

st.divider()

# Hero Section with modern styling
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; 
            border-radius: 15px; 
            margin-bottom: 2rem; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <h1 style="color: white; text-align: center; margin: 0; font-size: 3rem;">
        <i class='fa-solid fa-globe'></i> Global Stock Investment Guide
    </h1>
    <p style="color: white; text-align: center; font-size: 1.2rem; margin-top: 1rem; opacity: 0.9;">
        เรียนรู้และวิเคราะห์การลงทุนในหุ้นต่างประเทศอย่างครบถ้วน
    </p>
</div>
""", unsafe_allow_html=True)

# Market Overview with images
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=400&h=300&fit=crop", 
             caption="Financial Analysis", use_container_width=True)
    st.markdown("**วิเคราะห์เทคนิค**  \nเครื่องมือการวิเคราะห์ที่ทันสมัย")

with col2:
    st.image("https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=400&h=300&fit=crop", 
             caption="Global Markets", use_container_width=True)
    st.markdown("**ตลาดโลก**  \nเข้าถึงตลาดหลักทรัพย์ทั่วโลก")

with col3:
    st.image("https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=400&h=300&fit=crop", 
             caption="Investment Strategy", use_container_width=True)
    st.markdown("**กลยุทธ์การลงทุน**  \nแนวทางการลงทุนที่เหมาะสม")

# Current Market Status
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-chart-line'></i> สถานการณ์ตลาดวันนี้</h2>", unsafe_allow_html=True)

# Fetch real market data
@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_market_data():
    """ดึงข้อมูลตลาดจริงจาก yfinance"""
    market_indices = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "Dow Jones": "^DJI",
        "Nikkei 225": "^N225"
    }
    
    market_data = {}
    
    if YFINANCE_AVAILABLE:
        try:
            for name, symbol in market_indices.items():
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="2d")
                
                if len(hist) >= 2:
                    current_price = hist['Close'].iloc[-1]
                    prev_price = hist['Close'].iloc[-2]
                    change = current_price - prev_price
                    change_pct = (change / prev_price) * 100
                    
                    market_data[name] = {
                        "price": f"{current_price:,.2f}",
                        "change": f"{change:+.2f}",
                        "change_pct": f"{change_pct:+.2f}%"
                    }
                else:
                    # ถ้าไม่มีข้อมูลเพียงพอ
                    market_data[name] = {
                        "price": "N/A",
                        "change": "0.00",
                        "change_pct": "0.00%"
                    }
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {str(e)}")
            return None
    else:
        # ถ้าไม่มี yfinance ใช้ข้อมูลจำลอง
        market_data = {
            "S&P 500": {"price": "4,500.25", "change": "+12.50", "change_pct": "+0.28%"},
            "NASDAQ": {"price": "14,200.30", "change": "-25.80", "change_pct": "-0.18%"},
            "Dow Jones": {"price": "35,100.45", "change": "+85.30", "change_pct": "+0.24%"},
            "Nikkei 225": {"price": "33,750.89", "change": "+180.20", "change_pct": "+0.54%"}
        }
    
    return market_data

# Display market data
market_data = get_market_data()

if market_data:
    col1, col2, col3, col4 = st.columns(4)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    cols = [col1, col2, col3, col4]
    for i, (name, data) in enumerate(market_data.items()):
        with cols[i]:
            # แยก change และ change_pct
            change_value = data["change"].replace("+", "")
            st.metric(name, data["price"], f"{data['change']} ({data['change_pct']})")
    
    if YFINANCE_AVAILABLE:
        st.caption(f"📊 ข้อมูลจริงจาก Yahoo Finance | อัพเดท: {current_date}")
    else:
        st.caption(f"⚠️ ข้อมูลจำลอง (ติดตั้ง yfinance เพื่อดูข้อมูลจริง) | {current_date}")
        st.info("💡 รันคำสั่ง: `pip install yfinance` เพื่อดูข้อมูลตลาดแบบเรียลไทม์")
else:
    st.warning("ไม่สามารถดึงข้อมูลตลาดได้ในขณะนี้")

# Popular Stocks Section
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-fire'></i> หุ้นยอดนิยม</h2>", unsafe_allow_html=True)

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_popular_stocks():
    """ดึงข้อมูลหุ้นยอดนิยม"""
    popular_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "JPM"]
    stocks_data = []
    
    if YFINANCE_AVAILABLE:
        try:
            for symbol in popular_symbols:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                hist = ticker.history(period="1d")
                
                if not hist.empty:
                    current_price = hist['Close'].iloc[-1]
                    # ดึง previous close จาก info
                    prev_close = info.get('previousClose', current_price)
                    change = current_price - prev_close
                    change_pct = (change / prev_close) * 100 if prev_close != 0 else 0
                    
                    stocks_data.append({
                        "symbol": symbol,
                        "name": info.get('shortName', symbol),
                        "price": current_price,
                        "change": change,
                        "change_pct": change_pct
                    })
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการดึงข้อมูลหุ้น: {str(e)}")
            return None
    else:
        # ข้อมูลจำลอง
        stocks_data = [
            {"symbol": "AAPL", "name": "Apple Inc.", "price": 178.50, "change": 2.30, "change_pct": 1.31},
            {"symbol": "MSFT", "name": "Microsoft Corp", "price": 412.30, "change": -1.50, "change_pct": -0.36},
            {"symbol": "GOOGL", "name": "Alphabet Inc", "price": 142.80, "change": 3.20, "change_pct": 2.29},
            {"symbol": "AMZN", "name": "Amazon.com Inc", "price": 178.25, "change": 1.75, "change_pct": 0.99},
            {"symbol": "TSLA", "name": "Tesla Inc", "price": 242.80, "change": -4.50, "change_pct": -1.82},
            {"symbol": "NVDA", "name": "NVIDIA Corp", "price": 495.20, "change": 8.30, "change_pct": 1.70},
            {"symbol": "META", "name": "Meta Platforms", "price": 485.60, "change": 5.40, "change_pct": 1.12},
            {"symbol": "JPM", "name": "JPMorgan Chase", "price": 198.75, "change": -0.85, "change_pct": -0.43}
        ]
    
    return stocks_data

# Display popular stocks
popular_stocks = get_popular_stocks()

if popular_stocks:
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]
    
    for i, stock in enumerate(popular_stocks):
        with cols[i % 4]:
            # กำหนดสีตาม change
            delta_color = "normal"
            if stock["change"] > 0:
                delta_color = "normal"
            elif stock["change"] < 0:
                delta_color = "inverse"
                
            st.metric(
                label=f"**{stock['symbol']}**",
                value=f"${stock['price']:.2f}",
                delta=f"{stock['change']:+.2f} ({stock['change_pct']:+.2f}%)"
            )
            st.caption(stock['name'][:20])
    
    if YFINANCE_AVAILABLE:
        st.caption("📈 ข้อมูลจริงจาก Yahoo Finance (อัพเดททุก 5 นาที)")
    else:
        st.caption("⚠️ ข้อมูลจำลอง - ติดตั้ง yfinance เพื่อดูข้อมูลจริง")
else:
    st.warning("ไม่สามารถดึงข้อมูลหุ้นได้ในขณะนี้")

# Welcome Message
st.markdown("""
### <i class='fa-solid fa-handshake'></i> ยินดีต้อนรับนักลงทุนมือใหม่!

การลงทุนในหุ้นต่างประเทศเป็นหนทางสู่การสร้างความมั่งคั่งระยะยาว เว็บแอปนี้จะพาคุณเรียนรู้:

<i class='fa-solid fa-book-open'></i> **พื้นฐานการลงทุน** - ความรู้เบื้องต้นที่จำเป็น  
<i class='fa-solid fa-chart-line'></i> **การวิเคราะห์ข้อมูล** - เครื่องมือและเทคนิคการวิเคราะห์  
<i class='fa-solid fa-shield-halved'></i> **การบริหารความเสี่ยง** - วิธีป้องกันและลดความเสี่ยง  
<i class='fa-solid fa-lightbulb'></i> **กลยุทธ์การลงทุน** - แนวทางที่เหมาะสมกับคุณ  
""", unsafe_allow_html=True)

# Learning Path with modern cards
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-map'></i> เส้นทางการเรียนรู้</h2>", unsafe_allow_html=True)

# Learning cards
learning_cards = [
    {
        "icon": "<i class='fa-solid fa-book-open'></i>",
        "title": "พื้นฐานการลงทุน",
        "desc": "เริ่มต้นด้วยความรู้พื้นฐาน",
        "link": "/1_Basics_of_Investment",
        "color": "#4CAF50"
    },
    {
        "icon": "<i class='fa-solid fa-chart-line'></i>", 
        "title": "วิเคราะห์ข้อมูลหุ้น",
        "desc": "เครื่องมือวิเคราะห์แบบเรียลไทม์",
        "link": "/2_Stock_Data_Analysis", 
        "color": "#2196F3"
    },
    {
        "icon": "<i class='fa-solid fa-coins'></i>",
        "title": "ความเสี่ยงและค่าเงิน", 
        "desc": "ทำความเข้าใจ Forex Risk",
        "link": "/3_Forex_and_Risk",
        "color": "#FF9800"
    },
    {
        "icon": "<i class='fa-solid fa-lightbulb'></i>",
        "title": "เคล็ดลับและแหล่งความรู้",
        "desc": "ทรัพยากรและกลยุทธ์ขั้นสูง", 
        "link": "/4_About_and_Tips",
        "color": "#9C27B0"
    }
]

# Display learning cards
cols = st.columns(2)
for i, card in enumerate(learning_cards):
    with cols[i % 2]:
        st.markdown(f"""
        <div style="
            background: {card['color']}; 
            background: linear-gradient(135deg, {card['color']}dd, {card['color']}99);
            padding: 1.5rem; 
            border-radius: 12px; 
            margin: 0.5rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        ">
            <h3 style="color: white; margin: 0;">
                {card['icon']} {card['title']}
            </h3>
            <p style="color: white; opacity: 0.9; margin: 0.5rem 0;">
                {card['desc']}
            </p>
            <a href="{card['link']}" target="_self" style="
                color: white; 
                text-decoration: none; 
                font-weight: bold;
                opacity: 0.8;
            ">เริ่มเรียนรู้ →</a>
        </div>
        """, unsafe_allow_html=True)

# Features Section
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-star'></i> ฟีเจอร์เด่น</h2>", unsafe_allow_html=True)

feature_cols = st.columns(2)

with feature_cols[0]:
    st.markdown("""
    ### <i class='fa-solid fa-screwdriver-wrench'></i> เครื่องมือที่ทรงพลัง
    
    <i class='fa-solid fa-chart-line'></i> **Real-time Stock Data**  
    ข้อมูลหุ้นแบบเรียลไทม์จาก Alpha Vantage API
    
    <i class='fa-solid fa-chart-area'></i> **Interactive Charts**  
    กราฟการวิเคราะห์แบบโต้ตอบได้ด้วย Plotly
    
    <i class='fa-solid fa-calculator'></i> **Risk Calculator**  
    เครื่องคำนวณความเสี่ยงจากค่าเงิน
    
    <i class='fa-solid fa-mobile-screen'></i> **Responsive Design**  
    ใช้งานได้บนทุกอุปกรณ์
    """, unsafe_allow_html=True)

with feature_cols[1]:
    st.markdown("""
    ### <i class='fa-solid fa-graduation-cap'></i> แหล่งเรียนรู้ครบครัน
    
    <i class='fa-solid fa-book'></i> **Educational Content**  
    เนื้อหาการศึกษาที่ครอบคลุมทุกระดับ
    
    <i class='fa-solid fa-globe'></i> **Global Markets**  
    ข้อมูลจากตลาดหลักทรัพย์ทั่วโลก
    
    <i class='fa-solid fa-lightbulb'></i> **Expert Tips**  
    เคล็ดลับจากผู้เชี่ยวชาญการลงทุน
    
    <i class='fa-solid fa-lock'></i> **Safe Learning**  
    สภาพแวดล้อมการเรียนรู้ที่ปลอดภัย
    """, unsafe_allow_html=True)

# Popular Stocks Preview
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-fire'></i> หุ้นยอดนิยม</h2>", unsafe_allow_html=True)

pop_cols = st.columns(4)
popular_stocks = [
    {"symbol": "AAPL", "name": "Apple Inc.", "price": "$175.84", "change": "+2.1%"},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "price": "$338.11", "change": "+0.8%"}, 
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "price": "$126.50", "change": "-0.3%"},
    {"symbol": "TSLA", "name": "Tesla Inc.", "price": "$248.50", "change": "+4.2%"}
]

for i, stock in enumerate(popular_stocks):
    with pop_cols[i]:
        change_color = "green" if "+" in stock["change"] else "red"
        st.markdown(f"""
        <div style="
            border: 1px solid #ddd; 
            padding: 1rem; 
            border-radius: 8px; 
            text-align: center;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            <h4 style="margin: 0; color: #333;">{stock['symbol']}</h4>
            <p style="margin: 0.5rem 0; color: #666; font-size: 0.9rem;">{stock['name']}</p>
            <p style="margin: 0; font-weight: bold; font-size: 1.1rem;">{stock['price']}</p>
            <p style="margin: 0; color: {change_color};">{stock['change']}</p>
        </div>
        """, unsafe_allow_html=True)

# Quick Start Tips
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-rocket'></i> เริ่มต้นอย่างไร?</h2>", unsafe_allow_html=True)

tips_cols = st.columns(3)

with tips_cols[0]:
    st.markdown("""
    #### <i class='fa-solid fa-1'></i> เตรียมตัว
    - <i class='fa-solid fa-book'></i> อ่านพื้นฐานการลงทุน
    - <i class='fa-solid fa-money-bill-wave'></i> กำหนดงบประมาณ
    - <i class='fa-solid fa-bullseye'></i> ตั้งเป้าหมาย
    """, unsafe_allow_html=True)

with tips_cols[1]:
    st.markdown("""
    #### <i class='fa-solid fa-2'></i> เรียนรู้
    - <i class='fa-solid fa-chart-line'></i> ทำความเข้าใจกราฟ
    - <i class='fa-solid fa-magnifying-glass'></i> วิเคราะห์บริษัท
    - <i class='fa-solid fa-scale-balanced'></i> บริหารความเสี่ยง
    """, unsafe_allow_html=True)

with tips_cols[2]:
    st.markdown("""
    #### <i class='fa-solid fa-3'></i> ลงมือทำ
    - <i class='fa-solid fa-briefcase'></i> เปิดบัญชีลงทุน
    - <i class='fa-solid fa-arrow-trend-up'></i> เริ่มลงทุนจำนวนเล็ก
    - <i class='fa-solid fa-pen-to-square'></i> ติดตามผล
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><i class='fa-solid fa-triangle-exclamation'></i> <strong>คำเตือน:</strong> ข้อมูลในแอปนี้เป็นเพียงการศึกษาเท่านั้น ไม่ใช่คำแนะนำในการลงทุน</p>
    <p><i class='fa-solid fa-lightbulb'></i> การลงทุนมีความเสี่ยง ควรศึกษาข้อมูลให้ครบถ้วนก่อนตัดสินใจ</p>
</div>
""", unsafe_allow_html=True)