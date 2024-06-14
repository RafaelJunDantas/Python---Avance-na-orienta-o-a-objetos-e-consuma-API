from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    ''''
    Endpoint que exibe Hello World
    '''
    return {
        'Hello': 'World',
        'Teste': 'tudo certo',
    }

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    ''''
    Endpoint de cardapios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    res = requests.get(url)

    if res.status_code == 200:
        dados = res.json()
        print(f'Tudo certo: {res.status_code}')

        if restaurante is None:
            return {
                'dados': dados
            }

        dados_restaurante = []
        for item in dados:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {
            'restaurante': restaurante,
            'cardapio': dados_restaurante
        }
    
    else:
        return {
            'erro': f'{res.status_code} - {res.text}'
        }