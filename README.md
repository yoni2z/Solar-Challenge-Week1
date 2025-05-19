# Solar-Challenge-Week1

Solar Challenge Week 1

Task 1

This repository contains the code and deliverables for the 10 Academy Artificial Intelligence Mastery Week 0 Challenge, focusing on solar farm data analysis for Benin, Sierra Leone, and Togo.
Setup Instructions

Clone the Repository:
git clone https://github.com/yoni2z/Solar-Challenge-Week1.git
cd solar-challenge-week1


Set Up Virtual Environment:
python -m venv venv (or virtualenv venv)
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Run Jupyter Notebook:
jupyter notebook


Folder Structure:
├── .github/workflows/ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
├── tests/
├── scripts/



Dependencies

Python 3.8+
pandas, numpy, matplotlib, seaborn, scipy, jupyter


Task 2: Data Profiling, Cleaning & EDA

Branches: eda-benin, eda-sierraleone, eda-togo
Notebooks:
    - notebooks/benin_eda.ipynb: Profiling, cleaning, and EDA for Benin (525,600 rows).
    - notebooks/sierraleone_eda.ipynb: Profiling, cleaning, and EDA for Sierra Leone (525,600 rows).
    - notebooks/togo_eda.ipynb: Profiling, cleaning, and EDA for Togo (525,600 rows).
Cleaned Datasets:
    - data/benin_clean.csv
    - data/sierraleone_clean.csv
    - data/togo_clean.csv (in .gitignore)
Plots: Saved in notebooks/figures/.
Approach: Used chunking (50,000 rows) for loading, 10% sample for outliers, 10,000 rows for EDA.
References: pandas (https://pandas.pydata.org), scipy.stats (https://docs.scipy.org).

Task 3: Cross-Country Comparison and Strategic Recommendations

Task 3 synthesizes the cleaned datasets from Benin, Sierra Leone, and Togo to compare solar potential and provide strategic recommendations for MoonLight Energy Solutions’ solar investments.

Objectives
    -Compare Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI) across countries.
    -Identify the most suitable region for solar farm installation based on statistical analysis and exploratory data analysis (EDA).
    -Provide actionable recommendations to enhance operational efficiency and sustainability.

Methodology
    -Data Preparation: Loaded cleaned datasets (data/benin_clean.csv, data/sierraleone_clean.csv, data/togo_clean.csv) and concatenated them with a Country column for comparative analysis.
    -EDA: Generated boxplots and a bar chart (notebooks/figures/compare_visual_ghi.png) to visualize GHI, DNI, and DHI distributions, focusing on daytime data (GHI > 0) to mitigate nighttime skew.
    -Statistical Analysis: Conducted a one-way ANOVA test using scipy.stats.f_oneway to confirm significant differences in GHI means across countries (p-value = 0.0000).
    -Recommendations: Proposed targeting Benin for investment due to its superior GHI (240.56 W/m²) and DNI (167.19 W/m²), with strategies to mitigate variability using hybrid systems and battery storage.

Key Deliverables
    -Notebook: notebooks/compare_countries.ipynb containing EDA, visualizations, and ANOVA results.
    -Plot: notebooks/figures/compare_visual_ghi.png showing average GHI by country.
    -Findings: Benin identified as the optimal region, supported by statistical significance and high solar potential.


Optional Task 4: Running the Streamlit Dashboard
    -Ensure cleaned CSV files (benin_clean.csv, sierra_leone_clean.csv, togo_clean.csv) are in the data/ folder.
    -Run the dashboard:
        -run the command "streamlit run app/main.py" on the terminal
        -Open http://localhost:8501 in your browser.
        -Use the sidebar to select countries and view the GHI boxplot and top regions table.
    -Folder Structure
        -app/: Streamlit dashboard code (main.py, utils.py).
        -data/: Cleaned CSV files (ignored in .gitignore).
        -notebooks/: EDA notebooks for each country.
        -scripts/: Additional scripts.
        -.github/workflows/: CI/CD configuration.