import streamlit as st

# Set page config
st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .title-text {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .welcome-text {
        font-size: 1.2rem;
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Display title and welcome text
st.markdown('<div class="title-text">🌍 Welcome to World Cities</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="welcome-text">Explore cities around the world and discover fascinating information about them.</div>',
    unsafe_allow_html=True
)

# Display introductory content
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📍 **Search** - Find cities by name or country")

with col2:
    st.info("📊 **Statistics** - View demographic information")

with col3:
    st.info("🗺️ **Discover** - Explore cities on the map")

st.divider()

# Navigation to app page
st.subheader("Get Started")
if st.button("🚀 Go to App", use_container_width=True, key="go_to_app"):
    st.switch_page("pages/app.py")

st.divider()

# Additional information
st.markdown("""
### About This App
This Streamlit multipage application provides a comprehensive guide to world cities.
Navigate through different sections using the sidebar to explore more features.

### Features
- Browse and search world cities
- View detailed information about each city
- Access statistical data
- Visualize data with interactive charts

---
**Created with Streamlit** | **Explore the world, one city at a time** 🌏
""")
