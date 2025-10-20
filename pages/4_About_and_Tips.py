import streamlit as st

# Configuration
st.set_page_config(
    page_title="Tips & Resources - Global Stock Guide", 
    page_icon="�", 
    layout="wide"
)

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
    if st.button("📊 วิเคราะห์หุ้น", use_container_width=True):
        st.switch_page("pages/2_Stock_Data_Analysis.py")
with col4:
    if st.button("💱 ความเสี่ยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")
with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True, type="primary"):
        st.rerun()

st.divider()
st.header("� เคล็ดลับและแหล่งความรู้")
st.success("🎉 จบเนื้อหาการเรียนรู้ — ยินดีด้วย!")

# Tips Section
st.subheader("💎 เคล็ดลับสำคัญในการลงทุนหุ้นต่างประเทศ")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ ควรทำ (DO)
    1. **กระจายความเสี่ยง** - อย่าลงทุนในหุ้นตัวเดียว
    2. **ลงทุนระยะยาว** - อดทนและรอผลตอบแทน
    3. **ศึกษาข้อมูล** - อ่านรายงานและข่าวสารอยู่เสมอ
    4. **ตั้งเป้าหมาย** - รู้ว่าเราลงทุนเพื่ออะไร
    5. **ใช้ DCA** - ลงทุนเป็นงวดๆ ลดความเสี่ยง
    6. **ควบคุมอารมณ์** - อย่าตื่นตระหนกเมื่อราคาผันผวน
    """)

with col2:
    st.markdown("""
    ### ❌ ไม่ควรทำ (DON'T)
    1. **ยืมเงินมาลงทุน** - อย่าใช้เงินที่ไม่ใช่เงินเก็บ
    2. **ฟังซาน** - อย่าเชื่อคำแนะนำที่ไม่มีที่มา
    3. **ลงทุนแบบลิง** - อย่าซื้อหุ้นที่ไม่เข้าใจ
    4. **ซื้อขายบ่อย** - ค่าธรรมเนียมจะกัดกินกำไร
    5. **โลภมาก** - อยากรวยเร็วมักขาดทุน
    6. **ละเลยความเสี่ยง** - ต้องเข้าใจความเสี่ยงก่อนลงทุน
    """)

st.divider()

# Resources Section
st.subheader("📚 แหล่งความรู้เพิ่มเติม")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📺 YouTube Channels
    - **The Motley Fool**
    - **Ben Felix**
    - **Graham Stephan**
    - **Bloomberg Markets**
    """)

with col2:
    st.markdown("""
    ### 🎙️ Podcasts
    - **Chat with Traders**
    - **The Investors Podcast**
    - **Planet Money**
    - **MarketWatch**
    """)

with col3:
    st.markdown("""
    ### 📖 Books
    - **The Intelligent Investor**
    - **A Random Walk Down Wall Street**
    - **The Little Book**
    - **Rich Dad Poor Dad**
    """)

st.divider()

# Thai Resources
st.subheader("🇹🇭 แหล่งความรู้ภาษาไทย")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📱 เว็บไซต์และแอพ
    - **[SET.or.th](https://www.set.or.th)**
    - **Finanseer**
    - **The Secret Sauce**
    - **Finnomena**
    """)

with col2:
    st.markdown("""
    ### 📊 โบรกเกอร์ในไทย
    - **Bualuang Securities**
    - **KTB Securities**
    - **Phillip Securities**
    - **Interactive Brokers**
    """)

st.divider()

# Next Steps
st.subheader("🎯 ขั้นตอนต่อไป:")
st.markdown("""
1. **เปิดบัญชีลงทุน** กับโบรกเกอร์ที่มีบริการซื้อหุ้นต่างประเทศ
2. **เริ่มต้นด้วยเงินจำนวนน้อย** เพื่อทดลองและเรียนรู้
3. **ฝึกติดตามข่าวสาร** และวิเคราะห์หุ้นที่สนใจ
4. **สร้างพอร์ตโฟลิโอ** ที่กระจายความเสี่ยง

⚠️ **สำคัญ:** ข้อมูลในเว็บไซต์นี้เป็นเพียงการศึกษาเท่านั้น **ไม่ใช่คำแนะนำในการลงทุน**
""")



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
    <h3>🌟 ขอบคุณที่ใช้ Global Stock Investment Guide! 🌟</h3>
    <p>สร้างด้วย ❤️ เพื่อการเรียนรู้การลงทุนหุ้นต่างประเทศ</p>
    <p><em>Happy Investing! 📈💰</em></p>
</div>
""", unsafe_allow_html=True)
