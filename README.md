# AirTemp-Analytics

# 🌱 AirTemp Analytics: Global Climate Intelligence Dashboard

**AirTemp Analytics** is an end-to-end Data Science project designed to visualize and analyze global climate change indicators. This repository features both a deep-dive **Exploratory Data Analysis (EDA)** and an interactive **Streamlit Dashboard** for real-time policy insights.

---

## 🔍 Exploratory Data Analysis (EDA)
Before building the interactive dashboard, a comprehensive analysis was performed in the `Airtemp.ipynb` notebook. 

**Highlights of the EDA:**
- **Data Wrangling**: Handling missing values and normalizing climate indicators for 200+ countries.
- **Statistical Profiling**: Identifying the distribution of global temperatures and CO2 emissions per capita.
- **Correlation Mapping**: Discovering the strong statistical link between Forest Area (%) and Renewable Energy adoption.
- **Trend Spotting**: Identifying the specific decades where "Extreme Weather Events" showed the sharpest increase.

*To view the full analysis, open `Airtemp.ipynb` in VS Code or Jupyter Lab.*

---

## 🚀 Dashboard Features

- **Interactive Geospatial Mapping**: A global choropleth map for Avg Temperature, CO2 Emissions, and more.
- **Glassmorphism UI**: A professional, transparent interface with a custom "blended" background for high readability.
- **Dynamic Filtering**: Real-time updates based on country multiselect and year sliders.
- **Integrated Video**: Educational insights from National Geographic embedded directly in the platform.

---

## 🛠️ Tech Stack

- **Analysis**: Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn.
- **Web App**: [Streamlit](https://streamlit.io/) (Python-based framework).
- **Visualization**: Plotly Express (Interactive) & Seaborn (Statistical Heatmaps).

---

## 📥 Quick Start

### 1. Clone & Navigate
```bash
git clone [https://github.com/YOUR_USERNAME/AirTemp-Analytics.git](https://github.com/YOUR_USERNAME/AirTemp-Analytics.git)
cd AirTemp-Analytics

2. Install Requirements

pip install -r requirements.txt
3. Launch the App

streamlit run app.py


📂 Project Structure
Airtemp.ipynb: The core data science research and EDA.

new.py: The Python script powering the Streamlit dashboard.

climate_change_dataset.csv: The source dataset (Sourced from Kaggle).

climate-change-backgrounder.jpg: Custom UI background asset.

👩‍💻 Author
Hetaxi Rathod
---

### 💡 Final Steps for GitHub:
1. **The Notebook File**: Ensure `Airtemp.ipynb` is in the main folder (root) of your project so the link in the README works.
2. **Commit Message**: When you upload this to GitHub, use a message like: *"Add EDA notebook and update README for AirTemp Analytics project."*
3. **Environment**: Since you are using a notebook, make sure `ipykernel` is installed in your `venv` so you can run the EDA inside VS Code.
