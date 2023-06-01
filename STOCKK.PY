# import requests
# import json
# import time

# API_KEY = "rr2yNp_6onji8GLaxgPcHQPJRBUFdsdw"

# def fetch_stock_data(symbol):
#     url = f"https://api.polygon.io/v2/reference/financials/{symbol}?apiKey={API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# def analyze_stock(symbol):
#     while True:
#         stock_data = fetch_stock_data(symbol)
#         if stock_data:
#          results = stock_data['results']
#         if results:
#             # Extract the required financial ratios
#             # financials = stock_data['results'][0]['financials']
#             financials = results[0].get('financials', {})  # Use .get() to handle missing key
#             pe_ratio = financials['peRatio']
#             ps_ratio = financials['psRatio']
#             roe = financials['roe']
#             de_ratio = financials['deRatio']
#             ev_ebit = financials['evEbit']
#             operating_margin = financials['operatingMargin']
#             quick_ratio = financials['quickRatio']
            
#             # Perform analysis on the financial ratios
#             # You can add your quantitative analysis logic here
            
#             # Example: Print the fetched ratios
#             print(f"P/E Ratio: {pe_ratio}")
#             print(f"P/S Ratio: {ps_ratio}")
#             print(f"Return on Equity (ROE): {roe}")
#             print(f"Debt-to-Equity Ratio (D/E): {de_ratio}")
#             print(f"Enterprise Value to EBIT: {ev_ebit}")
#             print(f"Operating Margin: {operating_margin}")
#             print(f"Quick Ratio: {quick_ratio}")
#         else:
#             print("Financials data not available for this stock.")
        
#         time.sleep(120)  # Sleep for 2 minutes before fetching data again

# def main():
#     stock_name = input("Enter the stock name or ticker symbol: ")
#     analyze_stock(stock_name)

# if __name__ == '__main__':
#     main()

import requests
import json
import time

API_KEY = "rr2yNp_6onji8GLaxgPcHQPJRBUFdsdw"

def fetch_stock_data(symbol):
    url = f"https://api.polygon.io/v2/reference/financials/{symbol}?apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def analyze_stock(symbol):
    while True:
        stock_data = fetch_stock_data(symbol)
        print(stock_data)  # Debug statement
        if stock_data:
            results = stock_data['results']
            if results:
                financials = results[0].get('financials', {})
                pe_ratio = financials.get('peRatio')
                ps_ratio = financials.get('psRatio')
                roe = financials.get('roe')
                de_ratio = financials.get('deRatio')
                ev_ebit = financials.get('evEbit')
                operating_margin = financials.get('operatingMargin')
                quick_ratio = financials.get('quickRatio')

                # Perform analysis on the financial ratios
                # You can add your quantitative analysis logic here

                # Example: Print the fetched ratios
                if pe_ratio is not None:
                    print(f"P/E Ratio: {pe_ratio}")
                else:
                    print("P/E Ratio not available.")

                if ps_ratio is not None:
                    print(f"P/S Ratio: {ps_ratio}")
                else:
                    print("P/S Ratio not available.")

                if roe is not None:
                    print(f"Return on Equity (ROE): {roe}")
                else:
                    print("ROE not available.")

                if de_ratio is not None:
                    print(f"Debt-to-Equity Ratio (D/E): {de_ratio}")
                else:
                    print("D/E Ratio not available.")

                if ev_ebit is not None:
                    print(f"Enterprise Value to EBIT: {ev_ebit}")
                else:
                    print("EV/EBIT not available.")

                if operating_margin is not None:
                    print(f"Operating Margin: {operating_margin}")
                else:
                    print("Operating Margin not available.")

                if quick_ratio is not None:
                    print(f"Quick Ratio: {quick_ratio}")
                else:
                    print("Quick Ratio not available.")
            else:
                print("No results found for this stock.")
        else:
            print("Financials data not available for this stock.")

        time.sleep(120)  # Sleep for 2 minutes before fetching data again

def main():
    stock_name = input("Enter the stock name or ticker symbol: ")
    analyze_stock(stock_name)

if __name__ == '__main__':
    main()
