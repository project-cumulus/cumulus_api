import os
import csv
import requests
url = 'http://localhost:8000/cumulus/transactions/'

bank_accounts = {"Chase2020", "Chase5999"}
credit_cards = {"Chase7777"}

def save_transaction_data(file_name):
    file = open(f"../data/{file_name}", "r")
    data = list(csv.DictReader(file, delimiter=","))
    file.close()
    return data

def get_date(date_string):
    year = date_string[6:]
    month = date_string[0:2]
    day = date_string[3:5]
    return f"{year}-{month}-{day}"

def process_bank_account_transactions(data, account):
    for transaction in data:
        if transaction['Type'] == "ACCT_XFER":
            continue
        
        date = get_date(transaction['Posting Date'])
        account_id = 0
        
        if account == "Chase2020":
            account_id = 2
        
        if account == "Chase5999":
            account_id = 1
        
        payload = {
            'details': transaction['Details'],
            'currency': 'USD',
            'date': date,
            'description': transaction['Description'],
            'amount': transaction['Amount'],
            'type': transaction['Type'],
            'balance': transaction['Balance'],
            'account_id': account_id
        }
        
        x = requests.post(url, json = payload)
        print(x.status_code)
        print(x.text)
            
        if x.status_code != 200:
            print("Error in process_bank_account_transactions, unable to proceed")
            return
        

def process_credit_card_transactions(data, account):
    for transaction in data:
        transaction_date = get_date(transaction['Transaction Date'])
        account_id = 0
        
        if account == "Chase7777":
            account_id = 3 
        
        payload = {
            'date': transaction_date,
            'currency': 'USD',
            'description': transaction['Description'],
            'category': transaction['Category'],
            'amount': transaction['Amount'],
            'type': transaction['Type'],
            'account_id': account_id            
        }
        
        x = requests.post(url, json = payload)
        print(x.status_code)
        print(x.text)
        
        if x.status_code != 200:
            print("ERROR in process_credit_card_transactions, unable to proceed")
            return

files = os.listdir("../data/")

print(files)
for filename in files:
    if filename[-3:] != "CSV":
        print("File is not in the correct CSV format... skipping")
        continue
    
    account = filename[0:9]
    transaction_data = save_transaction_data(filename)
    print(len(transaction_data))
    
    if account in bank_accounts:
        process_bank_account_transactions(transaction_data, account)
    
    if account in credit_cards:
        process_credit_card_transactions(transaction_data, account)


