import streamlit as st
import datetime
import requests
import sys
import os

# เพิ่ม path สำหรับ import config
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_BASE_URL
from css_loader import load_all_styles

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False

# Add FontAwesome CDN (ต้องอยู่ก่อนเมนูบาร์เสมอ)
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
""", unsafe_allow_html=True)

# Configuration
st.set_page_config(
    page_title="Global Stock Investment Guide", 
    page_icon="<i class='fa-solid fa-globe'></i>", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load all CSS styles
load_all_styles()

menu_icons = {
    "home": "<i class='fa-solid fa-house' style='margin-right:6px;'></i>",
    "basics": "<i class='fa-solid fa-book-open' style='margin-right:6px;'></i>",
    "analysis": "<i class='fa-solid fa-chart-line' style='margin-right:6px;'></i>",
    "forex": "<i class='fa-solid fa-coins' style='margin-right:6px;'></i>",
    "tips": "<i class='fa-solid fa-lightbulb' style='margin-right:6px;'></i>"
}

# Modern Menu Bar
st.markdown("""
<div class="menu-container">
    <div class="menu-nav">
        <div class="logo"><i class='fa-solid fa-globe'></i>&nbsp;Global Stocks</div>
        <input type="checkbox" id="menu-toggle" style="display:none;" />
        <label class="menu-hamburger" for="menu-toggle">
            <span></span>
            <span></span>
            <span></span>
        </label>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Menu using Streamlit
