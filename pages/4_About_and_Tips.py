import streamlit as st

# Configuration
st.set_page_config(
    page_title="Tips & Resources - Global Stock Guide", 
    page_icon="💡", 
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




menu_icons = {
    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",
    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",
    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",
    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",
    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"
}


""", unsafe_allow_html=True)
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
        <a href="/" class="logo"><i class='fa-solid fa-globe'></i>&nbsp;Global Stocks</a>
        <input type="checkbox" id="menu-toggle" style="display:none;" />
        <label class="menu-hamburger" for="menu-toggle">
            <span></span>
            <span></span>
            <span></span>
        </label>
        <div class="menu-items">
            <a href="/" class="menu-item">{menu_icons['home']}หน้าหลัก</a>
            <a href="/1_Basics_of_Investment" class="menu-item">{menu_icons['basics']}พื้นฐานการลงทุน</a>
            <a href="/2_Stock_Data_Analysis" class="menu-item">{menu_icons['analysis']}วิเคราะห์หุ้น</a>
            <a href="/3_Forex_and_Risk" class="menu-item">{menu_icons['forex']}ความเสี่ยง</a>
            <a href="/4_About_and_Tips" class="menu-item active">{menu_icons['tips']}เคล็ดลับ</a>
        </div>
    </div>

st.success("จบเนื้อหาการเรียนรู้ — ยินดีด้วย! 🎉")

# Additional Resources
st.markdown("""
### 📚 แหล่งความรู้เพิ่มเติม
- **YouTube Channel:** The Motley Fool, Ben Felix
- **Podcast:** Chat with Traders, The Investors Podcast
- **Books:** "The Intelligent Investor", "A Random Walk Down Wall Street"
- **Thai Resources:** [SET.or.th](https://www.set.or.th), Finanseer, The Secret Sauce
""", unsafe_allow_html=True)

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("← ก่อนหน้า: ความเสี่ยง", use_container_width=True):
        st.switch_page("3_Forex_and_Risk.py")

with col2:
    if st.button("🏠 กลับหน้าหลัก", use_container_width=True):
        st.switch_page("streamlit_app.py")

with col3:
    if st.button("🔄 เริ่มใหม่", use_container_width=True):
        st.switch_page("1_Basics_of_Investment.py")

st.markdown("""
---
### <i class='fa-solid fa-bullseye'></i> ขั้นตอนต่อไป:
1. เปิดบัญชีลงทุนกับโบรกเกอร์ที่มีบริการซื้อหุ้นต่างประเทศ
2. เริ่มต้นด้วยเงินจำนวนน้อย
3. ฝึกติดตามข่าวสารและวิเคราะห์หุ้น
4. สร้างพอร์ตโฟลิโอที่กระจายความเสี่ยง

**สำคัญ:** ข้อมูลในเว็บไซต์นี้เป็นเพียงการศึกษาเท่านั้น ไม่ใช่คำแนะนำในการลงทุน
""", unsafe_allow_html=True)
