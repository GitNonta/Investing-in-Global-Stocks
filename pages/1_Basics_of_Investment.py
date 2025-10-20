import streamlit as st

# Configuration
st.set_page_config(
    page_title="Investment Basics - Global Stock Guide", 
    page_icon="", 
    layout="wide"
)

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
    if st.button("📘 พื้นฐานการลงทุน", use_container_width=True, type="primary"):
        st.rerun()
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
    ###  Microsoft (MSFT)
    - **ประเภท:** ซอฟตแวร
    - **ตลาด:** NASDAQ
    - **ประเทศ:** สหรฐอเมรกา
    - **จดเดน:** Windows, Azure, AI
    """)

st.divider()

st.subheader(" ศพททควรร")
st.markdown("""
1. **Stock Symbol (รหสหน):** ตวอกษรยอทใชแทนชอบรษท เชน AAPL = Apple  
2. **Market Price (ราคาตลาด):** ราคาหนลาสดทซอขายกนในตลาด  
3. **Dividend (เงนปนผล):** เงนทบรษทจายคนใหผถอหน  
4. **P/E Ratio:** อตราสวนราคาตอกำไร ใชประเมนวาหนแพงหรอถก  
5. **Market Cap (มลคาตลาด):** มลคารวมของหนทงหมดของบรษท
6. **Portfolio (พอรตโฟลโอ):** กลมของสนทรพยทลงทนไว
7. **Broker (โบรกเกอร):** บรษททเปนตวกลางในการซอขายหน
""")

st.divider()

st.subheader(" ขนตอนการเรมลงทน")
st.markdown("""
1. **ศกษาขอมล:** เรยนรเกยวกบตลาดหนและบรษททสนใจ
2. **เปดบญช:** สมครบญชกบโบรกเกอรทมบรการหนตางประเทศ เชน:
   - บวหลวง Securities (BUALUANG iFin)
   - KTB Securities (KT ZMICO)
   - Interactive Brokers (สำหรบเงนทนมาก)
3. **โอนเงน:** โอนเงนเขาบญชเพอซอหน
4. **เลอกหน:** เลอกหนทตองการซอ
5. **ซอขาย:** สงซอหนผานแพลตฟอรมของโบรกเกอร
6. **ตดตาม:** ตดตามผลการลงทนและขาวสารอยเสมอ
""")

st.divider()

st.subheader(" หลกการกระจายความเสยง (Diversification)")
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