st.markdown("### <i class='fa-solid fa-book-open'></i> เนื้อหาทั้งหมด", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("⌂ หน้าหลัก", use_container_width=True, type="primary", key="nav_home", help="กลับสู่หน้าหลัก"):
        st.rerun()

with col2:
    if st.button("◉ พื้นฐานการลงทุน", use_container_width=True, key="nav_basics"):
        st.switch_page("pages/1_Basics_of_Investment.py")

with col3:
    if st.button("📈 วิเคราะห์หุ้น", use_container_width=True, key="nav_analysis"):
        st.switch_page("pages/2_Stock_Data_Analysis.py")

with col4:
    if st.button("⚖ ความเสี่ยง", use_container_width=True, key="nav_forex"):
        st.switch_page("pages/3_Forex_and_Risk.py")

with col5:
    if st.button("💡 เคล็ดลับ", use_container_width=True, key="nav_tips"):
        st.switch_page("pages/4_About_and_Tips.py")

st.divider()

# Hero Section with modern styling
st.markdown("""
<div class="hero-section">
    <h1>
        <i class='fa-solid fa-globe'></i> Global Stock Investment Guide
    </h1>
    <p>
        เรียนรู้และวิเคราะห์การลงทุนในหุ้นต่างประเทศอย่างครบถ้วน
    </p>
</div>
""", unsafe_allow_html=True)

# Apple-inspired Slideshow
st.markdown("""
<div class="slideshow-container">
    <!-- Slide 1: Welcome -->
    <div class="slide slide-1 active">
        <div class="slide-controls">
            <button class="control-btn" onclick="toggleAutoPlay()">
                <i class="fa-solid fa-pause"></i> <span id="play-text">Pause</span>
            </button>
        </div>
        <div class="slide-content">
            <div class="slide-icon">💎</div>
            <h2>ยินดีต้อนรับสู่การลงทุนระดับโลก</h2>
            <p>เริ่มต้นเส้นทางการลงทุนของคุณด้วยเครื่องมือและความรู้ที่ครบครัน</p>
            <div class="slide-features">
                <div class="feature-item">
                    <i class="fa-solid fa-chart-line"></i>
                    <div>ข้อมูลเรียลไทม์</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-graduation-cap"></i>
                    <div>เรียนรู้ฟรี</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-shield-halved"></i>
                    <div>ปลอดภัย</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Slide 2: Analysis Tools -->
    <div class="slide slide-2">
        <div class="slide-controls">
            <button class="control-btn" onclick="toggleAutoPlay()">
                <i class="fa-solid fa-pause"></i> <span id="play-text-2">Pause</span>
            </button>
        </div>
        <div class="slide-content">
            <div class="slide-icon">📊</div>
            <h2>เครื่องมือวิเคราะห์ที่ทรงพลัง</h2>
            <p>วิเคราะห์หุ้นด้วย AI และข้อมูลแบบเรียลไทม์จาก Alpha Vantage & Yahoo Finance</p>
            <div class="slide-features">
                <div class="feature-item">
                    <i class="fa-solid fa-robot"></i>
                    <div>AI Analysis</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-chart-area"></i>
                    <div>Interactive Charts</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-database"></i>
                    <div>Real-time Data</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Slide 3: Global Markets -->
    <div class="slide slide-3">
        <div class="slide-controls">
            <button class="control-btn" onclick="toggleAutoPlay()">
                <i class="fa-solid fa-pause"></i> <span id="play-text-3">Pause</span>
            </button>
        </div>
        <div class="slide-content">
            <div class="slide-icon">🌍</div>
            <h2>เข้าถึงตลาดโลก</h2>
            <p>ลงทุนในหุ้นชั้นนำจาก NYSE, NASDAQ, LSE และตลาดอื่น ๆ ทั่วโลก</p>
            <div class="slide-features">
                <div class="feature-item">
                    <i class="fa-solid fa-building-columns"></i>
                    <div>NYSE & NASDAQ</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-landmark"></i>
                    <div>London Stock Exchange</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-yen-sign"></i>
                    <div>Asian Markets</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Slide 4: Risk Management -->
    <div class="slide slide-4">
        <div class="slide-controls">
            <button class="control-btn" onclick="toggleAutoPlay()">
                <i class="fa-solid fa-pause"></i> <span id="play-text-4">Pause</span>
            </button>
        </div>
        <div class="slide-content">
            <div class="slide-icon">🛡️</div>
            <h2>บริหารความเสี่ยงอย่างมืออาชีพ</h2>
            <p>เครื่องคำนวณความเสี่ยง Forex และเครื่องมือบริหารพอร์ตโฟลิโอ</p>
            <div class="slide-features">
                <div class="feature-item">
                    <i class="fa-solid fa-calculator"></i>
                    <div>Risk Calculator</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-coins"></i>
                    <div>Forex Analysis</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-chart-pie"></i>
                    <div>Portfolio Management</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Slide 5: Learn & Grow -->
    <div class="slide slide-5">
        <div class="slide-controls">
            <button class="control-btn" onclick="toggleAutoPlay()">
                <i class="fa-solid fa-pause"></i> <span id="play-text-5">Pause</span>
            </button>
        </div>
        <div class="slide-content">
            <div class="slide-icon">🚀</div>
            <h2>เรียนรู้และเติบโตไปด้วยกัน</h2>
            <p>บทเรียน เคล็ดลับ และกลยุทธ์จากผู้เชี่ยวชาญเพื่อความสำเร็จของคุณ</p>
            <div class="slide-features">
                <div class="feature-item">
                    <i class="fa-solid fa-book-open"></i>
                    <div>Free Courses</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-lightbulb"></i>
                    <div>Expert Tips</div>
                </div>
                <div class="feature-item">
                    <i class="fa-solid fa-trophy"></i>
                    <div>Success Stories</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Navigation Arrows -->
    <div class="slide-arrow prev" onclick="changeSlide(-1)">
        <i class="fa-solid fa-chevron-left"></i>
    </div>
    <div class="slide-arrow next" onclick="changeSlide(1)">
        <i class="fa-solid fa-chevron-right"></i>
    </div>

    <!-- Dots Indicator -->
    <div class="slide-dots">
        <span class="dot active" onclick="currentSlide(0)"></span>
        <span class="dot" onclick="currentSlide(1)"></span>
        <span class="dot" onclick="currentSlide(2)"></span>
        <span class="dot" onclick="currentSlide(3)"></span>
        <span class="dot" onclick="currentSlide(4)"></span>
    </div>

    <!-- Progress Bar -->
    <div class="slide-progress">
        <div class="slide-progress-bar" id="progress-bar"></div>
    </div>

    <!-- Swipe Hint for Mobile -->
    <div class="swipe-hint">
        <i class="fa-solid fa-hand-pointer"></i> ลากเพื่อเปลี่ยนสไลด์
    </div>
</div>

<script>
let slideIndex = 0;
let autoPlayInterval;
let isAutoPlaying = true;
let progressInterval;

// Initialize slideshow
document.addEventListener('DOMContentLoaded', function() {
    showSlide(slideIndex);
    startAutoPlay();
    
    // Touch/Swipe support
    let touchStartX = 0;
    let touchEndX = 0;
    const container = document.querySelector('.slideshow-container');
    
    container.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    container.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });
    
    function handleSwipe() {
        if (touchEndX < touchStartX - 50) changeSlide(1);
        if (touchEndX > touchStartX + 50) changeSlide(-1);
    }
});

function showSlide(n) {
    const slides = document.getElementsByClassName('slide');
    const dots = document.getElementsByClassName('dot');
    
    if (n >= slides.length) { slideIndex = 0; }
    if (n < 0) { slideIndex = slides.length - 1; }
    
    // Hide all slides
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove('active');
    }
    
    // Remove active from all dots
    for (let i = 0; i < dots.length; i++) {
        dots[i].classList.remove('active');
    }
    
    // Show current slide
    slides[slideIndex].classList.add('active');
    dots[slideIndex].classList.add('active');
    
    // Reset progress bar
    resetProgress();
}

function changeSlide(n) {
    slideIndex += n;
    showSlide(slideIndex);
    
    // Restart autoplay
    if (isAutoPlaying) {
        clearInterval(autoPlayInterval);
        startAutoPlay();
    }
}

function currentSlide(n) {
    slideIndex = n;
    showSlide(slideIndex);
    
    // Restart autoplay
    if (isAutoPlaying) {
        clearInterval(autoPlayInterval);
        startAutoPlay();
    }
}

function startAutoPlay() {
    const duration = 5000; // 5 seconds per slide
    let progress = 0;
    
    // Clear existing intervals
    clearInterval(autoPlayInterval);
    clearInterval(progressInterval);
    
    // Start new autoplay
    autoPlayInterval = setInterval(() => {
        changeSlide(1);
    }, duration);
    
    // Progress bar animation
    progressInterval = setInterval(() => {
        progress += 100 / (duration / 100);
        if (progress >= 100) {
            progress = 0;
        }
        document.getElementById('progress-bar').style.width = progress + '%';
    }, 100);
}

function resetProgress() {
    document.getElementById('progress-bar').style.width = '0%';
}

function toggleAutoPlay() {
    const playText = document.getElementById('play-text');
    const playText2 = document.getElementById('play-text-2');
    const playText3 = document.getElementById('play-text-3');
    const playText4 = document.getElementById('play-text-4');
    const playText5 = document.getElementById('play-text-5');
    const btns = document.querySelectorAll('.control-btn i');
    
    if (isAutoPlaying) {
        clearInterval(autoPlayInterval);
        clearInterval(progressInterval);
        isAutoPlaying = false;
        
        // Update all buttons
        [playText, playText2, playText3, playText4, playText5].forEach(el => {
            if (el) el.textContent = 'Play';
        });
        btns.forEach(btn => {
            btn.className = 'fa-solid fa-play';
        });
    } else {
        startAutoPlay();
        isAutoPlaying = true;
        
        // Update all buttons
        [playText, playText2, playText3, playText4, playText5].forEach(el => {
            if (el) el.textContent = 'Pause';
        });
        btns.forEach(btn => {
            btn.className = 'fa-solid fa-pause';
        });
    }
}

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') changeSlide(-1);
    if (e.key === 'ArrowRight') changeSlide(1);
    if (e.key === ' ') {
        e.preventDefault();
        toggleAutoPlay();
    }
});
</script>
""", unsafe_allow_html=True)

st.markdown("---")

# Market Overview with images
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=400&h=300&fit=crop", 
             caption="Financial Analysis", use_container_width=True)
    st.markdown("**วิเคราะห์เทคนิค**  \nเครื่องมือการวิเคราะห์ที่ทันสมัย")

