import streamlit as st
import sys
import os

# เพิ่ม path สำหรับ import css_loader
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from css_loader import load_all_styles

# Configuration
st.set_page_config(
    page_title="Investment Basics - Global Stock Guide", 
    page_icon="📘", 
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

# Modern Menu Bar (CSS loaded from styles/main.css)
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
    if st.button("◉ พื้นฐานการลงทุน", use_container_width=True, type="primary"):
        st.rerun()
with col3:
    if st.button("� วิเคราะห์หุ้น", use_container_width=True):
        st.switch_page("pages/2_Stock_Data_Analysis.py")
with col4:
    if st.button("⚖ ความเสี่ยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True):
        st.switch_page("pages/4_About_and_Tips.py")

st.divider()

st.markdown("<h1><i class='fa-solid fa-book-open'></i> พื้นฐานการลงทุนในหุ้นต่างประเทศ</h1>", unsafe_allow_html=True)
st.write("""
การลงทุนในหุ้นต่างประเทศหมายถึงการซื้อหุ้นของบริษัทที่จดทะเบียนในตลาดหลักทรัพย์นอกประเทศของเรา  
เช่น Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), หรือ Amazon (AMZN)
""")

st.markdown("""
**<i class='fa-solid fa-circle-check' style='color: #4caf50;'></i> ข้อดี:**
- <i class='fa-solid fa-shield-halved'></i> กระจายความเสี่ยงจากเศรษฐกิจในประเทศ  
- <i class='fa-solid fa-rocket'></i> เข้าถึงบริษัทระดับโลกที่เติบโตสูง  
- <i class='fa-solid fa-dollar-sign'></i> ได้รับผลตอบแทนจากค่าเงิน (ถ้าค่า USD แข็งขึ้น)

**<i class='fa-solid fa-triangle-exclamation' style='color: #ff9800;'></i> ความเสี่ยง:**
- <i class='fa-solid fa-chart-line'></i> ความผันผวนของค่าเงิน  
- <i class='fa-solid fa-gavel'></i> กฎระเบียบและภาษีที่แตกต่างกัน  
- <i class='fa-solid fa-money-bill-wave'></i> ต้นทุนค่าธรรมเนียมที่อาจสูงกว่า
""", unsafe_allow_html=True)

st.markdown("<h2><i class='fa-solid fa-fire'></i> ตัวอย่างหุ้นยอดนิยม</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### <i class='fa-brands fa-apple'></i> Apple (AAPL)
    - **ประเภท:** เทคโนโลยี
    - **ตลาด:** NASDAQ
    - **ประเทศ:** สหรัฐอเมริกา
    - **จุดเด่น:** iPhone, iPad, MacBook
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    ### <i class='fa-solid fa-car'></i> Tesla (TSLA)
    - **ประเภท:** รถยนต์ไฟฟ้า
    - **ตลาด:** NASDAQ
    - **ประเทศ:** สหรัฐอเมริกา
    - **จุดเด่น:** EV, พลังงานหมุนเวียน
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    ### <i class='fa-brands fa-microsoft'></i> Microsoft (MSFT)
    - **ประเภท:** ซอฟต์แวร์
    - **ตลาด:** NASDAQ
    - **ประเทศ:** สหรัฐอเมริกา
    - **จุดเด่น:** Windows, Azure, AI
    """, unsafe_allow_html=True)

st.divider()

st.markdown("<h2><i class='fa-solid fa-book'></i> ศัพท์ที่ควรรู้</h2>", unsafe_allow_html=True)
st.markdown("""
1. **<i class='fa-solid fa-tag'></i> Stock Symbol (รหัสหุ้น):** ตัวอักษรย่อที่ใช้แทนชื่อบริษัท เช่น AAPL = Apple  
2. **<i class='fa-solid fa-money-bill-trend-up'></i> Market Price (ราคาตลาด):** ราคาหุ้นล่าสุดที่ซื้อขายกันในตลาด  
3. **<i class='fa-solid fa-hand-holding-dollar'></i> Dividend (เงินปันผล):** เงินที่บริษัทจ่ายคืนให้ผู้ถือหุ้น  
4. **<i class='fa-solid fa-percent'></i> P/E Ratio:** อัตราส่วนราคาต่อกำไร ใช้ประเมินว่าหุ้นแพงหรือถูก  
5. **<i class='fa-solid fa-building'></i> Market Cap (มูลค่าตลาด):** มูลค่ารวมของหุ้นทั้งหมดของบริษัท
6. **<i class='fa-solid fa-briefcase'></i> Portfolio (พอร์ตโฟลิโอ):** กลุ่มของสินทรัพย์ที่ลงทุนไว้
7. **<i class='fa-solid fa-handshake'></i> Broker (โบรกเกอร์):** บริษัทที่เป็นตัวกลางในการซื้อขายหุ้น
""", unsafe_allow_html=True)

st.divider()

st.markdown("<h2><i class='fa-solid fa-list-ol'></i> ขั้นตอนการเริ่มลงทุน</h2>", unsafe_allow_html=True)
st.markdown("""
1. **<i class='fa-solid fa-graduation-cap'></i> ศึกษาข้อมูล:** เรียนรู้เกี่ยวกับตลาดหุ้นและบริษัทที่สนใจ
2. **<i class='fa-solid fa-user-plus'></i> เปิดบัญชี:** สมัครบัญชีกับโบรกเกอร์ที่มีบริการหุ้นต่างประเทศ เช่น:
   - ธนาคารกรุงเทพ (Bualuang iFin)
   - KTB Securities (KT ZMICO)
   - Interactive Brokers (สำหรับเงินทุนมาก)
3. **<i class='fa-solid fa-money-bill-transfer'></i> โอนเงิน:** โอนเงินเข้าบัญชีเพื่อซื้อหุ้น
4. **<i class='fa-solid fa-magnifying-glass-chart'></i> เลือกหุ้น:** เลือกหุ้นที่ต้องการซื้อ
5. **<i class='fa-solid fa-cart-shopping'></i> ซื้อขาย:** ส่งคำสั่งซื้อหุ้นผ่านแพลตฟอร์มของโบรกเกอร์
6. **<i class='fa-solid fa-chart-simple'></i> ติดตาม:** ติดตามผลการลงทุนและข่าวสารอยู่เสมอ
""", unsafe_allow_html=True)

st.divider()

st.markdown("<h2><i class='fa-solid fa-shield-halved'></i> หลักการกระจายความเสี่ยง (Diversification)</h2>", unsafe_allow_html=True)
st.write("""
อยาลงทนในหนตวเดยว! ควรกระจายเงนลงทนไปในหลายหน หลายประเภทธรกจ และหลายประเทศ

**ตวอยางพอรตโฟลโอแนะนำ:**
- 40% เทคโนโลย (Tech): Apple, Microsoft, Nvidia
- 30% การเงน (Finance): JPMorgan, Berkshire Hathaway
- 20% สขภาพ (Healthcare): Johnson & Johnson, Pfizer
- 10% สนคาอปโภคบรโภค (Consumer): Coca-Cola, Procter & Gamble
""")

col1, col2 = st.columns(2)
with col1:
    st.success("<i class='fa-solid fa-circle-check'></i> **ทำ:** กระจายความเสี่ยง, ลงทุนระยะยาว, ศึกษาข้อมูล", icon="✅")
with col2:
    st.error("<i class='fa-solid fa-circle-xmark'></i> **ไม่ควรทำ:** ลงทุนแบบฟังซาน, ยืมเงินมาลงทุน, เชื่อข่าวลือ", icon="⚠️")

st.divider()

st.info("""
<i class='fa-solid fa-lightbulb'></i> **เคล็ดลับ:** เริ่มต้นด้วยการลงทุนในกองทุน ETF ที่ติดตามดัชนี S&P 500 (เช่น SPY หรือ VOO)  
เพราะจะช่วยให้คุณกระจายความเสี่ยงไปยังหุ้นชั้นนำ 500 บริษัทในสหรัฐ ในครั้งเดียว!
""", icon="💡")

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='color: #666;'><i class='fa-solid fa-arrow-right'></i> อ่านต่อ: <a href='/2_Stock_Data_Analysis' target='_self'>วิเคราะห์ข้อมูลหุ้นแบบเรียลไทม์</a></p>
</div>
""", unsafe_allow_html=True)
