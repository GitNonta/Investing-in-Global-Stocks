import streamlit as stimport streamlit as st



# Configuration# Configuration

st.set_page_config(st.set_page_config(

    page_title="Investment Basics - Global Stock Guide",     page_title="Investment Basics - Global Stock Guide", 

    page_icon="📘",     page_icon="", 

    layout="wide"    layout="wide"

))



# Add FontAwesome CDN# Add FontAwesome CDN

st.markdown("""st.markdown("""

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

""", unsafe_allow_html=True)""", unsafe_allow_html=True)



menu_icons = {menu_icons = {

    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",    "home": "<i class=''fa-solid fa-house'' style=''margin-right:6px;''></i>",

    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",    "basics": "<i class=''fa-solid fa-book-open'' style=''margin-right:6px;''></i>",

    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",    "analysis": "<i class=''fa-solid fa-chart-line'' style=''margin-right:6px;''></i>",

    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",    "forex": "<i class=''fa-solid fa-coins'' style=''margin-right:6px;''></i>",

    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"    "tips": "<i class=''fa-solid fa-lightbulb'' style=''margin-right:6px;''></i>"

}}



# Modern Menu Bar# Modern Menu Bar

st.markdown(f"""st.markdown(f"""

<style><style>

.menu-container {{background: linear-gradient(90deg, #2C3E50 0%, #3498DB 50%, #9B59B6 100%);padding: 0.8rem 0;margin: -1rem -1rem 2rem -1rem;box-shadow: 0 2px 10px rgba(0,0,0,0.1);position: sticky;top: 0;z-index: 999;}}.menu-container {{background: linear-gradient(90deg, #2C3E50 0%, #3498DB 50%, #9B59B6 100%);padding: 0.8rem 0;margin: -1rem -1rem 2rem -1rem;box-shadow: 0 2px 10px rgba(0,0,0,0.1);position: sticky;top: 0;z-index: 999;}}

.menu-nav {{max-width: 1200px;margin: 0 auto;display: flex;justify-content: space-between;align-items: center;padding: 0 2rem;}}.menu-nav {{max-width: 1200px;margin: 0 auto;display: flex;justify-content: space-between;align-items: center;padding: 0 2rem;}}

.logo {{font-size: 1.5rem;font-weight: bold;color: white;text-decoration: none;}}.logo {{font-size: 1.5rem;font-weight: bold;color: white;text-decoration: none;}}

.menu-items {{display: flex;gap: 2rem;align-items: center;}}.menu-items {{display: flex;gap: 2rem;align-items: center;}}

.menu-item {{color: white;text-decoration: none;padding: 0.5rem 1rem;border-radius: 20px;transition: all 0.3s ease;font-weight: 500;font-size: 0.95rem;display: flex;align-items: center;}}.menu-item {{color: white;text-decoration: none;padding: 0.5rem 1rem;border-radius: 20px;transition: all 0.3s ease;font-weight: 500;font-size: 0.95rem;display: flex;align-items: center;}}

.menu-item:hover {{background: rgba(255,255,255,0.2);color: white;transform: translateY(-2px);text-decoration: none;}}.menu-item:hover {{background: rgba(255,255,255,0.2);color: white;transform: translateY(-2px);text-decoration: none;}}

.menu-item.active {{background: rgba(255,255,255,0.3);color: white;}}.menu-item.active {{background: rgba(255,255,255,0.3);color: white;}}

.menu-icon {{margin-right: 0.5rem;}}.menu-icon {{margin-right: 0.5rem;}}

@media (max-width: 768px) {{.menu-nav {{flex-direction: column;padding: 1rem;}}.menu-items {{margin-top: 1rem;flex-wrap: wrap;gap: 1rem;}}}}@media (max-width: 768px) {{.menu-nav {{flex-direction: column;padding: 1rem;}}.menu-items {{margin-top: 1rem;flex-wrap: wrap;gap: 1rem;}}}}

</style></style>



<div class="menu-container"><div class="menu-container">

    <div class="menu-nav">    <div class="menu-nav">

        <div class="logo"><i class='fa-solid fa-globe'></i> Global Stocks</div>        <div class="logo"> Global Stocks</div>

    </div>    </div>

</div></div>

""", unsafe_allow_html=True)""", unsafe_allow_html=True)



# Navigation Menu# Navigation Menu

st.markdown("### <i class='fa-solid fa-book-open'></i> เนื้อหาทั้งหมด", unsafe_allow_html=True)col1, col2, col3, col4, col5 = st.columns(5)

col1, col2, col3, col4, col5 = st.columns(5)with col1:

with col1:    if st.button("🏠 หน้าหลัก", use_container_width=True):

    if st.button("<i class='fa-solid fa-house'></i> หน้าหลัก", use_container_width=True):        st.switch_page("streamlit_app.py")

        st.switch_page("streamlit_app.py")with col2:

with col2:    if st.button("📘 พื้นฐานการลงทุน", use_container_width=True, type="primary"):

    if st.button("<i class='fa-solid fa-book-open'></i> พื้นฐานการลงทุน", use_container_width=True, type="primary"):        st.rerun()

        st.rerun()with col3:

with col3:    if st.button("📊 วิเคราะห์หุ้น", use_container_width=True):

    if st.button("<i class='fa-solid fa-chart-line'></i> วิเคราะห์หุ้น", use_container_width=True):        st.switch_page("pages/2_Stock_Data_Analysis.py")

        st.switch_page("pages/2_Stock_Data_Analysis.py")with col4:

with col4:    if st.button("💱 ความเสี่ยง", use_container_width=True):

    if st.button("<i class='fa-solid fa-coins'></i> ความเสี่ยง", use_container_width=True):        st.switch_page("pages/3_Forex_and_Risk.py")

        st.switch_page("pages/3_Forex_and_Risk.py")with col5:

with col5:    if st.button("💡 เคล็ดลับ", use_container_width=True):

    if st.button("<i class='fa-solid fa-lightbulb'></i> เคล็ดลับ", use_container_width=True):        st.switch_page("pages/4_About_and_Tips.py")

        st.switch_page("pages/4_About_and_Tips.py")

st.divider()

st.divider()

st.header(" พนฐานการลงทนในหนตางประเทศ")

st.markdown("<h1><i class='fa-solid fa-book-open'></i> พื้นฐานการลงทุนในหุ้นต่างประเทศ</h1>", unsafe_allow_html=True)st.write("""

st.write("""การลงทนในหนตางประเทศหมายถงการซอหนของบรษททจดทะเบยนในตลาดหลกทรพยนอกประเทศของเรา  

การลงทุนในหุ้นต่างประเทศหมายถึงการซื้อหุ้นของบริษัทที่จดทะเบียนในตลาดหลักทรัพย์นอกประเทศของเรา  เชน Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), หรอ Amazon (AMZN)

เช่น Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), หรือ Amazon (AMZN)

""")**ขอด:**

- กระจายความเสยงจากเศรษฐกจในประเทศ  

st.markdown("""- เขาถงบรษทระดบโลกทเตบโตสง  

**<i class='fa-solid fa-circle-check' style='color: #4caf50;'></i> ข้อดี:**- ไดรบผลตอบแทนจากคาเงน (ถาคา USD แขงขน)

- <i class='fa-solid fa-shield-halved'></i> กระจายความเสี่ยงจากเศรษฐกิจในประเทศ  

- <i class='fa-solid fa-rocket'></i> เข้าถึงบริษัทระดับโลกที่เติบโตสูง  **ความเสยง:**

- <i class='fa-solid fa-dollar-sign'></i> ได้รับผลตอบแทนจากค่าเงิน (ถ้าค่า USD แข็งขึ้น)- ความผนผวนของคาเงน  

- กฎระเบยบและภาษทแตกตางกน  

**<i class='fa-solid fa-triangle-exclamation' style='color: #ff9800;'></i> ความเสี่ยง:**- ตนทนคาธรรมเนยมทอาจสงกวา

- <i class='fa-solid fa-chart-line'></i> ความผันผวนของค่าเงิน  """)

- <i class='fa-solid fa-gavel'></i> กฎระเบียบและภาษีที่แตกต่างกัน  

- <i class='fa-solid fa-money-bill-wave'></i> ต้นทุนค่าธรรมเนียมที่อาจสูงกว่าst.subheader(" ตวอยางหนยอดนยม")

""", unsafe_allow_html=True)col1, col2, col3 = st.columns(3)



st.markdown("<h2><i class='fa-solid fa-fire'></i> ตัวอย่างหุ้นยอดนิยม</h2>", unsafe_allow_html=True)with col1:

col1, col2, col3 = st.columns(3)    st.markdown("""

    ###  Apple (AAPL)

with col1:    - **ประเภท:** เทคโนโลย

    st.markdown("""    - **ตลาด:** NASDAQ

    ### <i class='fa-brands fa-apple'></i> Apple (AAPL)    - **ประเทศ:** สหรฐอเมรกา

    - **ประเภท:** เทคโนโลยี    - **จดเดน:** iPhone, iPad, MacBook

    - **ตลาด:** NASDAQ    """)

    - **ประเทศ:** สหรัฐอเมริกา

    - **จุดเด่น:** iPhone, iPad, MacBookwith col2:

    """, unsafe_allow_html=True)    st.markdown("""

    ###  Tesla (TSLA)

with col2:    - **ประเภท:** รถยนตไฟฟา

    st.markdown("""    - **ตลาด:** NASDAQ

    ### <i class='fa-solid fa-car'></i> Tesla (TSLA)    - **ประเทศ:** สหรฐอเมรกา

    - **ประเภท:** รถยนต์ไฟฟ้า    - **จดเดน:** EV, พลงงานหมนเวยน

    - **ตลาด:** NASDAQ    """)

    - **ประเทศ:** สหรัฐอเมริกา

    - **จุดเด่น:** EV, พลังงานหมุนเวียนwith col3:

    """, unsafe_allow_html=True)    st.markdown("""

    ###  Microsoft (MSFT)

with col3:    - **ประเภท:** ซอฟตแวร

    st.markdown("""    - **ตลาด:** NASDAQ

    ### <i class='fa-brands fa-microsoft'></i> Microsoft (MSFT)    - **ประเทศ:** สหรฐอเมรกา

    - **ประเภท:** ซอฟต์แวร์    - **จดเดน:** Windows, Azure, AI

    - **ตลาด:** NASDAQ    """)

    - **ประเทศ:** สหรัฐอเมริกา

    - **จุดเด่น:** Windows, Azure, AIst.divider()

    """, unsafe_allow_html=True)

st.subheader(" ศพททควรร")

st.divider()st.markdown("""

1. **Stock Symbol (รหสหน):** ตวอกษรยอทใชแทนชอบรษท เชน AAPL = Apple  

st.markdown("<h2><i class='fa-solid fa-book'></i> ศัพท์ที่ควรรู้</h2>", unsafe_allow_html=True)2. **Market Price (ราคาตลาด):** ราคาหนลาสดทซอขายกนในตลาด  

st.markdown("""3. **Dividend (เงนปนผล):** เงนทบรษทจายคนใหผถอหน  

1. **<i class='fa-solid fa-tag'></i> Stock Symbol (รหัสหุ้น):** ตัวอักษรย่อที่ใช้แทนชื่อบริษัท เช่น AAPL = Apple  4. **P/E Ratio:** อตราสวนราคาตอกำไร ใชประเมนวาหนแพงหรอถก  

2. **<i class='fa-solid fa-money-bill-trend-up'></i> Market Price (ราคาตลาด):** ราคาหุ้นล่าสุดที่ซื้อขายกันในตลาด  5. **Market Cap (มลคาตลาด):** มลคารวมของหนทงหมดของบรษท

3. **<i class='fa-solid fa-hand-holding-dollar'></i> Dividend (เงินปันผล):** เงินที่บริษัทจ่ายคืนให้ผู้ถือหุ้น  6. **Portfolio (พอรตโฟลโอ):** กลมของสนทรพยทลงทนไว

4. **<i class='fa-solid fa-percent'></i> P/E Ratio:** อัตราส่วนราคาต่อกำไร ใช้ประเมินว่าหุ้นแพงหรือถูก  7. **Broker (โบรกเกอร):** บรษททเปนตวกลางในการซอขายหน

5. **<i class='fa-solid fa-building'></i> Market Cap (มูลค่าตลาด):** มูลค่ารวมของหุ้นทั้งหมดของบริษัท""")

6. **<i class='fa-solid fa-briefcase'></i> Portfolio (พอร์ตโฟลิโอ):** กลุ่มของสินทรัพย์ที่ลงทุนไว้

7. **<i class='fa-solid fa-handshake'></i> Broker (โบรกเกอร์):** บริษัทที่เป็นตัวกลางในการซื้อขายหุ้นst.divider()

""", unsafe_allow_html=True)

st.subheader(" ขนตอนการเรมลงทน")

st.divider()st.markdown("""

1. **ศกษาขอมล:** เรยนรเกยวกบตลาดหนและบรษททสนใจ

st.markdown("<h2><i class='fa-solid fa-list-ol'></i> ขั้นตอนการเริ่มลงทุน</h2>", unsafe_allow_html=True)2. **เปดบญช:** สมครบญชกบโบรกเกอรทมบรการหนตางประเทศ เชน:

st.markdown("""   - บวหลวง Securities (BUALUANG iFin)

1. **<i class='fa-solid fa-graduation-cap'></i> ศึกษาข้อมูล:** เรียนรู้เกี่ยวกับตลาดหุ้นและบริษัทที่สนใจ   - KTB Securities (KT ZMICO)

2. **<i class='fa-solid fa-user-plus'></i> เปิดบัญชี:** สมัครบัญชีกับโบรกเกอร์ที่มีบริการหุ้นต่างประเทศ เช่น:   - Interactive Brokers (สำหรบเงนทนมาก)

   - ธนาคารกรุงเทพ (Bualuang iFin)3. **โอนเงน:** โอนเงนเขาบญชเพอซอหน

   - KTB Securities (KT ZMICO)4. **เลอกหน:** เลอกหนทตองการซอ

   - Interactive Brokers (สำหรับเงินทุนมาก)5. **ซอขาย:** สงซอหนผานแพลตฟอรมของโบรกเกอร

3. **<i class='fa-solid fa-money-bill-transfer'></i> โอนเงิน:** โอนเงินเข้าบัญชีเพื่อซื้อหุ้น6. **ตดตาม:** ตดตามผลการลงทนและขาวสารอยเสมอ

4. **<i class='fa-solid fa-magnifying-glass-chart'></i> เลือกหุ้น:** เลือกหุ้นที่ต้องการซื้อ""")

5. **<i class='fa-solid fa-cart-shopping'></i> ซื้อขาย:** ส่งคำสั่งซื้อหุ้นผ่านแพลตฟอร์มของโบรกเกอร์

6. **<i class='fa-solid fa-chart-simple'></i> ติดตาม:** ติดตามผลการลงทุนและข่าวสารอยู่เสมอst.divider()

""", unsafe_allow_html=True)

st.subheader(" หลกการกระจายความเสยง (Diversification)")

st.divider()st.write("""

อยาลงทนในหนตวเดยว! ควรกระจายเงนลงทนไปในหลายหน หลายประเภทธรกจ และหลายประเทศ

st.markdown("<h2><i class='fa-solid fa-shield-halved'></i> หลักการกระจายความเสี่ยง (Diversification)</h2>", unsafe_allow_html=True)

st.write("""**ตวอยางพอรตโฟลโอแนะนำ:**

อย่าลงทุนในหุ้นตัวเดียว! ควรกระจายเงินลงทุนไปในหลายหุ้น หลายประเภทธุรกิจ และหลายประเทศ- 40% เทคโนโลย (Tech): Apple, Microsoft, Nvidia

- 30% การเงน (Finance): JPMorgan, Berkshire Hathaway

**ตัวอย่างพอร์ตโฟลิโอแนะนำ:**- 20% สขภาพ (Healthcare): Johnson & Johnson, Pfizer

- 40% เทคโนโลยี (Tech): Apple, Microsoft, Nvidia- 10% สนคาอปโภคบรโภค (Consumer): Coca-Cola, Procter & Gamble

- 30% การเงิน (Finance): JPMorgan, Berkshire Hathaway""")

- 20% สุขภาพ (Healthcare): Johnson & Johnson, Pfizer

- 10% สินค้าอุปโภคบริโภค (Consumer): Coca-Cola, Procter & Gamblecol1, col2 = st.columns(2)

""")with col1:

    st.success(" **ทำ:** กระจายความเสยง, ลงทนระยะยาว, ศกษาขอมล")

col1, col2 = st.columns(2)with col2:

with col1:    st.error(" **ไมควรทำ:** ลงทนแบบฟงซาน, ยมเงนมาลงทน, เชอขาวลอ")

    st.success("<i class='fa-solid fa-circle-check'></i> **ทำ:** กระจายความเสี่ยง, ลงทุนระยะยาว, ศึกษาข้อมูล", icon="✅")

with col2:st.divider()

    st.error("<i class='fa-solid fa-circle-xmark'></i> **ไม่ควรทำ:** ลงทุนแบบฟังซาน, ยืมเงินมาลงทุน, เชื่อข่าวลือ", icon="⚠️")

st.info("""

st.divider() **เคลดลบ:** เรมตนดวยการลงทนในกองทน ETF ทตดตามดชน S&P 500 (เชน SPY หรอ VOO)  

เพราะจะชวยใหคณกระจายความเสยงไปยงหนชนนำ 500 บรษทในสหรฐ ในครงเดยว!

st.info("""""")

<i class='fa-solid fa-lightbulb'></i> **เคล็ดลับ:** เริ่มต้นด้วยการลงทุนในกองทุน ETF ที่ติดตามดัชนี S&P 500 (เช่น SPY หรือ VOO)  

เพราะจะช่วยให้คุณกระจายความเสี่ยงไปยังหุ้นชั้นนำ 500 บริษัทในสหรัฐ ในครั้งเดียว!st.markdown("---")

""", icon="💡")st.markdown("""

<div style=''text-align: center; padding: 20px;''>

st.markdown("---")    <p style=''color: #666;''> อานตอ: <a href=''/2_Stock_Data_Analysis'' target=''_self''>วเคราะหขอมลหนแบบเรยลไทม</a></p>

st.markdown("""</div>

<div style='text-align: center; padding: 20px;'>""", unsafe_allow_html=True)

    <p style='color: #666;'><i class='fa-solid fa-arrow-right'></i> อ่านต่อ: <a href='/2_Stock_Data_Analysis' target='_self'>วิเคราะห์ข้อมูลหุ้นแบบเรียลไทม์</a></p>
</div>
""", unsafe_allow_html=True)
