@echo off
echo ===================================
echo  Global Stock App - Library Installer
echo ===================================
echo.

echo กำลังตรวจสอบ Python...
python --version
if errorlevel 1 (
    echo ❌ ไม่พบ Python! กรุณาติดตั้ง Python ก่อน
    echo ดาวน์โหลดจาก: https://python.org
    pause
    exit /b 1
)

echo.
echo กำลังอัพเกรด pip...
python -m pip install --upgrade pip

echo.
echo กำลังติดตั้งไลบรารีที่จำเป็น...
echo.

echo [1/6] ติดตั้ง Streamlit...
pip install streamlit>=1.28.0

echo [2/6] ติดตั้ง Pandas...
pip install pandas>=2.0.0

echo [3/6] ติดตั้ง Requests...
pip install requests>=2.31.0

echo [4/6] ติดตั้ง NumPy...
pip install numpy>=1.24.0

echo [5/6] ติดตั้ง Plotly...
pip install plotly>=5.15.0

echo [6/6] ติดตั้ง yfinance...
pip install yfinance>=0.2.18

echo.
echo ===================================
echo ✅ ติดตั้งเสร็จสิ้น!
echo ===================================
echo.
echo วิธีรันแอป:
echo   cd %~dp0
echo   streamlit run streamlit_app.py
echo.
echo หรือดับเบิลคลิกที่ไฟล์ run_app.bat
echo.
pause