# Capstone Project I - Mutual Fund Analytics

## Overview
This repository contains the ETL (Extract, Transform, Load) pipelines and initial setup for a Mutual Fund Analytics project. The initial objectives focused on scaffolding the project directory, setting up the Python environment, fetching live Mutual Fund NAVs from a public API, and establishing a basic data ingestion framework.

## Project Structure
- `data/raw/`: Contains the raw CSV datasets, including both generated mock data and live NAV data.
- `data/processed/`: Intended for cleaned and transformed datasets.
- `notebooks/`: Directory for exploratory data analysis (EDA) using Jupyter Notebooks.
- `sql/`: Directory for storing analytical SQL queries.
- `dashboard/`: Intended to contain code related to the final analytics dashboard.
- `reports/`: For generated reports, visualizations, and summaries.

## Python Scripts

### 1. `live_nav_fetch.py`
This script connects to the public [mfapi.in](https://www.mfapi.in/) to fetch the latest, live Net Asset Value (NAV) data for 6 key mutual fund schemes (e.g., SBI Bluechip, HDFC Top 100). It parses the JSON response and stores the historical data locally in `data/raw/` as raw CSV files.

### 2. `generate_mock_data.py`
A utility script used to generate randomized dummy data for 10 foundational CSV datasets (such as `fund_master.csv`, `nav_history.csv`, `investor_demographics.csv`, etc.). This was used to mock up the required dataset dependencies for the project environment.

### 3. `data_ingestion.py`
The primary data ingestion and validation script that:
- Reads all available CSV files in the `data/raw/` directory.
- Inspects their data types and dimensions (`.shape`, `.dtypes`, `.head()`).
- Explores the categorical structures within the `fund_master` dataset.
- Validates the data quality by cross-referencing AMFI codes between `fund_master.csv` and `nav_history.csv` to ensure no historical data is missing.

## Setup & Usage Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/kvasuaditya-star/BLUESTOCK.git
   cd BLUESTOCK
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Install the required libraries (pandas, requests, etc.) via:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scripts:**
   Generate the mock datasets, fetch the live NAVs, and run the ingestion validation:
   ```bash
   python generate_mock_data.py
   python live_nav_fetch.py
   python data_ingestion.py
   ```
