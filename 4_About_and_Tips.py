import streamlit as st

# Navigation Links
st.markdown("""
<div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 20px;">
    <h4>📖 เนื้อหาทั้งหมด:</h4>
    <p>
        <a href="/" target="_self">🏠 หน้าหลัก</a> | 
        <a href="/1_Basics_of_Investment" target="_self">📘 พื้นฐานการลงทุน</a> | 
        <a href="/2_Stock_Data_Analysis" target="_self">📊 วิเคราะห์ข้อมูลหุ้น</a> | 
        <a href="/3_Forex_and_Risk" target="_self">💱 ค่าเงินและความเสี่ยง</a> | 
        💡 <strong>เคล็ดลับและแหล่งความรู้</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.header("💡 แหล่งความรู้และเคล็ดลับ")
st.write("""
**เว็บไซต์ที่ควรติดตาม:**
- [Yahoo Finance](https://finance.yahoo.com)
- [Investing.com](https://www.investing.com)
- [Morningstar](https://www.morningstar.com)
- [TradingView](https://www.tradingview.com)

**เคล็ดลับสำหรับนักลงทุนใหม่:**
- เริ่มจากเงินน้อย ๆ และลงทุนสม่ำเสมอ  
- ศึกษาบริษัทก่อนซื้อทุกครั้ง  
- อย่า Panic เมื่อราคาผันผวน  
- คิดระยะยาวมากกว่าระยะสั้น
""")

st.success("จบเนื้อหาการเรียนรู้ — ยินดีด้วย! 🎉")

# Additional Resources
st.markdown("### 📚 แหล่งความรู้เพิ่มเติม")
st.markdown("""
- **YouTube Channel:** The Motley Fool, Ben Felix
- **Podcast:** Chat with Traders, The Investors Podcast
- **Books:** "The Intelligent Investor", "A Random Walk Down Wall Street"
- **Thai Resources:** [SET.or.th](https://www.set.or.th), Finanseer, The Secret Sauce
""")

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
### 🎯 ขั้นตอนต่อไป:
1. เปิดบัญชีลงทุนกับโบรกเกอร์ที่มีบริการซื้อหุ้นต่างประเทศ
2. เริ่มต้นด้วยเงินจำนวนน้อย
3. ฝึกติดตามข่าวสารและวิเคราะห์หุ้น
4. สร้างพอร์ตโฟลิโอที่กระจายความเสี่ยง

**สำคัญ:** ข้อมูลในเว็บไซต์นี้เป็นเพียงการศึกษาเท่านั้น ไม่ใช่คำแนะนำในการลงทุน
""")
