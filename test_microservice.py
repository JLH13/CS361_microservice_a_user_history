import requests

def add_conversion(user_id, from_currency, to_currency, amount, result):
    url = 'http://127.0.0.1:5000/add_conversion'
    data = {
        'user_id': user_id,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount': amount,
        'result': result
    }
    response = requests.post(url, json=data)
    print(response.json())

def get_history(user_id):
    url = f'http://127.0.0.1:5000/get_history/{user_id}'
    response = requests.get(url)
    print(response.json())

def reset_history():
    url = 'http://127.0.0.1:5000/reset_history'
    response = requests.post(url)
    print(response.json())

if __name__ == '__main__':
    user_id = 'user123'
    
    add_conversion(user_id, 'USD', 'EUR', 100, 84)
    add_conversion(user_id, 'EUR', 'USD', 100, 118)
    
    get_history(user_id)
