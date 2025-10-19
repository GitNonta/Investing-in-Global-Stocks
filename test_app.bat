@echo off
echo ===============================
echo  ทดสอบ Global Stocks App
echo ===============================
echo.

echo ตรวจสอบโครงสร้างไฟล์...
if not exist "streamlit_app.py" (
    echo ❌ ไม่พบ streamlit_app.py
    pause
    exit /b 1
)

if not exist "1_Basics_of_Investment.py" (
    echo ❌ ไม่พบ 1_Basics_of_Investment.py
    pause
    exit /b 1
)

if not exist "2_Stock_Data_Analysis.py" (
    echo ❌ ไม่พบ 2_Stock_Data_Analysis.py
    pause
    exit /b 1
)

if not exist "3_Forex_and_Risk.py" (
    echo ❌ ไม่พบ 3_Forex_and_Risk.py
    pause
    exit /b 1
)

if not exist "4_About_and_Tips.py" (
    echo ❌ ไม่พบ 4_About_and_Tips.py
    pause
    exit /b 1
)

if exist "pages" (
    echo ⚠️ พบโฟลเดอร์ pages! กำลังลบ...
    rmdir /s /q "pages"
)

echo ✅ โครงสร้างไฟล์ถูกต้อง
echo.

echo ตรวจสอบ Python และ Streamlit...
python --version
if errorlevel 1 (
    echo ❌ ไม่พบ Python
    pause
    exit /b 1
)

python -c "import streamlit; print('Streamlit:', streamlit.__version__)"
if errorlevel 1 (
    echo ❌ ไม่พบ Streamlit กรุณาติดตั้งก่อน
    echo pip install streamlit
    pause
    exit /b 1
)

echo ✅ Python และ Streamlit พร้อมใช้งาน
echo.

echo เริ่มต้นแอป...
echo 🌐 กำลังเปิด http://localhost:8501
echo กด Ctrl+C เพื่อปิดแอป
echo.

streamlit run streamlit_app.py