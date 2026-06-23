import pandas as pd
import os
import glob

def load_and_inspect_datasets(data_dir="data/raw"):
    """Loads all CSVs in the specified directory and prints basic info."""
    print(f"--- Inspecting all CSV datasets in {data_dir} ---")
    csv_files = glob.glob(os.path.join(data_dir, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {data_dir}. Please place the 10 provided datasets here.")
        return
    
    for file_path in csv_files:
        filename = os.path.basename(file_path)
        print(f"\n[{filename}]")
        try:
            df = pd.read_csv(file_path)
            print(f"Shape: {df.shape}")
            print("Data Types:")
            print(df.dtypes)
            print("Head:")
            print(df.head())
        except Exception as e:
            print(f"Error reading {filename}: {e}")

def explore_fund_master(fund_master_path="data/raw/fund_master.csv"):
    """Explores the fund master dataset."""
    print(f"\n--- Exploring Fund Master ({fund_master_path}) ---")
    if not os.path.exists(fund_master_path):
        print(f"{fund_master_path} not found. Skipping exploration.")
        return None
    
    try:
        df = pd.read_csv(fund_master_path)
        print("Unique Fund Houses:", df.get('fund_house', pd.Series()).nunique())
        print("Unique Categories:", df.get('category', pd.Series()).nunique())
        print("Unique Sub-Categories:", df.get('sub_category', pd.Series()).nunique())
        print("Unique Risk Grades:", df.get('risk_grade', pd.Series()).nunique())
        return df
    except Exception as e:
        print(f"Error exploring fund master: {e}")
        return None

def validate_amfi_codes(fund_master_df, nav_history_path="data/raw/nav_history.csv"):
    """Validates that AMFI codes in fund master exist in nav history."""
    print(f"\n--- Validating AMFI Codes against {nav_history_path} ---")
    if fund_master_df is None:
        print("Fund master data is missing. Cannot validate AMFI codes.")
        return
        
    if not os.path.exists(nav_history_path):
        print(f"{nav_history_path} not found. Cannot validate AMFI codes.")
        return
        
    try:
        nav_df = pd.read_csv(nav_history_path)
        
        # Assuming the AMFI code column might be named 'scheme_code' or 'amfi_code'
        # Let's try to infer column names or use defaults
        fm_code_col = 'scheme_code' if 'scheme_code' in fund_master_df.columns else 'amfi_code' if 'amfi_code' in fund_master_df.columns else None
        nav_code_col = 'scheme_code' if 'scheme_code' in nav_df.columns else 'amfi_code' if 'amfi_code' in nav_df.columns else None
        
        if fm_code_col and nav_code_col:
            fm_codes = set(fund_master_df[fm_code_col].dropna().unique())
            nav_codes = set(nav_df[nav_code_col].dropna().unique())
            
            missing_codes = fm_codes - nav_codes
            print(f"Total codes in Fund Master: {len(fm_codes)}")
            print(f"Total codes in NAV History: {len(nav_codes)}")
            print(f"Codes in Fund Master but missing in NAV History: {len(missing_codes)}")
            
            print("\nData Quality Summary:")
            if len(missing_codes) == 0:
                print("Excellent: All AMFI codes from the fund master are present in the NAV history.")
            else:
                print(f"Warning: {len(missing_codes)} AMFI codes from the fund master are missing in the NAV history. This might indicate incomplete historical data or inactive funds.")
        else:
            print("Could not identify the AMFI code column ('scheme_code' or 'amfi_code') in one or both datasets.")
            
    except Exception as e:
        print(f"Error validating AMFI codes: {e}")

if __name__ == "__main__":
    load_and_inspect_datasets()
    fm_df = explore_fund_master()
    validate_amfi_codes(fm_df)
