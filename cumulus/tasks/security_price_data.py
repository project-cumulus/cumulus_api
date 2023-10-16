import json
import csv
import requests
from decouple import config
API_KEY = config("ALPHA_VANTAGE_KEY")

ticker = input("Enter a ticker: \n").upper()
file_type = None
while file_type not in {"csv", "json"}:
    file_type = input("Please enter format (CSV/JSON): \n").lower()

def get_daily_price_data_json(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    json_data = json.dumps(data, indent=4)
     
    with open("0001_SPY_Daily_Time_Series.json", "w") as outfile:
        outfile.write(json_data)
    

def get_daily_price_data_csv(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={API_KEY}&datatype=csv"
    r = requests.get(url)
    data = r.text.split("\r\n")
    for i in range(len(data)):
        row = data[i].split(",")
        data[i] = row

    with open("0001_SPY_Daily_Time_Series.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
        csvfile.close()


if file_type == "csv":
    get_daily_price_data_csv(ticker)
elif file_type == "json":
    get_daily_price_data_json(ticker)

