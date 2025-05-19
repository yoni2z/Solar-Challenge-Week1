import pandas as pd
import os

def load_cleaned_data(countries):
    """
    Load cleaned CSV files for specified countries.
    Returns a dictionary with country names as keys and DataFrames as values.
    """
    data = {}
    for country in countries:
        file_path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
        if os.path.exists(file_path):
            data[country] = pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"Cleaned data for {country} not found at {file_path}")
    return data

def get_top_regions(data_dict, metric="GHI", top_n=5):
    """
    Compute top regions (countries) by average metric (e.g., GHI).
    Returns a DataFrame with country, average metric, and rank.
    """
    means = []
    for country, df in data_dict.items():
        if metric in df.columns:
            mean_value = df[metric].mean()
            means.append({"Country": country, f"Average {metric} (W/m²)": round(mean_value, 2)})
    result_df = pd.DataFrame(means)
    result_df = result_df.sort_values(f"Average {metric} (W/m²)", ascending=False).reset_index(drop=True)
    result_df["Rank"] = result_df.index + 1
    return result_df.head(top_n)