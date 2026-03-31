import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import os

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="AirTemp Analysis : Climate Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. Professional Background CSS ---
def set_bg(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            data = f.read()
        base64_image = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                            url("data:image/jpg;base64,{base64_image}");
                background-size: cover;
                background-attachment: fixed;
            }}
            
            /* Target Sidebar specifically for visibility */
            [data-testid="stSidebar"] {{
                background-color: rgba(0, 0, 0, 0.5); /* Adds a slight dark tint to sidebar background */
            }}
            
            /* Force all text, labels, and headers in the sidebar to be white */
            [data-testid="stSidebar"] .st-at, [data-testid="stSidebar"] label, [data-testid="stSidebar"] h2 {{
                color: white !important;
            }}

            /* Hide Deploy Button */
            header {{visibility: hidden;}}
            
            /* Glassmorphism for containers */
            div[data-testid="stMetric"], .stTabs {{
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 10px;
                backdrop-filter: blur(10px);
            }}

            /* Global text color fix */
            h1, h2, h3, p, span, label, .stMetricValue {{
                color: white !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

set_bg('climate-change-backgrounder.jpg')

# --- 3. Data Loading ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('climate_change_dataset.csv')
        df.dropna(inplace=True)
        return df
    except:
        return None

df = load_data()
if df is None: st.stop()

# --- 4. Sidebar Filters ---
st.sidebar.header('📂 Filters')
min_y, max_y = int(df['Year'].min()), int(df['Year'].max())
year_range = st.sidebar.slider('Year Range', min_y, max_y, (min_y, max_y))
countries = st.sidebar.multiselect('Countries', sorted(df['Country'].unique()), default=sorted(df['Country'].unique())[:5])

filtered_df = df[(df['Year'].between(year_range[0], year_range[1])) & (df['Country'].isin(countries) if countries else True)]

# --- 5. Main Dashboard ---
st.title('🌍 AirTemp Analytics : Climate Intelligence')

if not filtered_df.empty:
    # KPIs
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Avg Temp", f"{filtered_df['Avg Temperature (°C)'].mean():.2f} °C")
    m2.metric("Avg CO2", f"{filtered_df['CO2 Emissions (Tons/Capita)'].mean():.2f} T")
    m3.metric("Extreme Events", f"{filtered_df['Extreme Weather Events'].sum():,}")
    m4.metric("Renewable %", f"{filtered_df['Renewable Energy (%)'].mean():.1f}%")

    st.divider()

    # Tabs (Added Video Analysis Tab here)
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Trends", "📊 Correlations", "🗺️ Map", "🎥 Video Insights"])

    with tab1:
        metric = st.selectbox('Select Metric', df.columns.drop(['Year', 'Country']))
        fig_line = px.line(filtered_df.groupby('Year')[metric].mean().reset_index(), x='Year', y=metric, template="plotly_dark")
        st.plotly_chart(fig_line, use_container_width=True)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            fig_h, ax = plt.subplots(facecolor='none')
            sns.heatmap(filtered_df.drop('Year', axis=1).corr(numeric_only=True), annot=True, cmap='viridis', ax=ax)
            st.pyplot(fig_h)
        with c2:
            fig_scat = px.scatter(filtered_df, x='CO2 Emissions (Tons/Capita)', y='Avg Temperature (°C)', color='Country', template="plotly_dark")
            st.plotly_chart(fig_scat, use_container_width=True)

    with tab3:
        map_ind = st.selectbox('Map Indicator', ['Avg Temperature (°C)', 'CO2 Emissions (Tons/Capita)', 'Renewable Energy (%)'])
        fig_map = px.choropleth(filtered_df.groupby('Country')[map_ind].mean().reset_index(),
                                locations="Country", locationmode="country names", color=map_ind, template="plotly_dark")
        st.plotly_chart(fig_map, use_container_width=True)

    with tab4:
        st.subheader("Educational Video: Understanding Climate Change")
        # You can use a local file path or a YouTube URL
        video_url = "https://www.youtube.com/watch?v=dcBXmj1nMTQ" 
        st.video(video_url)
        st.write("Source: National Geographic - Climate Change 101")

    st.header('📂 Raw Data Explorer')
    st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown("Developed by **Hetaxi Rathod** | Data Source: Kaggle")