with col2:
    st.image("https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=400&h=300&fit=crop", 
             caption="Global Markets", use_container_width=True)
    st.markdown("**ตลาดโลก**  \nเข้าถึงตลาดหลักทรัพย์ทั่วโลก")

with col3:
    st.image("https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=400&h=300&fit=crop", 
             caption="Investment Strategy", use_container_width=True)
    st.markdown("**กลยุทธ์การลงทุน**  \nแนวทางการลงทุนที่เหมาะสม")

# Current Market Status
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-chart-line'></i> สถานการณ์ตลาดวันนี้</h2>", unsafe_allow_html=True)

# Fetch real market data with auto-rotating slideshow
@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_all_market_data():
    """ดึงข้อมูลตลาดและหุ้นทั้งหมด"""
    # รวมดัชนีตลาดและหุ้นยอดนิยม
    all_symbols = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "Dow Jones": "^DJI",
        "Nikkei 225": "^N225",
        "FTSE 100": "^FTSE",
        "DAX": "^GDAXI",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Google": "GOOGL",
        "Amazon": "AMZN",
        "Tesla": "TSLA",
        "NVIDIA": "NVDA",
        "Meta": "META",
        "JPMorgan": "JPM",
        "Netflix": "NFLX",
        "Adobe": "ADBE",
        "Intel": "INTC",
        "Cisco": "CSCO"
    }
    
    market_data = []
    
    if YFINANCE_AVAILABLE:
        try:
            for name, symbol in all_symbols.items():
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="2d")
                
                if len(hist) >= 2:
                    current_price = hist['Close'].iloc[-1]
                    prev_price = hist['Close'].iloc[-2]
                    change = current_price - prev_price
                    change_pct = (change / prev_price) * 100
                    
                    market_data.append({
                        "name": name,
                        "price": f"{current_price:,.2f}",
                        "change": f"{change:+.2f}",
                        "change_pct": f"{change_pct:+.2f}%",
                        "raw_change": change
                    })
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {str(e)}")
            return None
    else:
        # ข้อมูลจำลอง
        market_data = [
            {"name": "S&P 500", "price": "4,500.25", "change": "+12.50", "change_pct": "+0.28%", "raw_change": 12.5},
            {"name": "NASDAQ", "price": "14,200.30", "change": "-25.80", "change_pct": "-0.18%", "raw_change": -25.8},
            {"name": "Dow Jones", "price": "35,100.45", "change": "+85.30", "change_pct": "+0.24%", "raw_change": 85.3},
            {"name": "Nikkei 225", "price": "33,750.89", "change": "+180.20", "change_pct": "+0.54%", "raw_change": 180.2},
            {"name": "Apple", "price": "178.50", "change": "+2.30", "change_pct": "+1.31%", "raw_change": 2.3},
            {"name": "Microsoft", "price": "412.30", "change": "-1.50", "change_pct": "-0.36%", "raw_change": -1.5},
            {"name": "Google", "price": "142.80", "change": "+3.20", "change_pct": "+2.29%", "raw_change": 3.2},
            {"name": "Tesla", "price": "242.80", "change": "-4.50", "change_pct": "-1.82%", "raw_change": -4.5}
        ]
    
    return market_data

