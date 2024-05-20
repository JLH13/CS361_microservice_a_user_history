# CS361_microservice_a_user_history

## Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call:

To add a conversion record:  
Endpoint:   /add_conversion
Method:   POST
Payload (JSON):
```
{
  "user_id": "user123",
  "from_currency": "USD",
  "to_currency": "EUR",
  "amount": 100,
  "result": 84
}
```
Example Call:
```
import requests
url = 'http://127.0.0.1:5000/add_conversion'
data = {
    "user_id": "user123",
    "from_currency": "USD",
    "to_currency": "EUR",
    "amount": 100,
    "result": 84
}
response = requests.post(url, json=data)
print(response.json())
```



## Clear instructions for how to programmatically RECEIVE data from the microservice you implemented:

To retrieve conversion history:
Endpoint: /get_history/<user_id>
Method: GET

Example Call:
```
import requests
user_id = "user123"
url = f'http://127.0.0.1:5000/get_history/{user_id}'
response = requests.get(url)
print(response.json())
```



## UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand:

<img width="731" alt="Screenshot 2024-05-19 at 8 38 31 PM" src="https://github.com/JLH13/CS361_microservice_a_user_history/assets/108007953/0152a28d-a389-4ee2-9eb9-8568a8934705">
