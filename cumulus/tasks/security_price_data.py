import json
import requests
import pprint
from decouple import config

pp = pprint.PrettyPrinter(indent=4)

API_KEY = config("ALPHA_VANTAGE_KEY")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&outputsize=full&apikey={API_KEY}"
r = requests.get(url)
data = r.json()
pp.pprint(data)

# Serializing json
json_data = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("0001_SPY_Daily_Time_Series.json", "w") as outfile:
    outfile.write(json_data)