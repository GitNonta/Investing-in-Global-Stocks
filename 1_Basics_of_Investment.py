import streamlit as st

# Navigation Links
st.markdown("""
<div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 20px;">
    <h4>📖 เนื้อหาทั้งหมด:</h4>
    <p>
        <a href="/" target="_self">🏠 หน้าหลัก</a> | 
        📘 <strong>พื้นฐานการลงทุน</strong> | 
        <a href="/2_Stock_Data_Analysis" target="_self">📊 วิเคราะห์ข้อมูลหุ้น</a> | 
        <a href="/3_Forex_and_Risk" target="_self">💱 ค่าเงินและความเสี่ยง</a> | 
        <a href="/4_About_and_Tips" target="_self">💡 เคล็ดลับและแหล่งความรู้</a>
    </p>
</div>
""", unsafe_allow_html=True)

st.header("📘 พื้นฐานการลงทุนในหุ้นต่างประเทศ")
st.write("""
การลงทุนในหุ้นต่างประเทศหมายถึงการซื้อหุ้นของบริษัทที่จดทะเบียนในตลาดหลักทรัพย์นอกประเทศของเรา  
เช่น Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), หรือ Amazon (AMZN)

**ข้อดี:**
- กระจายความเสี่ยงจากเศรษฐกิจในประเทศ  
- เข้าถึงบริษัทระดับโลกที่เติบโตสูง  
- ได้รับผลตอบแทนจากค่าเงิน (ถ้าค่า USD แข็งขึ้น)

**ข้อควรระวัง:**
- ค่าธรรมเนียมการแลกเปลี่ยนเงิน  
- ความเสี่ยงจากค่าเงิน (Forex Risk)  
- เวลาการซื้อขายต่างจากประเทศไทย
""")

st.image("https://cdn.pixabay.com/photo/2016/11/22/19/16/stock-exchange-1853266_1280.jpg", caption="Global Market Concept")

# Navigation Buttons
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("🏠 กลับหน้าหลัก", use_container_width=True):
        st.switch_page("streamlit_app.py")

with col3:
    if st.button("ถัดไป: วิเคราะห์ข้อมูล 📊", use_container_width=True):
        st.switch_page("2_Stock_Data_Analysis.py")

st.markdown("""
### 🎯 พร้อมแล้ว? ไปต่อกันเลย!
ต่อไปเราจะลองวิเคราะห์ข้อมูลหุ้นจริง ๆ โดยใช้ API ฟรี
""")
