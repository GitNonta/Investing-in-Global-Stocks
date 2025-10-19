import streamlit as st

# Navigation Links
st.markdown("""
<div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 20px;">
    <h4>📖 เนื้อหาทั้งหมด:</h4>
    <p>
        <a href="/" target="_self">🏠 หน้าหลัก</a> | 
        <a href="/1_Basics_of_Investment" target="_self">📘 พื้นฐานการลงทุน</a> | 
        <a href="/2_Stock_Data_Analysis" target="_self">📊 วิเคราะห์ข้อมูลหุ้น</a> | 
        💱 <strong>ค่าเงินและความเสี่ยง</strong> | 
        <a href="/4_About_and_Tips" target="_self">💡 เคล็ดลับและแหล่งความรู้</a>
    </p>
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
