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
    "home": "<i class=''fa-solid fa-house'' style=''margin-right:6px;''></i>",
    "basics": "<i class=''fa-solid fa-book-open'' style=''margin-right:6px;''></i>",
    "analysis": "<i class=''fa-solid fa-chart-line'' style=''margin-right:6px;''></i>",
    "forex": "<i class=''fa-solid fa-coins'' style=''margin-right:6px;''></i>",
    "tips": "<i class=''fa-solid fa-lightbulb'' style=''margin-right:6px;''></i>"
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
        <a href="/" target="_self" class="logo"> Global Stocks</a>
        <div class="menu-items">
            <a href="/" target="_self" class="menu-item">{menu_icons['home']}หน้าหลัก</a>
            <a href="1_Basics_of_Investment" target="_self" class="menu-item active">{menu_icons['basics']}พื้นฐานการลงทุน</a>
            <a href="2_Stock_Data_Analysis" target="_self" class="menu-item">{menu_icons['analysis']}วิเคราะห์หุ้น</a>
            <a href="3_Forex_and_Risk" target="_self" class="menu-item">{menu_icons['forex']}ความเสี่ยง</a>
            <a href="4_About_and_Tips" target="_self" class="menu-item">{menu_icons['tips']}เคล็ดลับ</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.header(" พนฐานการลงทนในหนตางประเทศ")
st.write("""
การลงทนในหนตางประเทศหมายถงการซอหนของบรษททจดทะเบยนในตลาดหลกทรพยนอกประเทศของเรา  
เชน Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), หรอ Amazon (AMZN)

**ขอด:**
- กระจายความเสยงจากเศรษฐกจในประเทศ  
- เขาถงบรษทระดบโลกทเตบโตสง  
- ไดรบผลตอบแทนจากคาเงน (ถาคา USD แขงขน)

**ความเสยง:**
- ความผนผวนของคาเงน  
- กฎระเบยบและภาษทแตกตางกน  
- ตนทนคาธรรมเนยมทอาจสงกวา
""")

st.subheader(" ตวอยางหนยอดนยม")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ###  Apple (AAPL)
    - **ประเภท:** เทคโนโลย
    - **ตลาด:** NASDAQ
    - **ประเทศ:** สหรฐอเมรกา
    - **จดเดน:** iPhone, iPad, MacBook
    """)

with col2:
    st.markdown("""
    ###  Tesla (TSLA)
    - **ประเภท:** รถยนตไฟฟา
    - **ตลาด:** NASDAQ
    - **ประเทศ:** สหรฐอเมรกา
    - **จดเดน:** EV, พลงงานหมนเวยน
    """)

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
    st.success(" **ทำ:** กระจายความเสยง, ลงทนระยะยาว, ศกษาขอมล")
with col2:
    st.error(" **ไมควรทำ:** ลงทนแบบฟงซาน, ยมเงนมาลงทน, เชอขาวลอ")

st.divider()

st.info("""
 **เคลดลบ:** เรมตนดวยการลงทนในกองทน ETF ทตดตามดชน S&P 500 (เชน SPY หรอ VOO)  
เพราะจะชวยใหคณกระจายความเสยงไปยงหนชนนำ 500 บรษทในสหรฐ ในครงเดยว!
""")

st.markdown("---")
st.markdown("""
<div style=''text-align: center; padding: 20px;''>
    <p style=''color: #666;''> อานตอ: <a href=''/2_Stock_Data_Analysis'' target=''_self''>วเคราะหขอมลหนแบบเรยลไทม</a></p>
</div>
""", unsafe_allow_html=True)
