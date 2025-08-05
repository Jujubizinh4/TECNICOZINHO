import requests
from bs4 import BeautifulSoup

# URL do site a ser acessado

url = "https://www.example.com"

# Faz a requisição para o site

response = requests.get(url)

# Verifica se o site respondeu corretamente

if response.status_code == 200:

    # Faz o parser do conteúdo HTML

    soup = BeautifulSoup(response.text, 'html.parser')

    # Pega o conteúdo da tag <title>

    title = soup.title.string

    # Mostra o título na tela

    print("Título da página:", title)

else:

    print("Erro ao acessar o site:", response.status_code)

