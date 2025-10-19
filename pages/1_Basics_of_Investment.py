import streamlit as stimport streamlit as st



# Configuration# Navigation Links

st.set_page_config(st.markdown("""

    page_title="Investment Basics - Global Stock Guide", <div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 20px;">

    page_icon="📘",     <h4>📖 เนื้อหาทั้งหมด:</h4>

    layout="wide"    <p>

)        <a href="/" target="_self">🏠 หน้าหลัก</a> | 

        📘 <strong>พื้นฐานการลงทุน</strong> | 

# Add FontAwesome CDN (ต้องอยู่ก่อนเมนูบาร์เสมอ)        <a href="/2_Stock_Data_Analysis" target="_self">📊 วิเคราะห์ข้อมูลหุ้น</a> | 

st.markdown("""        <a href="/3_Forex_and_Risk" target="_self">💱 ค่าเงินและความเสี่ยง</a> | 

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">        <a href="/4_About_and_Tips" target="_self">💡 เคล็ดลับและแหล่งความรู้</a>

""", unsafe_allow_html=True)    </p>

</div>

menu_icons = {""", unsafe_allow_html=True)

    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",

    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",st.header("📘 พื้นฐานการลงทุนในหุ้นต่างประเทศ")

    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",st.write("""

    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",การลงทุนในหุ้นต่างประเทศหมายถึงการซื้อหุ้นของบริษัทที่จดทะเบียนในตลาดหลักทรัพย์นอกประเทศของเรา  

    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"เช่น Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), หรือ Amazon (AMZN)

}

**ข้อดี:**

# Modern Menu Bar (เหมือน streamlit_app.py)- กระจายความเสี่ยงจากเศรษฐกิจในประเทศ  

st.markdown(f"""- เข้าถึงบริษัทระดับโลกที่เติบโตสูง  

<style>- ได้รับผลตอบแทนจากค่าเงิน (ถ้าค่า USD แข็งขึ้น)

.menu-container {{

    position: sticky;**ข้อควรระวัง:**

    top: 0;- ค่าธรรมเนียมการแลกเปลี่ยนเงิน  

    z-index: 100;- ความเสี่ยงจากค่าเงิน (Forex Risk)  

    background: rgba(44,62,80,0.92);- เวลาการซื้อขายต่างจากประเทศไทย

    backdrop-filter: blur(6px);""")

    box-shadow: 0 4px 24px 0 rgba(44,62,80,0.12);

    padding: 0.7rem 0;st.image("https://cdn.pixabay.com/photo/2016/11/22/19/16/stock-exchange-1853266_1280.jpg", caption="Global Market Concept")

    margin: 0 0 1.5rem 0;

    transition: background 0.3s;# Navigation Buttons

}}st.markdown("---")

.menu-nav {{col1, col2, col3 = st.columns([1, 2, 1])

    max-width: 1100px;

    margin: 0 auto;with col1:

    display: flex;    if st.button("🏠 กลับหน้าหลัก", use_container_width=True):

    justify-content: space-between;        st.switch_page("streamlit_app.py")

    align-items: center;

    padding: 0 1.5rem;with col3:

}}    if st.button("ถัดไป: วิเคราะห์ข้อมูล 📊", use_container_width=True):

