import streamlit as stimport streamlit as st



# Configuration# Configuration

st.set_page_config(st.set_page_config(

    page_title="Tips & Resources - Global Stock Guide",     page_title="Tips & Resources - Global Stock Guide", 

    page_icon="💡",     page_icon="", 

    layout="wide"    layout="wide"

))



menu_icons = {# Add FontAwesome CDN

    "home": "<img src='https://cdn-icons-png.flaticon.com/512/1946/1946436.png' width='20' style='vertical-align:middle;margin-right:6px;'>",st.markdown("""

    "basics": "<img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='20' style='vertical-align:middle;margin-right:6px;'>",<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">

    "analysis": "<img src='https://cdn-icons-png.flaticon.com/512/2721/2721297.png' width='20' style='vertical-align:middle;margin-right:6px;'>",""", unsafe_allow_html=True)

    "forex": "<img src='https://cdn-icons-png.flaticon.com/512/3135/3135706.png' width='20' style='vertical-align:middle;margin-right:6px;'>",

    "tips": "<img src='https://cdn-icons-png.flaticon.com/512/1828/1828884.png' width='20' style='vertical-align:middle;margin-right:6px;'>"# Modern Menu Bar with FontAwesome icons

}menu_icons = {

    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",

# Modern Menu Bar    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",

st.markdown(f"""    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",

<style>    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",

.menu-container {{background: linear-gradient(90deg, #2C3E50 0%, #3498DB 50%, #9B59B6 100%);padding: 0.8rem 0;margin: -1rem -1rem 2rem -1rem;box-shadow: 0 2px 10px rgba(0,0,0,0.1);position: sticky;top: 0;z-index: 999;}}    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"

.menu-nav {{max-width: 1200px;margin: 0 auto;display: flex;justify-content: space-between;align-items: center;padding: 0 2rem;}}}

.logo {{font-size: 1.5rem;font-weight: bold;color: white;text-decoration: none;}}

.menu-items {{display: flex;gap: 2rem;align-items: center;}}st.markdown(f"""

.menu-item {{color: white;text-decoration: none;padding: 0.5rem 1rem;border-radius: 20px;transition: all 0.3s ease;font-weight: 500;font-size: 0.95rem;display: flex;align-items: center;}}<style>

.menu-item:hover {{background: rgba(255,255,255,0.2);color: white;transform: translateY(-2px);text-decoration: none;}}.menu-container {{

.menu-item.active {{background: rgba(255,255,255,0.3);color: white;}}    position: sticky;

.menu-icon {{margin-right: 0.5rem;}}    top: 0;

@media (max-width: 768px) {{.menu-nav {{flex-direction: column;padding: 1rem;}}.menu-items {{margin-top: 1rem;flex-wrap: wrap;gap: 1rem;}}}}    z-index: 100;

</style>    background: rgba(44,62,80,0.92);

    backdrop-filter: blur(6px);

<div class="menu-container">    box-shadow: 0 4px 24px 0 rgba(44,62,80,0.12);

    <div class="menu-nav">    padding: 0.7rem 0;

        <a href="/" target="_self" class="logo">🌍 Global Stocks</a>    margin: 0 0 1.5rem 0;

        <div class="menu-items">    transition: background 0.3s;

            <a href="/" target="_self" class="menu-item">{menu_icons['home']}หน้าหลัก</a>}}

            <a href="1_Basics_of_Investment" target="_self" class="menu-item">{menu_icons['basics']}พื้นฐานการลงทุน</a>.menu-nav {{

            <a href="2_Stock_Data_Analysis" target="_self" class="menu-item">{menu_icons['analysis']}วิเคราะห์หุ้น</a>    max-width: 1100px;

            <a href="3_Forex_and_Risk" target="_self" class="menu-item">{menu_icons['forex']}ความเสี่ยง</a>    margin: 0 auto;

            <a href="4_About_and_Tips" target="_self" class="menu-item active">{menu_icons['tips']}เคล็ดลับ</a>    display: flex;

        </div>    justify-content: space-between;

    </div>    align-items: center;

</div>    padding: 0 1.5rem;

""", unsafe_allow_html=True)}}

.logo {{

st.header("💡 เคล็ดลับและแหล่งความรู้")    font-size: 1.3rem;

st.success("🎉 จบเนื้อหาการเรียนรู้ — ยินดีด้วย!")    font-weight: bold;

    color: #fff;

# Tips Section    text-decoration: none;

st.subheader("💎 เคล็ดลับสำคัญในการลงทุนหุ้นต่างประเทศ")    display: flex;

    align-items: center;

col1, col2 = st.columns(2)    letter-spacing: 1px;

    transition: transform 0.2s;

with col1:}}

    st.markdown(""".logo:hover {{

    ### ✅ ควรทำ (DO)    transform: scale(1.07) rotate(-2deg);

    1. **กระจายความเสี่ยง** - อย่าลงทุนในหุ้นตัวเดียว    color: #ffd700;

    2. **ลงทุนระยะยาว** - อดทนและรอผลตอบแทน}}

    3. **ศึกษาข้อมูล** - อ่านรายงานและข่าวสารอยู่เสมอ.menu-items {{

    4. **ตั้งเป้าหมาย** - รู้ว่าเราลงทุนเพื่ออะไร    display: flex;

    5. **ใช้ DCA** - ลงทุนเป็นงวดๆ ลดความเสี่ยง    gap: 1.2rem;

    6. **ควบคุมอารมณ์** - อย่าตื่นตระหนกเมื่อราคาผันผวน    align-items: center;

    """)    transition: gap 0.2s;

}}

with col2:.menu-item {{

    st.markdown("""    color: #fff;

    ### ❌ ไม่ควรทำ (DON'T)    text-decoration: none;

    1. **ยืมเงินมาลงทุน** - อย่าใช้เงินที่ไม่ใช่เงินเก็บ    padding: 0.35rem 1.1rem;

    2. **ฟังซาน** - อย่าเชื่อคำแนะนำที่ไม่มีที่มา    border-radius: 18px;

    3. **ลงทุนแบบลิง** - อย่าซื้อหุ้นที่ไม่เข้าใจ    font-weight: 500;

    4. **ซื้อขายบ่อย** - ค่าธรรมเนียมจะกัดกินกำไร    font-size: 1.05rem;

    5. **โลภมาก** - อยากรวยเร็วมักขาดทุน    display: flex;

    6. **ละเลยความเสี่ยง** - ต้องเข้าใจความเสี่ยงก่อนลงทุน    align-items: center;

    """)    position: relative;

    transition: background 0.18s, color 0.18s, transform 0.18s;

st.divider()    overflow: hidden;

}}

# Resources Section.menu-item .fa-solid {{

st.subheader("📚 แหล่งความรู้เพิ่มเติม")    transition: transform 0.25s cubic-bezier(.68,-0.55,.27,1.55), color 0.18s;

}}

col1, col2, col3 = st.columns(3).menu-item:hover .fa-solid {{

    transform: scale(1.18) rotate(-10deg);

with col1:    color: #ffd700;

    st.markdown("""}}

    ### 📺 YouTube Channels.menu-item:hover {{

    - **The Motley Fool**    background: #3b4a5a;

    - **Ben Felix**    color: #ffd700;

    - **Graham Stephan**    transform: translateY(-2px) scale(1.04);

    - **Bloomberg Markets**    box-shadow: 0 2px 8px 0 rgba(44,62,80,0.10);

    """)}}

.menu-item.active {{

with col2:    background: linear-gradient(90deg, #667eea 60%, #764ba2 100%);

    st.markdown("""    color: #fff;

    ### 🎙️ Podcasts    box-shadow: 0 2px 12px 0 rgba(102,126,234,0.10);

    - **Chat with Traders**    font-weight: 700;

    - **The Investors Podcast**}}

    - **Planet Money**.menu-item.active .fa-solid {{

    - **MarketWatch**    color: #ffd700;

    """)}}

</style>

with col3:

    st.markdown("""<div class="menu-container">

    ### 📖 Books    <div class="menu-nav">

    - **The Intelligent Investor**        <a href="/" target="_self" class="logo"><i class='fa-solid fa-globe'></i>&nbsp;Global Stocks</a>

    - **A Random Walk Down Wall Street**        <div class="menu-items">

    - **The Little Book of Common Sense Investing**            <a href="/" target="_self" class="menu-item">{menu_icons['home']}หนาหลก</a>

    - **Rich Dad Poor Dad**            <a href="1_Basics_of_Investment" target="_self" class="menu-item">{menu_icons['basics']}พนฐานการลงทน</a>

    """)            <a href="2_Stock_Data_Analysis" target="_self" class="menu-item">{menu_icons['analysis']}วเคราะหหน</a>

            <a href="3_Forex_and_Risk" target="_self" class="menu-item">{menu_icons['forex']}ความเสยง</a>

st.divider()            <a href="4_About_and_Tips" target="_self" class="menu-item active">{menu_icons['tips']}เคลดลบ</a>

        </div>

# Thai Resources    </div>

st.subheader("🇹🇭 แหล่งความรู้ภาษาไทย")</div>

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

st.header(" เคลดลบและแหลงความร")

with col1:st.success(" จบเนอหาการเรยนร  ยนดดวย!")

    st.markdown("""

    ### 📱 เว็บไซต์และแอพ# Tips Section

    - **[SET.or.th](https://www.set.or.th)**st.subheader(" เคลดลบสำคญในการลงทนหนตางประเทศ")

    - **Finanseer**

    - **The Secret Sauce**col1, col2 = st.columns(2)

    - **Finnomena**

    """)with col1:

    st.markdown("""

with col2:    ###  ควรทำ (DO)

    st.markdown("""    1. **กระจายความเสยง** - อยาลงทนในหนตวเดยว

    ### 📊 โบรกเกอร์ในไทย    2. **ลงทนระยะยาว** - อดทนและรอผลตอบแทน

    - **Bualuang Securities**    3. **ศกษาขอมล** - อานรายงานและขาวสารอยเสมอ

    - **KTB Securities**    4. **ตงเปาหมาย** - รวาเราลงทนเพออะไร

    - **Phillip Securities**    5. **ใช DCA** - ลงทนเปนงวด ลดความเสยง

    - **Interactive Brokers**    6. **ควบคมอารมณ** - อยาตนตระหนกเมอราคาผนผวน

    """)    """)



st.divider()with col2:

    st.markdown("""

# Investment Tools    ###  ไมควรทำ (DON'T)

st.subheader("🛠️ เครื่องมือที่มีประโยชน์")    1. **ยมเงนมาลงทน** - อยาใชเงนทไมใชเงนเกบ

    2. **ฟงซาน** - อยาเชอคำแนะนำทไมมทมา

col1, col2, col3 = st.columns(3)    3. **ลงทนแบบลง** - อยาซอหนทไมเขาใจ

    4. **ซอขายบอย** - คาธรรมเนยมจะกดกนกำไร

with col1:    5. **โลภมาก** - อยากรวยเรวมกขาดทน

    st.info("""    6. **ละเลยความเสยง** - ตองเขาใจความเสยงกอนลงทน

    **📈 การวิเคราะห์**    """)

    - Yahoo Finance

    - TradingViewst.divider()

    - Investing.com

    """)# Resources Section

st.subheader(" แหลงความรเพมเตม")

with col2:

    st.info("""col1, col2, col3 = st.columns(3)

    **📰 ข่าวสาร**

    - Bloombergwith col1:

    - Reuters    st.markdown("""

    - CNBC    ###  YouTube Channels

    """)    - **The Motley Fool**

    - **Ben Felix**

with col3:    - **Graham Stephan**

    st.info("""    - **Bloomberg Markets**

    **💰 คำนวณ**    """)

    - Dividend Calculator

    - Compound Interestwith col2:

    - Portfolio Visualizer    st.markdown("""

    """)    ###  Podcasts

    - **Chat with Traders**

st.divider()    - **The Investors Podcast**

    - **Planet Money**

# Next Steps    - **MarketWatch**

st.subheader("🎯 ขั้นตอนต่อไป:")    """)

st.markdown("""

1. **เปิดบัญชีลงทุน** กับโบรกเกอร์ที่มีบริการซื้อหุ้นต่างประเทศwith col3:

2. **เริ่มต้นด้วยเงินจำนวนน้อย** เพื่อทดลองและเรียนรู้    st.markdown("""

3. **ฝึกติดตามข่าวสาร** และวิเคราะห์หุ้นที่สนใจ    ###  Books

4. **สร้างพอร์ตโฟลิโอ** ที่กระจายความเสี่ยง    - **The Intelligent Investor**

    - **A Random Walk Down Wall Street**

⚠️ **สำคัญ:** ข้อมูลในเว็บไซต์นี้เป็นเพียงการศึกษาเท่านั้น **ไม่ใช่คำแนะนำในการลงทุน**    - **The Little Book of Common Sense Investing**

""")    - **Rich Dad Poor Dad**

    """)

# Navigation Buttons

st.markdown("---")st.divider()

col1, col2, col3 = st.columns([1, 2, 1])

# Thai Resources

with col1:st.subheader(" แหลงความรภาษาไทย")

    if st.button("← ก่อนหน้า: ความเสี่ยง", use_container_width=True):

        st.switch_page("pages/3_Forex_and_Risk.py")col1, col2 = st.columns(2)



with col2:with col1:

    if st.button("🏠 กลับหน้าหลัก", use_container_width=True):    st.markdown("""

        st.switch_page("streamlit_app.py")    ###  เวบไซตและแอพ

    - **[SET.or.th](https://www.set.or.th)**

with col3:    - **Finanseer**

    if st.button("🔄 เริ่มใหม่", use_container_width=True):    - **The Secret Sauce**

        st.switch_page("pages/1_Basics_of_Investment.py")    - **Finnomena**

    """)

st.markdown("---")

st.markdown("""with col2:

<div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>    st.markdown("""

    <h3>🌟 ขอบคุณที่ใช้ Global Stock Investment Guide! 🌟</h3>    ###  โบรกเกอรในไทย

    <p>สร้างด้วย ❤️ เพื่อการเรียนรู้การลงทุนหุ้นต่างประเทศ</p>    - **Bualuang Securities**

    <p><em>Happy Investing! 📈💰</em></p>    - **KTB Securities**

</div>    - **Phillip Securities**

""", unsafe_allow_html=True)    - **Interactive Brokers**

    """)

st.divider()

# Next Steps
st.subheader(" ขนตอนตอไป:")
st.markdown("""
1. **เปดบญชลงทน** กบโบรกเกอรทมบรการซอหนตางประเทศ
2. **เรมตนดวยเงนจำนวนนอย** เพอทดลองและเรยนร
3. **ฝกตดตามขาวสาร** และวเคราะหหนทสนใจ
4. **สรางพอรตโฟลโอ** ทกระจายความเสยง

 **สำคญ:** ขอมลในเวบไซตนเปนเพยงการศกษาเทานน **ไมใชคำแนะนำในการลงทน**
""")

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button(" กอนหนา: ความเสยง", use_container_width=True):
        st.switch_page("pages/3_Forex_and_Risk.py")

with col2:
    if st.button(" กลบหนาหลก", use_container_width=True):
        st.switch_page("streamlit_app.py")

with col3:
    if st.button(" เรมใหม", use_container_width=True):
        st.switch_page("pages/1_Basics_of_Investment.py")

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
    <h3> ขอบคณทใช Global Stock Investment Guide! </h3>
    <p>สรางดวย  เพอการเรยนรการลงทนหนตางประเทศ</p>
    <p><em>Happy Investing! </em></p>
</div>
""", unsafe_allow_html=True)
