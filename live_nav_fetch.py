import requests
import pandas as pd
import os

def fetch_and_save_nav(scheme_code, scheme_name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Check if 'data' key exists in response
        if 'data' in data and data['data']:
            df = pd.DataFrame(data['data'])
            
            # The API returns 'date' and 'nav'
            # Let's add scheme_code and scheme_name for clarity
            df['scheme_code'] = scheme_code
            df['scheme_name'] = scheme_name
            
            output_dir = os.path.join("data", "raw")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f"nav_{scheme_code}.csv")
            
            df.to_csv(output_file, index=False)
            print(f"Successfully saved NAV data for {scheme_name} ({scheme_code}) to {output_file}")
        else:
            print(f"No NAV data found for {scheme_name} ({scheme_code})")
            
    except Exception as e:
        print(f"Failed to fetch data for {scheme_name} ({scheme_code}): {e}")

if __name__ == "__main__":
    schemes = {
        "125497": "HDFC Top 100 Direct",
        "119551": "SBI Bluechip",
        "120503": "ICICI Bluechip",
        "118632": "Nippon Large Cap",
        "119092": "Axis Bluechip",
        "120841": "Kotak Bluechip"
    }
    
    print("Starting NAV fetch for key schemes...")
    for code, name in schemes.items():
        fetch_and_save_nav(code, name)
    print("NAV fetch complete.")
