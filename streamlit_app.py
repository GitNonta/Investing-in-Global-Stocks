import streamlit as st

st.set_page_config(page_title="Global Stock Investment", page_icon="🌍", layout="wide")

# Navigation Links
st.markdown("""
<div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 20px;">
    <h4>📖 เนื้อหาทั้งหมด:</h4>
    <p>
        🏠 <strong>หน้าหลัก</strong> | 
        <a href="/1_Basics_of_Investment" target="_self">📘 พื้นฐานการลงทุน</a> | 
        <a href="/2_Stock_Data_Analysis" target="_self">📊 วิเคราะห์ข้อมูลหุ้น</a> | 
        <a href="/3_Forex_and_Risk" target="_self">💱 ค่าเงินและความเสี่ยง</a> | 
        <a href="/4_About_and_Tips" target="_self">💡 เคล็ดลับและแหล่งความรู้</a>
    </p>
</div>
""", unsafe_allow_html=True)

st.title("🌍 Global Stock Investment Guide")
st.subheader("เรียนรู้และวิเคราะห์การลงทุนในหุ้นต่างประเทศ")

st.write("""
ยินดีต้อนรับสู่เว็บแอปการลงทุนในหุ้นต่างประเทศ  
คุณจะได้เรียนรู้ตั้งแต่พื้นฐานของการลงทุน ไปจนถึงการวิเคราะห์ข้อมูลหุ้นจริง  
เหมาะสำหรับผู้เริ่มต้นที่ต้องการเข้าใจตลาดหุ้นโลก เช่น **NASDAQ**, **S&P 500**, **Nikkei**, และอื่น ๆ
""")

# Quick Start Guide
st.markdown("""
### 🚀 เริ่มต้นการเรียนรู้:
1. **[📘 พื้นฐานการลงทุน](/1_Basics_of_Investment)** - เรียนรู้หลักการพื้นฐาน
2. **[📊 วิเคราะห์ข้อมูลหุ้น](/2_Stock_Data_Analysis)** - ลองวิเคราะห์หุ้นจริง
3. **[💱 ค่าเงินและความเสี่ยง](/3_Forex_and_Risk)** - เข้าใจความเสี่ยงและการจัดการ
4. **[💡 เคล็ดลับและแหล่งความรู้](/4_About_and_Tips)** - ทรัพยากรเพิ่มเติม

### 📋 ขั้นตอนที่แนะนำ:
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📘 เริ่มจากพื้นฐาน", use_container_width=True):
        st.switch_page("1_Basics_of_Investment.py")

with col2:
    if st.button("� วิเคราะห์หุ้น", use_container_width=True):
        st.switch_page("2_Stock_Data_Analysis.py")

with col3:
    if st.button("💱 ความเสี่ยง", use_container_width=True):
        st.switch_page("3_Forex_and_Risk.py")

with col4:
    if st.button("💡 เคล็ดลับ", use_container_width=True):
        st.switch_page("4_About_and_Tips.py")

st.info("�👈 หรือใช้เมนูด้านซ้ายเพื่อเลือกหัวข้อการเรียนรู้")
