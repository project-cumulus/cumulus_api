import os
import csv
import requests
url = 'http://localhost:8000/subscriptions/chase_transactions/'

bank_accounts = {"Chase0070", "Chase2158"}
credit_cards = {"Chase7070"}

def save_transaction_data(file_name):
    file = open(file_name, "r")
    data = list(csv.DictReader(file, delimiter=","))
    file.close()
    return data

def get_date(date_string):
    year = date_string[6:]
    month = date_string[0:2]
    day = date_string[3:5]
    return f"{year}-{month}-{day}"

def process_bank_account_transactions(data):
    for transaction in data:
        if transaction['Type'] == "ACCT_XFER":
            continue
        
        date = get_date(transaction['Posting Date'])
        
        payload = {
            'account': "",
            'account_type': 'bank_account',
            'details': transaction['Details'],
            'currency': 'USD',
            'date': date,
            'description': transaction['Description'],
            'amount': transaction['Amount'],
            'type': transaction['Type'],
            'balance': transaction['Balance']
        }
        
        x = requests.post(url, json = payload)
        print(x.status_code)
        print(x.text)

def process_credit_card_transactions(data):
    for transaction in data:
        transaction_date = get_date(transaction['Transaction Date'])
        
        payload = {
            'date': transaction_date,
            'description': transaction['Description'],
            'category': transaction['Category'],
            'amount': transaction['Amount'],
            'type': transaction['Type']
        }
        
        x = requests.post(url, json = payload)
        print(x.status_code)
        print(x.text)

files = os.listdir()

for filename in files:
    if filename[-3:] != "CSV":
        continue
    
    transaction_data = save_transaction_data(filename)
    print(len(transaction_data))
    
    if filename[0:9] in bank_accounts:
        process_bank_account_transactions(transaction_data)
    
    if filename[0:9] in credit_cards:
        process_credit_card_transactions(transaction_data)


