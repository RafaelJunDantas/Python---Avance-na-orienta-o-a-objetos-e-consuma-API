import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

res = requests.get(url)

if res.status_code == 200:
    dados = res.json()
    print(f'Tudo certo: {res.status_code}')

    restaurantes = {}
    for item in dados:
        company = item['Company']
        if company not in restaurantes:
            restaurantes[company] = []

        restaurantes[company].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'O erro foi {res.status_code}')
    
# for item in restaurantes['Pizza Hut']:
#     print('-' * 50)
#     print(item)

for company, data in restaurantes.items():
    file_name = f'{company}.json'

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)