# Initialize session state for slideshow
if 'market_slide_index' not in st.session_state:
    st.session_state.market_slide_index = 0

# Auto-advance slideshow (every 3 seconds)
import time
current_time = int(time.time())
slide_interval = 3  # seconds

# Calculate which slide to show based on time
auto_slide_index = (current_time // slide_interval) % 100  # Will cycle through slides

# Get all market data
all_market_data = get_all_market_data()

if all_market_data and len(all_market_data) > 0:
    # Calculate how many complete sets of 4 we have
    total_slides = (len(all_market_data) + 3) // 4  # Round up division
    
    # Use time-based auto-rotation
    current_slide = auto_slide_index % total_slides
    
    # Get 4 items for current slide
    start_idx = current_slide * 4
    end_idx = min(start_idx + 4, len(all_market_data))
    current_items = all_market_data[start_idx:end_idx]
    
    # Display current slide
    cols = st.columns(len(current_items))
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    for i, data in enumerate(current_items):
        with cols[i]:
            st.metric(data["name"], data["price"], f"{data['change']} ({data['change_pct']})")
    
    # Slideshow indicator
    st.markdown(f"""
    <div style="text-align: center; margin-top: 1rem;">
        <span style="color: #666; font-size: 0.9rem;">
            <i class='fa-solid fa-chart-line'></i> {current_slide + 1}/{total_slides} • 
            {"<i class='fa-solid fa-circle' style='color: #f44336;'></i>" if YFINANCE_AVAILABLE else "<i class='fa-solid fa-triangle-exclamation' style='color: #ff9800;'></i>"} 
            {f"ข้อมูลจริงจาก Yahoo Finance" if YFINANCE_AVAILABLE else "ข้อมูลจำลอง"} • 
            อัพเดท: {current_date}
        </span>
        <br/>
        <span style="color: #999; font-size: 0.8rem;">
            <i class='fa-solid fa-rotate'></i> สไลด์โชว์อัตโนมัติทุก {slide_interval} วินาที ({len(all_market_data)} รายการ)
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    if not YFINANCE_AVAILABLE:
        st.info("<i class='fa-solid fa-lightbulb'></i> รันคำสั่ง: `pip install yfinance` เพื่อดูข้อมูลตลาดแบบเรียลไทม์", icon="💡")
    
    # Force refresh every 3 seconds
    st.markdown(f"""
    <script>
        setTimeout(function(){{
            window.parent.location.reload();
        }}, {slide_interval * 1000});
    </script>
    """, unsafe_allow_html=True)
else:
    st.warning("ไม่สามารถดึงข้อมูลตลาดได้ในขณะนี้")

# Popular Stocks Section
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-fire'></i> หุ้นยอดนิยม</h2>", unsafe_allow_html=True)

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_popular_stocks():
    """ดึงข้อมูลหุ้นยอดนิยม"""
    # Dictionary mapping symbols to company domains for logos
    symbol_domains = {
        "AAPL": "apple.com",
        "MSFT": "microsoft.com",
        "GOOGL": "google.com",
        "AMZN": "amazon.com",
        "TSLA": "tesla.com",
        "NVDA": "nvidia.com",
        "META": "meta.com",
        "JPM": "jpmorganchase.com"
    }
    
    popular_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "JPM"]
    stocks_data = []
    
    if YFINANCE_AVAILABLE:
        try:
            for symbol in popular_symbols:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                hist = ticker.history(period="1d")
                
                if not hist.empty:
                    current_price = hist['Close'].iloc[-1]
                    # ดึง previous close จาก info
                    prev_close = info.get('previousClose', current_price)
                    change = current_price - prev_close
                    change_pct = (change / prev_close) * 100 if prev_close != 0 else 0
                    
                    stocks_data.append({
                        "symbol": symbol,
                        "name": info.get('shortName', symbol),
                        "price": current_price,
                        "change": change,
                        "change_pct": change_pct,
                        "domain": symbol_domains.get(symbol, "example.com")
                    })
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการดึงข้อมูลหุ้น: {str(e)}")
            return None
    else:
        # ข้อมูลจำลอง
        stocks_data = [
            {"symbol": "AAPL", "name": "Apple Inc.", "price": 178.50, "change": 2.30, "change_pct": 1.31, "domain": "apple.com"},
            {"symbol": "MSFT", "name": "Microsoft Corp", "price": 412.30, "change": -1.50, "change_pct": -0.36, "domain": "microsoft.com"},
            {"symbol": "GOOGL", "name": "Alphabet Inc", "price": 142.80, "change": 3.20, "change_pct": 2.29, "domain": "google.com"},
            {"symbol": "AMZN", "name": "Amazon.com Inc", "price": 178.25, "change": 1.75, "change_pct": 0.99, "domain": "amazon.com"},
            {"symbol": "TSLA", "name": "Tesla Inc", "price": 242.80, "change": -4.50, "change_pct": -1.82, "domain": "tesla.com"},
            {"symbol": "NVDA", "name": "NVIDIA Corp", "price": 495.20, "change": 8.30, "change_pct": 1.70, "domain": "nvidia.com"},
            {"symbol": "META", "name": "Meta Platforms", "price": 485.60, "change": 5.40, "change_pct": 1.12, "domain": "meta.com"},
            {"symbol": "JPM", "name": "JPMorgan Chase", "price": 198.75, "change": -0.85, "change_pct": -0.43, "domain": "jpmorganchase.com"}
        ]
    
    return stocks_data

# Display popular stocks
popular_stocks = get_popular_stocks()

if popular_stocks:
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]
    
    for i, stock in enumerate(popular_stocks):
        with cols[i % 4]:
            # กำหนดสีตาม change
            change_icon = "<i class='fa-solid fa-circle' style='color: #4caf50;'></i>" if stock["change"] > 0 else "<i class='fa-solid fa-circle' style='color: #f44336;'></i>" if stock["change"] < 0 else "<i class='fa-solid fa-circle' style='color: #9e9e9e;'></i>"
            logo_url = f"https://logo.clearbit.com/{stock['domain']}"
            
            # แสดงโลโก้และข้อมูล
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 0.5rem;">
                <img src="{logo_url}" alt="{stock['symbol']}" 
                     style="width: 40px; height: 40px; border-radius: 8px; object-fit: contain; background: #f8f9fa; padding: 4px;"
                     onerror="this.style.display='none'">
            </div>
            """, unsafe_allow_html=True)
            
            st.metric(
                label=f"**{stock['symbol']}**",
                value=f"${stock['price']:.2f}",
                delta=f"{stock['change']:+.2f} ({stock['change_pct']:+.2f}%)"
            )
            st.caption(stock['name'][:20])
    
    if YFINANCE_AVAILABLE:
        st.caption("<i class='fa-solid fa-chart-line'></i> ข้อมูลจริงจาก Yahoo Finance (อัพเดททุก 5 นาที)", unsafe_allow_html=True)
    else:
        st.caption("<i class='fa-solid fa-triangle-exclamation'></i> ข้อมูลจำลอง - ติดตั้ง yfinance เพื่อดูข้อมูลจริง", unsafe_allow_html=True)
else:
    st.warning("ไม่สามารถดึงข้อมูลหุ้นได้ในขณะนี้")

# Welcome Message
st.markdown("""
### <i class='fa-solid fa-handshake'></i> ยินดีต้อนรับนักลงทุนมือใหม่!

การลงทุนในหุ้นต่างประเทศเป็นหนทางสู่การสร้างความมั่งคั่งระยะยาว เว็บแอปนี้จะพาคุณเรียนรู้:

<i class='fa-solid fa-book-open'></i> **พื้นฐานการลงทุน** - ความรู้เบื้องต้นที่จำเป็น  
<i class='fa-solid fa-chart-line'></i> **การวิเคราะห์ข้อมูล** - เครื่องมือและเทคนิคการวิเคราะห์  
<i class='fa-solid fa-shield-halved'></i> **การบริหารความเสี่ยง** - วิธีป้องกันและลดความเสี่ยง  
<i class='fa-solid fa-lightbulb'></i> **กลยุทธ์การลงทุน** - แนวทางที่เหมาะสมกับคุณ  
""", unsafe_allow_html=True)

# Learning Path with modern cards
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-map'></i> เส้นทางการเรียนรู้</h2>", unsafe_allow_html=True)

# Learning cards
learning_cards = [
    {
        "icon": "<i class='fa-solid fa-book-open'></i>",
        "title": "พื้นฐานการลงทุน",
        "desc": "เริ่มต้นด้วยความรู้พื้นฐาน",
        "link": "/1_Basics_of_Investment",
        "color": "#4CAF50"
    },
    {
        "icon": "<i class='fa-solid fa-chart-line'></i>", 
        "title": "วิเคราะห์ข้อมูลหุ้น",
        "desc": "เครื่องมือวิเคราะห์แบบเรียลไทม์",
        "link": "/2_Stock_Data_Analysis", 
        "color": "#2196F3"
    },
    {
        "icon": "<i class='fa-solid fa-coins'></i>",
        "title": "ความเสี่ยงและค่าเงิน", 
        "desc": "ทำความเข้าใจ Forex Risk",
        "link": "/3_Forex_and_Risk",
        "color": "#FF9800"
    },
    {
        "icon": "<i class='fa-solid fa-lightbulb'></i>",
        "title": "เคล็ดลับและแหล่งความรู้",
        "desc": "ทรัพยากรและกลยุทธ์ขั้นสูง", 
        "link": "/4_About_and_Tips",
        "color": "#9C27B0"
    }
]

# Display learning cards with clickable cards
cols = st.columns(2)

# Card 1: พื้นฐานการลงทุน
with cols[0]:
    if st.button("📖 พื้นฐานการลงทุน\n\nเริ่มต้นด้วยความรู้พื้นฐาน", key="card_basics", use_container_width=True, type="secondary"):
        st.switch_page("pages/1_Basics_of_Investment.py")
    
# Card 2: วิเคราะห์ข้อมูลหุ้น
with cols[1]:
    if st.button("📊 วิเคราะห์ข้อมูลหุ้น\n\nเครื่องมือวิเคราะห์แบบเรียลไทม์", key="card_analysis", use_container_width=True, type="secondary"):
        st.switch_page("pages/2_Stock_Data_Analysis.py")

# Card 3: ความเสี่ยงและค่าเงิน
with cols[0]:
    if st.button("💰 ความเสี่ยงและค่าเงิน\n\nทำความเข้าใจ Forex Risk", key="card_forex", use_container_width=True, type="secondary"):
        st.switch_page("pages/3_Forex_and_Risk.py")

# Card 4: เคล็ดลับและแหล่งความรู้
with cols[1]:
    if st.button("💡 เคล็ดลับและแหล่งความรู้\n\nทรัพยากรและกลยุทธ์ขั้นสูง", key="card_tips", use_container_width=True, type="secondary"):
        st.switch_page("pages/4_About_and_Tips.py")

# Features Section
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-star'></i> ฟีเจอร์เด่น</h2>", unsafe_allow_html=True)

feature_cols = st.columns(2)

with feature_cols[0]:
    st.markdown("""
    ### <i class='fa-solid fa-screwdriver-wrench'></i> เครื่องมือที่ทรงพลัง
    
    <i class='fa-solid fa-chart-line'></i> **Real-time Stock Data**  
    ข้อมูลหุ้นแบบเรียลไทม์จาก Alpha Vantage API
    
    <i class='fa-solid fa-chart-area'></i> **Interactive Charts**  
    กราฟการวิเคราะห์แบบโต้ตอบได้ด้วย Plotly
    
    <i class='fa-solid fa-calculator'></i> **Risk Calculator**  
    เครื่องคำนวณความเสี่ยงจากค่าเงิน
    
    <i class='fa-solid fa-mobile-screen'></i> **Responsive Design**  
    ใช้งานได้บนทุกอุปกรณ์
    """, unsafe_allow_html=True)

with feature_cols[1]:
    st.markdown("""
    ### <i class='fa-solid fa-graduation-cap'></i> แหล่งเรียนรู้ครบครัน
    
    <i class='fa-solid fa-book'></i> **Educational Content**  
    เนื้อหาการศึกษาที่ครอบคลุมทุกระดับ
    
    <i class='fa-solid fa-globe'></i> **Global Markets**  
    ข้อมูลจากตลาดหลักทรัพย์ทั่วโลก
    
    <i class='fa-solid fa-lightbulb'></i> **Expert Tips**  
    เคล็ดลับจากผู้เชี่ยวชาญการลงทุน
    
    <i class='fa-solid fa-lock'></i> **Safe Learning**  
    สภาพแวดล้อมการเรียนรู้ที่ปลอดภัย
    """, unsafe_allow_html=True)

# Popular Stocks Preview
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-fire'></i> หุ้นยอดนิยม</h2>", unsafe_allow_html=True)

pop_cols = st.columns(4)
popular_stocks = [
    {"symbol": "AAPL", "name": "Apple Inc.", "price": "$175.84", "change": "+2.1%", "domain": "apple.com"},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "price": "$338.11", "change": "+0.8%", "domain": "microsoft.com"}, 
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "price": "$126.50", "change": "-0.3%", "domain": "google.com"},
    {"symbol": "TSLA", "name": "Tesla Inc.", "price": "$248.50", "change": "+4.2%", "domain": "tesla.com"}
]

