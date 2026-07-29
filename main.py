import pandas as pd
import numpy as np
from src.pipeline import run_data_cleaning_pipeline
def main():
    print("🚀 Running Foundations & EDA Assessment Pipeline...\n")
    dirty_dataset = pd.DataFrame({
        "id": [1, 2, 2, 3, 4, 5, 6],
        "name": [" abel", "sara ", "sara ", None, "JOHN", "Helen", "marta"],
        "department": ["cs", "IT", "IT", "se", "CS", "it", None],
        "salary": [4000, 4500, 4500, np.nan, 5000, 4800, 85000],
        "age": [25, 230, 230, 28, 30, -4, 27]
    })
    print("=== RAW UNCLEANED DATASET ===")
    print(dirty_dataset.to_string(index=False))
    cleaned_df = run_data_cleaning_pipeline(dirty_dataset)
    print("\n=== FINAL CLEANED DATASET ===")
    print(cleaned_df.to_string(index=False))
    # Save cleaned output
    cleaned_df.to_csv("data/final_cleaned_assessment_data.csv", index=False)
    print("\n✅ Cleaned dataset saved to 'data/final_cleaned_assessment_data.csv'")
if __name__ == "__main__":
    main()