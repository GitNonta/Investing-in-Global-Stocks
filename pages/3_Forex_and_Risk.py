import streamlit as st
import sys
import os

# เพิ่ม path สำหรับ import css_loader
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from css_loader import load_all_styles

# Configuration
st.set_page_config(
    page_title="Forex & Risk - Global Stock Guide", 
    page_icon="💱", 
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
    if st.button("◉ พื้นฐานการลงทุน", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")
with col3:
    if st.button("� วิเคราะห์หุ้น", use_container_width=True):
        st.switch_page("pages/2_Stock_Data_Analysis.py")
with col4:
    if st.button("⚖ ความเสี่ยง", use_container_width=True, type="primary"):
        st.rerun()
with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True):
        st.switch_page("pages/4_About_and_Tips.py")

st.divider()
st.markdown("<h1><i class='fa-solid fa-coins'></i> ค่าเงินและความเสี่ยงในการลงทุนต่างประเทศ</h1>", unsafe_allow_html=True)
st.write("""
เมื่อเราลงทุนในตลาดต่างประเทศ เราไม่ได้เสี่ยงแค่ราคาหุ้น แต่ยังเสี่ยงกับ “ค่าเงิน”  
เช่น ถ้าคุณถือหุ้น Tesla (TSLA) ที่ซื้อด้วย USD แต่เงินบาทแข็งขึ้น ผลตอบแทนจริงอาจลดลง

**ตัวอย่างความเสี่ยง:**
- หุ้นขึ้น 10% แต่ค่าเงิน USD อ่อนลง 8% → กำไรจริงเหลือเพียง 2%
- หุ้นลง 5% แต่ค่าเงินแข็งขึ้น 3% → ขาดทุนจริงแค่ 2%

**แนวทางลดความเสี่ยง:**
- ลงทุนผ่านกองทุนรวมต่างประเทศ (Foreign ETF)  
- ใช้พอร์ตกระจายความเสี่ยงหลายประเทศ  
- ใช้กลยุทธ์ "Dollar-Cost Averaging (DCA)"
""")

# Risk Calculator
st.markdown("### <i class='fa-solid fa-calculator'></i> คำนวณความเสี่ยงค่าเงิน", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    stock_return = st.number_input("ผลตอบแทนจากหุ้น (%)", value=10.0)
    
with col2:
    forex_change = st.number_input("การเปลี่ยนแปลงค่าเงิน (%)", value=-5.0)

actual_return = stock_return + forex_change
st.metric("ผลตอบแทนจริง", f"{actual_return:.1f}%", delta=f"{forex_change:+.1f}%")

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← ก่อนหน้า: วิเคราะห์ข้อมูล", use_container_width=True):
        st.switch_page("pages/2_Stock_Data_Analysis.py")

with col3:
    if st.button("ถัดไป: เคล็ดลับ →", use_container_width=True):
        st.switch_page("pages/4_About_and_Tips.py")
