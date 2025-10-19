# 🔑 Alpha Vantage API Setup Guide

## ✅ API Key ของคุณ
```
API Key: 81WH16M23KTGFE8G
```

## 📊 ข้อมูลการใช้งาน Alpha Vantage API

### 🆓 แผนฟรี (Free Plan):
- **5 API requests ต่อนาที**
- **500 API requests ต่อวัน**
- ข้อมูลหุ้นแบบเรียลไทม์จากตลาดหลักทรัพย์สหรัฐฯ

### 📈 ฟีเจอร์ที่รองรับ:
- ✅ ราคาหุ้นรายวัน (Daily Stock Prices)
- ✅ ข้อมูลปรับปรุงแล้ว (Adjusted Close)
- ✅ ปริมาณการซื้อขาย (Volume)
- ✅ ข้อมูลย้อนหลัง 100 วัน

### 🔧 การใช้งานในแอป:
1. **กรอกรหัสหุ้น** เช่น AAPL, MSFT, GOOGL
2. **คลิกปุ่มหุ้นยอดนิยม** เพื่อเลือกง่าย ๆ
3. **ดูกราฟ** และข้อมูลสถิติแบบละเอียด

### ⚠️ ข้อจำกัด:
- ถ้าใช้เกิน 5 requests ต่อนาทีจะต้องรอ
- หากใช้เกิน 500 requests ต่อวันต้องรอวันใหม่
- สามารถอัพเกรดเป็นแผนเสียเงินได้ที่ [alphavantage.co](https://www.alphavantage.co/premium/)

### 🎯 เคล็ดลับการใช้งาน:
- ใช้ปุ่มหุ้นยอดนิยมแทนการพิมพ์รหัสหุ้น
- ลองใช้ Yahoo Finance ถ้า API limit เต็ม
- ข้อมูลจะอัพเดตทุกวันหลังตลาดปิด

### 🔄 ทางเลือกอื่น:
หากไม่ต้องการใช้ Alpha Vantage API สามารถใช้ **Yahoo Finance** แทนได้:
```bash
pip install yfinance plotly
```

## 🚀 การรันแอป:
```bash
cd global_stocks_app
streamlit run streamlit_app.py
```

แอปจะเปิดที่ http://localhost:8501