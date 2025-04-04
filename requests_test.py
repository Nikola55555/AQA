import requests

response = requests.get(
        url='https://api.spoonacular.com/recipes/complexSearch', 
        headers={'Content-Type': 'application/json'},
        params={'query': 'pasta'
                        })

print(response.status_code)