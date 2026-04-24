"""
Data cleaning module for processing raw data files.
"""

import pandas as pd
from pathlib import Path


def load_raw_data(file_path):
    """Load raw data from CSV file."""
    return pd.read_csv(file_path)


def clean_data(df):
    """
    Perform data cleaning operations:
    - Remove duplicates
    - Handle missing values
    - Standardize formats
    """
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    return df


def save_cleaned_data(df, output_path):
    """Save cleaned data to CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")


if __name__ == "__main__":
    # Load raw data
    raw_file = Path(__file__).parent.parent / "data" / "raw_data.csv"
    df = load_raw_data(raw_file)
    
    # Clean data
    df_cleaned = clean_data(df)
    
    # Save cleaned data
    output_file = Path(__file__).parent.parent / "data" / "cleaned_data.csv"
    save_cleaned_data(df_cleaned, output_file)
