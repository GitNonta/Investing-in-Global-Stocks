import streamlit as st

# Configuration
st.set_page_config(
    page_title="Tips & Resources - Global Stock Guide", 
    page_icon="", 
    layout="wide"
)

# Add FontAwesome CDN
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
""", unsafe_allow_html=True)

# Modern Menu Bar with FontAwesome icons
menu_icons = {
    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",
    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",
    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",
    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",
    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"
}

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
</style>

<div class="menu-container">
    <div class="menu-nav">
        <a href="/" target="_self" class="logo"><i class='fa-solid fa-globe'></i>&nbsp;Global Stocks</a>
        <div class="menu-items">
            <a href="/" target="_self" class="menu-item">{menu_icons['home']}หนาหลก</a>
            <a href="1_Basics_of_Investment" target="_self" class="menu-item">{menu_icons['basics']}พนฐานการลงทน</a>
            <a href="2_Stock_Data_Analysis" target="_self" class="menu-item">{menu_icons['analysis']}วเคราะหหน</a>
            <a href="3_Forex_and_Risk" target="_self" class="menu-item">{menu_icons['forex']}ความเสยง</a>
            <a href="4_About_and_Tips" target="_self" class="menu-item active">{menu_icons['tips']}เคลดลบ</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.header(" เคลดลบและแหลงความร")
st.success(" จบเนอหาการเรยนร  ยนดดวย!")

# Tips Section
st.subheader(" เคลดลบสำคญในการลงทนหนตางประเทศ")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ###  ควรทำ (DO)
    1. **กระจายความเสยง** - อยาลงทนในหนตวเดยว
    2. **ลงทนระยะยาว** - อดทนและรอผลตอบแทน
    3. **ศกษาขอมล** - อานรายงานและขาวสารอยเสมอ
    4. **ตงเปาหมาย** - รวาเราลงทนเพออะไร
    5. **ใช DCA** - ลงทนเปนงวด ลดความเสยง
    6. **ควบคมอารมณ** - อยาตนตระหนกเมอราคาผนผวน
    """)

with col2:
    st.markdown("""
    ###  ไมควรทำ (DON'T)
    1. **ยมเงนมาลงทน** - อยาใชเงนทไมใชเงนเกบ
    2. **ฟงซาน** - อยาเชอคำแนะนำทไมมทมา
    3. **ลงทนแบบลง** - อยาซอหนทไมเขาใจ
    4. **ซอขายบอย** - คาธรรมเนยมจะกดกนกำไร
    5. **โลภมาก** - อยากรวยเรวมกขาดทน
    6. **ละเลยความเสยง** - ตองเขาใจความเสยงกอนลงทน
    """)

st.divider()

# Resources Section
st.subheader(" แหลงความรเพมเตม")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ###  YouTube Channels
    - **The Motley Fool**
    - **Ben Felix**
    - **Graham Stephan**
    - **Bloomberg Markets**
    """)

with col2:
    st.markdown("""
    ###  Podcasts
    - **Chat with Traders**
    - **The Investors Podcast**
    - **Planet Money**
    - **MarketWatch**
    """)

with col3:
    st.markdown("""
    ###  Books
    - **The Intelligent Investor**
    - **A Random Walk Down Wall Street**
    - **The Little Book of Common Sense Investing**
    - **Rich Dad Poor Dad**
    """)

st.divider()

# Thai Resources
st.subheader(" แหลงความรภาษาไทย")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ###  เวบไซตและแอพ
    - **[SET.or.th](https://www.set.or.th)**
    - **Finanseer**
    - **The Secret Sauce**
    - **Finnomena**
    """)

with col2:
    st.markdown("""
    ###  โบรกเกอรในไทย
    - **Bualuang Securities**
    - **KTB Securities**
    - **Phillip Securities**
    - **Interactive Brokers**
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
