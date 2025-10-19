#!/bin/bash

echo "==================================="
echo " เริ่มต้น Global Stock App"
echo "==================================="
echo

echo "กำลังตรวจสอบ Streamlit..."
if ! command -v streamlit &> /dev/null; then
    echo "❌ ไม่พบ Streamlit!"
    echo "กรุณารันไฟล์ ./install_requirements.sh ก่อน"
    exit 1
fi

echo "✅ เริ่มต้นแอป..."
echo
echo "🌐 เว็บแอปจะเปิดใน Browser อัตโนมัติ"
echo "📊 URL: http://localhost:8501"
echo
echo "กด Ctrl+C เพื่อปิดแอป"
echo

cd "$(dirname "$0")"
streamlit run streamlit_app.py