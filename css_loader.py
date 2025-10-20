"""
CSS Helper Functions for Loading External Stylesheets
"""
import streamlit as st
import os

def load_css(css_file):
    """Load CSS from external file"""
    css_path = os.path.join(os.path.dirname(__file__), 'styles', css_file)
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        return True
    except FileNotFoundError:
        st.error(f"CSS file not found: {css_file}")
        return False
    except Exception as e:
        st.error(f"Error loading CSS: {str(e)}")
        return False

def load_all_styles():
    """Load all CSS files for the application"""
    css_files = ['main.css', 'hero.css', 'cards.css', 'stocks.css']
    for css_file in css_files:
        load_css(css_file)
