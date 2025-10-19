@echo off
echo ===================================
echo  เริ่มต้น Global Stock App
echo ===================================
echo.

echo กำลังตรวจสอบ Streamlit...
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ไม่พบ Streamlit! 
    echo กรุณารันไฟล์ install_requirements.bat ก่อน
    pause
    exit /b 1
)

echo ✅ เริ่มต้นแอป...
echo.
echo 🌐 เว็บแอปจะเปิดใน Browser อัตโนมัติ
echo 📊 URL: http://localhost:8501
echo.
echo กด Ctrl+C เพื่อปิดแอป
echo.

cd /d "%~dp0"
streamlit run streamlit_app.py