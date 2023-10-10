import pprint
pp = pprint.PrettyPrinter(indent=4)
import requests
url = 'http://localhost:8000/cumulus/transactions/'

def get_transactions():
    data = requests.get(url)
    print(data.status_code)
    dict = {}
    
    for transaction in data.json():
        if transaction['description'] == "":
            continue
        if transaction['description'] in dict:
            # dict[transaction['description']].append(transaction)
            dict[transaction['description']] += 1
        else:
            # dict[transaction['description']] = [transaction]
            dict[transaction['description']] = 1
    
    for key in list(dict):
        if dict[key] >= 5:
            print(key)
        else:
            dict.pop(key)
    
    
    print("len of dict", len(list(dict)))
    pp.pprint(dict)
    return dict

# get_transactions()


def identify_income():
    data = requests.get(url).json()
    credits = {}
    
    for tx in data:
        if tx['details'] == "CREDIT":
            if tx['description'] in credits:
                credits[tx['description']].append(tx)
            else:
                credits[tx['description']] = [tx]
    
    pp.pprint(credits)
    return credits

identify_income()
    
    
    
    
    