for i, stock in enumerate(popular_stocks):
    with pop_cols[i]:
        change_color = "green" if "+" in stock["change"] else "red"
        logo_url = f"https://logo.clearbit.com/{stock['domain']}"
        st.markdown(f"""
        <div class="stock-card">
            <img src="{logo_url}" alt="{stock['symbol']}" class="stock-logo" 
                 onerror="this.style.display='none'" 
                 style="width: 48px; height: 48px; border-radius: 8px; margin-bottom: 0.5rem; object-fit: contain;">
            <h4>{stock['symbol']}</h4>
            <p class="stock-name">{stock['name']}</p>
            <p class="stock-price">{stock['price']}</p>
            <p class="stock-change" style="color: {change_color};">{stock['change']}</p>
        </div>
        """, unsafe_allow_html=True)

# Quick Start Tips
st.markdown("---")
st.markdown("<h2><i class='fa-solid fa-rocket'></i> เริ่มต้นอย่างไร?</h2>", unsafe_allow_html=True)

tips_cols = st.columns(3)

with tips_cols[0]:
    st.markdown("""
    #### <i class='fa-solid fa-1'></i> เตรียมตัว
    - <i class='fa-solid fa-book'></i> อ่านพื้นฐานการลงทุน
    - <i class='fa-solid fa-money-bill-wave'></i> กำหนดงบประมาณ
    - <i class='fa-solid fa-bullseye'></i> ตั้งเป้าหมาย
    """, unsafe_allow_html=True)

