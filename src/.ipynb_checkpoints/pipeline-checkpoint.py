import pandas as pd
import numpy as np
def run_data_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Executes a complete data cleaning pipeline:
    - Removes duplicates
    - Corrects age entry errors
    - Standardizes text
    - Handles missing values
    - Caps salary outliers using IQR
    """
    df_clean = df.copy()
    # 1. Remove Duplicate Records
    df_clean = df_clean.drop_duplicates()
    # 2. Correct Data Entry Errors
    df_clean["age"] = df_clean["age"].apply(lambda x: x if (0 <= x <= 120) else np.nan)
    # 3. Standardize Text Values
    df_clean["name"] = df_clean["name"].fillna("Unknown").str.strip().str.title()
    df_clean["department"] = df_clean["department"].fillna("Unknown").str.strip().str.upper()
    # 4. Fill Missing Values
    df_clean["age"] = df_clean["age"].fillna(df_clean["age"].median())
    df_clean["salary"] = df_clean["salary"].fillna(df_clean["salary"].median())

    # 5. Detect and Cap Salary Outliers using IQR
    Q1 = df_clean["salary"].quantile(0.25)
    Q3 = df_clean["salary"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_clean["salary"] = np.where(df_clean["salary"] > upper_bound, upper_bound, df_clean["salary"])
    df_clean["salary"] = np.where(df_clean["salary"] < lower_bound, lower_bound, df_clean["salary"])
    return df_clean