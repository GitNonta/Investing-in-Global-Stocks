from setuptools import setup, find_packages

setup(
    name="global-stocks-app",
    version="1.0.0",
    author="Global Stock Investment Team",
    description="เว็บแอปสำหรับเรียนรู้และวิเคราะห์การลงทุนในหุ้นต่างประเทศ",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.0.0",
        "requests>=2.31.0",
        "numpy>=1.24.0",
        "plotly>=5.15.0",
        "yfinance>=0.2.18",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ]
    },
    entry_points={
        "console_scripts": [
            "global-stocks=streamlit_app:main",
        ],
    },
)