with tips_cols[1]:
    st.markdown("""
    #### <i class='fa-solid fa-2'></i> เรียนรู้
    - <i class='fa-solid fa-chart-line'></i> ทำความเข้าใจกราฟ
    - <i class='fa-solid fa-magnifying-glass'></i> วิเคราะห์บริษัท
    - <i class='fa-solid fa-scale-balanced'></i> บริหารความเสี่ยง
    """, unsafe_allow_html=True)

with tips_cols[2]:
    st.markdown("""
    #### <i class='fa-solid fa-3'></i> ลงมือทำ
    - <i class='fa-solid fa-briefcase'></i> เปิดบัญชีลงทุน
    - <i class='fa-solid fa-arrow-trend-up'></i> เริ่มลงทุนจำนวนเล็ก
    - <i class='fa-solid fa-pen-to-square'></i> ติดตามผล
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p><i class='fa-solid fa-triangle-exclamation'></i> <strong>คำเตือน:</strong> ข้อมูลในแอปนี้เป็นเพียงการศึกษาเท่านั้น ไม่ใช่คำแนะนำในการลงทุน</p>
    <p><i class='fa-solid fa-lightbulb'></i> การลงทุนมีความเสี่ยง ควรศึกษาข้อมูลให้ครบถ้วนก่อนตัดสินใจ</p>
</div>
""", unsafe_allow_html=True)