.logo {{        st.switch_page("pages/2_Stock_Data_Analysis.py")

    font-size: 1.3rem;

    font-weight: bold;st.markdown("""

    color: #fff;### 🎯 พร้อมแล้ว? ไปต่อกันเลย!

    text-decoration: none;ต่อไปเราจะลองวิเคราะห์ข้อมูลหุ้นจริง ๆ โดยใช้ API ฟรี

    display: flex;""")

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
            <a href="/" target="_self" class="menu-item">{menu_icons['home']}หน้าหลัก</a>
            <a href="/1_Basics_of_Investment" target="_self" class="menu-item active">{menu_icons['basics']}พื้นฐานการลงทุน</a>
            <a href="/2_Stock_Data_Analysis" target="_self" class="menu-item">{menu_icons['analysis']}วิเคราะห์หุ้น</a>
            <a href="/3_Forex_and_Risk" target="_self" class="menu-item">{menu_icons['forex']}ความเสี่ยง</a>
            <a href="/4_About_and_Tips" target="_self" class="menu-item">{menu_icons['tips']}เคล็ดลับ</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
            padding: 2rem; 
            border-radius: 15px; 
            margin-bottom: 2rem; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <h1 style="color: white; text-align: center; margin: 0;">
        📘 พื้นฐานการลงทุนในหุ้นต่างประเทศ
    </h1>
    <p style="color: white; text-align: center; font-size: 1.2rem; margin-top: 1rem; opacity: 0.9;">
        เริ่มต้นการเดินทางสู่นักลงทุนระดับโลก
    </p>
</div>
""", unsafe_allow_html=True)

# Main content with images
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## 🌍 หุ้นต่างประเทศคืออะไร?
    
    การลงทุนในหุ้นต่างประเทศหมายถึงการซื้อหุ้นของบริษัทที่จดทะเบียนในตลาดหลักทรัพย์นอกประเทศของเรา  
    
    ### 🏢 ตัวอย่างหุ้นยอดนิยม:
    """)
    
    # Popular stocks examples
    stocks_examples = st.columns(2)
    with stocks_examples[0]:
        st.markdown("""
        **🇺🇸 หุ้นอเมริกา**
        - 🍎 Apple (AAPL) - เทคโนโลยี
        - 🚗 Tesla (TSLA) - รถยนต์ไฟฟ้า  
        - 💻 Microsoft (MSFT) - ซอฟต์แวร์
        - 📦 Amazon (AMZN) - อีคอมเมิร์ซ
        """)
    
    with stocks_examples[1]:
        st.markdown("""
        **🌏 หุ้นเอเชีย**
        - 🛒 Alibaba (BABA) - อีคอมเมิร์ซจีน
        - 🎮 Nintendo (7974.T) - เกมญี่ปุ่น
        - 📱 Samsung (005930.KS) - เทคโนโลยีเกาหลี
        - 🏦 ASML (ASML) - เซมิคอนดักเตอร์
        """)

with col2:
    st.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=500&h=400&fit=crop", 
             caption="📈 Global Stock Markets")

# Benefits and Risks Section
st.markdown("---")
st.subheader("⚖️ ข้อดีและความเสี่ยง")

benefits_risks = st.columns(2)

with benefits_risks[0]:
    st.markdown("""
    ### ✅ ข้อดี
    
    **🌐 การกระจายลงทุน (Diversification)**  
    ลดความเสี่ยงจากการพึ่งพาเศรษฐกิจในประเทศเดียว
    
    **📈 การเติบโตสูง**  
    เข้าถึงบริษัทระดับโลกที่มีการเติบโตรวดเร็ว
    
    **💱 ผลตอบแทนจากค่าเงิน**  
    ได้ประโยชน์เมื่อค่าเงินดอลลาร์แข็งค่า
    
    **🔬 นวัตกรรมใหม่**  
    ลงทุนในเทคโนโลยีและธุรกิจล้ำสมัย
    """)

with benefits_risks[1]:
    st.markdown("""
    ### ⚠️ ความเสี่ยง
    
    **💸 ค่าธรรมเนียม**  
    ค่าแลกเปลี่ยนเงิน, ค่าโอน, ค่าคัสโตเดียน
    
    **📉 ความผันผวนของค่าเงิน**  
    อัตราแลกเปลี่ยนอาจทำให้ขาดทุน
    
    **🕐 เวลาซื้อขาย**  
    ตลาดเปิด-ปิดต่างเวลากับประเทศไทย
    
    **📊 ข้อมูลข่าวสาร**  
    อาจไม่ทันสมัยหรือเข้าถึงยาก
    """)

# Investment Process
st.markdown("---")
st.subheader("🛣️ ขั้นตอนการลงทุน")

st.image("https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&h=300&fit=crop", 
         caption="💡 Investment Strategy Planning")

process_steps = st.columns(4)

