import streamlit as st

# Configuration
st.set_page_config(
    page_title="Forex & Risk - Global Stock Guide", 
    page_icon="💱", 
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
.menu-container {background: linear-gradient(90deg, #2C3E50 0%, #3498DB 50%, #9B59B6 100%);padding: 0.8rem 0;margin: -1rem -1rem 2rem -1rem;box-shadow: 0 2px 10px rgba(0,0,0,0.1);position: sticky;top: 0;z-index: 999;}
.menu-nav {max-width: 1200px;margin: 0 auto;display: flex;justify-content: space-between;align-items: center;padding: 0 2rem;}
.logo {font-size: 1.5rem;font-weight: bold;color: white;text-decoration: none;}
.menu-items {display: flex;gap: 2rem;align-items: center;}
.menu-item {color: white;text-decoration: none;padding: 0.5rem 1rem;border-radius: 20px;transition: all 0.3s ease;font-weight: 500;font-size: 0.95rem;display: flex;align-items: center;}
.menu-item:hover {background: rgba(255,255,255,0.2);color: white;transform: translateY(-2px);text-decoration: none;}
.menu-item.active {background: rgba(255,255,255,0.3);color: white;}
.menu-icon {margin-right: 0.5rem;}
@media (max-width: 768px) {.menu-nav {flex-direction: column;padding: 1rem;}.menu-items {margin-top: 1rem;flex-wrap: wrap;gap: 1rem;}}
</style>

<div class="menu-container">
    <div class="menu-nav">
        <a href="/" class="logo">🌍 Global Stocks</a>
        <div class="menu-items">
            <a href="/" class="menu-item">{menu_icons['home']}หน้าหลัก</a>
            <a href="/1_Basics_of_Investment" class="menu-item">{menu_icons['basics']}พื้นฐานการลงทุน</a>
            <a href="/2_Stock_Data_Analysis" class="menu-item">{menu_icons['analysis']}วิเคราะห์หุ้น</a>
            <a href="/3_Forex_and_Risk" class="menu-item active">{menu_icons['forex']}ความเสี่ยง</a>
            <a href="/4_About_and_Tips" class="menu-item">{menu_icons['tips']}เคล็ดลับ</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



st.header("💱 ค่าเงินและความเสี่ยงในการลงทุนต่างประเทศ")
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
st.markdown("### 🧮 คำนวณความเสี่ยงค่าเงิน")
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
        st.switch_page("2_Stock_Data_Analysis.py")

with col3:
    if st.button("ถัดไป: เคล็ดลับ →", use_container_width=True):
        st.switch_page("4_About_and_Tips.py")
