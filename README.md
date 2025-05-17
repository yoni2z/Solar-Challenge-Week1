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