steps = [
    {"icon": "🎯", "title": "กำหนดเป้าหมาย", "desc": "ตั้งวัตถุประสงค์และระยะเวลา"},
    {"icon": "💰", "title": "จัดสรรเงินทุน", "desc": "กำหนดงบประมาณที่เสียได้"},
    {"icon": "🏦", "title": "เปิดบัญชี", "desc": "เลือกโบรกเกอร์ที่เหมาะสม"},
    {"icon": "📊", "title": "วิเคราะห์และลงทุน", "desc": "เริ่มซื้อหุ้นที่เลือก"}
]

for i, step in enumerate(steps):
    with process_steps[i]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #4CAF50dd, #4CAF5099);
            padding: 1.5rem; 
            border-radius: 12px; 
            text-align: center;
            margin: 0.5rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        ">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{step['icon']}</div>
            <h4 style="color: white; margin: 0;">{step['title']}</h4>
            <p style="color: white; opacity: 0.9; font-size: 0.9rem; margin: 0.5rem 0;">
                {step['desc']}
            </p>
        </div>
        """, unsafe_allow_html=True)

# Key Terms
st.markdown("---")
st.subheader("📖 คำศัพท์สำคัญ")

terms_cols = st.columns(2)

with terms_cols[0]:
    st.markdown("""
    ### 💹 คำศัพท์พื้นฐาน
    
    **📈 Bull Market** - ตลาดขาขึ้น (ราคาหุ้นเพิ่มขึ้นต่อเนื่อง)  
    **📉 Bear Market** - ตลาดขาลง (ราคาหุ้นลดลงต่อเนื่อง)  
    **💰 Dividend** - เงินปันผล  
    **📊 P/E Ratio** - อัตราส่วนราคาต่อกำไร  
    **📋 Portfolio** - พอร์ตลงทุน  
    **🎯 Market Cap** - มูลค่าตลาด  
    """)

with terms_cols[1]:
    st.markdown("""
    ### 🌐 คำศัพท์ต่างประเทศ
    
    **💱 Forex Risk** - ความเสี่ยงจากอัตราแลกเปลี่ยน  
    **🏦 Custodian** - ผู้ดูแลหลักทรัพย์  
    **📄 ADR** - American Depositary Receipt  
    **🏛️ NYSE** - New York Stock Exchange  
    **💻 NASDAQ** - National Association of Securities Dealers Automated Quotations  
    **⏰ After Hours** - การซื้อขายนอกเวลา  
    """)

# Tips for beginners
st.markdown("---")
st.info("""
### 💡 เคล็ดลับสำหรับมือใหม่

🔸 **เริ่มต้นด้วยจำนวนเงินที่เสียได้** - อย่าใช้เงินที่จำเป็นต่อการใช้ชีวิต  
🔸 **ศึกษาบริษัทก่อนลงทุน** - อ่านงบการเงิน, ข่าว, แนวโน้มธุรกิจ  
🔸 **กระจายการลงทุน** - อย่าใส่ไข่ไว้ในตะกร้าใบเดียว  
🔸 **ลงทุนระยะยาว** - หุ้นดีมักให้ผลตอบแทนดีในระยะยาว  
🔸 **ติดตามข่าวสารอย่างสม่ำเสมอ** - โลกการเงินเปลี่ยนแปลงรวดเร็ว  
""")

# Navigation Buttons
st.markdown("---")
navigation_cols = st.columns([1, 3, 1])

with navigation_cols[0]:
    if st.button("🏠 กลับหน้าหลัก", use_container_width=True, type="secondary"):
        st.switch_page("streamlit_app.py")

with navigation_cols[2]:
    if st.button("ถัดไป: วิเคราะห์ข้อมูลหุ้น 📊", use_container_width=True, type="primary"):
        st.switch_page("pages/2_Stock_Data_Analysis.py")

# Call to action
st.success("🎯 **พร้อมแล้ว?** มาลองใช้เครื่องมือวิเคราะห์ข้อมูลหุ้นแบบเรียลไทม์กันเลย!")

# Footer
st.markdown("""
---
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>⚠️ <strong>คำเตือน:</strong> ข้อมูลนี้เป็นเพียงการศึกษาเท่านั้น ไม่ใช่คำแนะนำในการลงทุน</p>
</div>
""", unsafe_allow_html=True)
