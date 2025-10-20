import streamlit as st
import sys
import os

# Add the project root to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from css_loader import load_all_styles

# Configuration
st.set_page_config(
    page_title="Tips & Resources - Global Stock Guide", 
    page_icon="�", 
    layout="wide"
)

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
    if st.button("🏠 หน้าหลัก", use_container_width=True):
        st.switch_page("streamlit_app.py")
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
    if st.button("💡 เคล็ดลับ", use_container_width=True, type="primary"):
        st.rerun()

st.divider()
st.markdown("<h1><i class='fa-solid fa-lightbulb'></i> เคล็ดลับและแหล่งความรู้</h1>", unsafe_allow_html=True)
st.success("🎉 จบเนื้อหาการเรียนรู้ — ยินดีด้วย!", icon="🎉")

# Tips Section
st.markdown("<h2><i class='fa-solid fa-gem'></i> เคล็ดลับสำคัญในการลงทุนหุ้นต่างประเทศ</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### <i class='fa-solid fa-check-circle' style='color:green;'></i> ควรทำ (DO)
    1. **กระจายความเสี่ยง** - อย่าลงทุนในหุ้นตัวเดียว
    2. **ลงทุนระยะยาว** - อดทนและรอผลตอบแทน
    3. **ศึกษาข้อมูล** - อ่านรายงานและข่าวสารอยู่เสมอ
    4. **ตั้งเป้าหมาย** - รู้ว่าเราลงทุนเพื่ออะไร
    5. **ใช้ DCA** - ลงทุนเป็นงวดๆ ลดความเสี่ยง
    6. **ควบคุมอารมณ์** - อย่าตื่นตระหนกเมื่อราคาผันผวน
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    ### <i class='fa-solid fa-times-circle' style='color:red;'></i> ไม่ควรทำ (DON'T)
    1. **ยืมเงินมาลงทุน** - อย่าใช้เงินที่ไม่ใช่เงินเก็บ
    2. **ฟังซาน** - อย่าเชื่อคำแนะนำที่ไม่มีที่มา
    3. **ลงทุนแบบลิง** - อย่าซื้อหุ้นที่ไม่เข้าใจ
    4. **ซื้อขายบ่อย** - ค่าธรรมเนียมจะกัดกินกำไร
    5. **โลภมาก** - อยากรวยเร็วมักขาดทุน
    6. **ละเลยความเสี่ยง** - ต้องเข้าใจความเสี่ยงก่อนลงทุน
    """, unsafe_allow_html=True)

st.divider()

# Resources Section
st.markdown("<h2><i class='fa-solid fa-book-open'></i> แหล่งความรู้เพิ่มเติม</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### <i class='fa-brands fa-youtube' style='color:red;'></i> YouTube Channels
    - **The Motley Fool**
    - **Ben Felix**
    - **Graham Stephan**
    - **Bloomberg Markets**
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    ### <i class='fa-solid fa-podcast' style='color:#9146FF;'></i> Podcasts
    - **Chat with Traders**
    - **The Investors Podcast**
    - **Planet Money**
    - **MarketWatch**
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    ### <i class='fa-solid fa-book' style='color:#4A90E2;'></i> Books
    - **The Intelligent Investor**
    - **A Random Walk Down Wall Street**
    - **The Little Book**
    - **Rich Dad Poor Dad**
    """, unsafe_allow_html=True)

st.divider()

# Thai Resources
st.markdown("<h2><i class='fa-solid fa-flag' style='color:#ED1C24;'></i> แหล่งความรู้ภาษาไทย</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### <i class='fa-solid fa-mobile-screen'></i> เว็บไซต์และแอพ
    - **[SET.or.th](https://www.set.or.th)**
    - **Finanseer**
    - **The Secret Sauce**
    - **Finnomena**
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    ### <i class='fa-solid fa-building-columns'></i> โบรกเกอร์ในไทย
    - **Bualuang Securities**
    - **KTB Securities**
    - **Phillip Securities**
    - **Interactive Brokers**
    """, unsafe_allow_html=True)

st.divider()

# Next Steps
st.markdown("<h2><i class='fa-solid fa-bullseye'></i> ขั้นตอนต่อไป:</h2>", unsafe_allow_html=True)
st.markdown("""
1. **เปิดบัญชีลงทุน** กับโบรกเกอร์ที่มีบริการซื้อหุ้นต่างประเทศ
2. **เริ่มต้นด้วยเงินจำนวนน้อย** เพื่อทดลองและเรียนรู้
3. **ฝึกติดตามข่าวสาร** และวิเคราะห์หุ้นที่สนใจ
4. **สร้างพอร์ตโฟลิโอ** ที่กระจายความเสี่ยง

<i class='fa-solid fa-triangle-exclamation' style='color:orange;'></i> **สำคัญ:** ข้อมูลในเว็บไซต์นี้เป็นเพียงการศึกษาเท่านั้น **ไม่ใช่คำแนะนำในการลงทุน**
""", unsafe_allow_html=True)



# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← ก่อนหน้า: ความเสี่ยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")

with col2:
    if st.button("🏠 กลับหน้าหลัก", use_container_width=True):
        st.switch_page("streamlit_app.py")

with col3:
    if st.button("🔄 เริ่มใหม่", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
    <h3><i class='fa-solid fa-star' style='color:gold;'></i> ขอบคุณที่ใช้ Global Stock Investment Guide! <i class='fa-solid fa-star' style='color:gold;'></i></h3>
    <p>สร้างด้วย <i class='fa-solid fa-heart' style='color:red;'></i> เพื่อการเรียนรู้การลงทุนหุ้นต่างประเทศ</p>
    <p><em>Happy Investing! <i class='fa-solid fa-chart-line'></i><i class='fa-solid fa-sack-dollar'></i></em></p>
</div>
""", unsafe_allow_html=True)
