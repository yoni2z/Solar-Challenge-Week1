import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_cleaned_data, get_top_regions

# Page configuration
st.set_page_config(page_title="Solar Farm Analysis Dashboard", layout="wide")

# Title and description
st.title("Solar Farm Analysis Dashboard")
st.markdown("""
This dashboard visualizes solar farm data for Benin, Sierra Leone, and Togo.
Select countries to compare GHI distributions and view top regions by average GHI.
""")

# Sidebar for country selection
st.sidebar.header("Filter Options")
countries = ["Benin", "SierraLeone", "Togo"]
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=countries,
    default=countries
)

if not selected_countries:
    st.warning("Please select at least one country.")
else:
    # Load data
    try:
        data_dict = load_cleaned_data(selected_countries)

        # Boxplot of GHI
        st.subheader("GHI Distribution by Country")
        plot_data = []
        for country in selected_countries:
            df = data_dict[country]
            df["Country"] = country
            plot_data.append(df[["Country", "GHI"]])
        plot_df = pd.concat(plot_data, ignore_index=True)
        fig = px.box(plot_df, x="Country", y="GHI", title="GHI Distribution (W/m²)",
                     color="Country", height=500)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        # Top regions table
        st.subheader("Top Regions by Average GHI")
        top_regions_df = get_top_regions(data_dict, metric="GHI")
        st.dataframe(top_regions_df, use_container_width=True)

    except FileNotFoundError as e:
        st.error(str(e))