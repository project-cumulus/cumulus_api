import csv
import requests

file = open("20231008.CSV", "r")
data = list(csv.DictReader(file, delimiter=","))
file.close()
url = 'http://localhost:8000/subscriptions/chase_transactions/'


for transaction in data:
    posting_date = transaction['Posting Date']
    year = posting_date[6:]
    month = posting_date[0:2]
    day = posting_date[3:5]
    date = f"{year}-{month}-{day}"
    
    payload = {
        'debit': transaction['Details'],
        'posting_date': date,
        'description': transaction['Description'],
        'amount': transaction['Amount'],
        'type': transaction['Type'],
        'balance': transaction['Balance']
    }
    
    x = requests.post(url, json = payload)
    print(x.status_code)
    print(x)


