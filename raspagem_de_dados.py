import requests
from bs4 import BeautifulSoup


url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/593/palmas-to"
def temperatura(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,"html.parser")
    temperaturaMinima = soup.find(id='min-temp-1')
    temperaturaMaxima = soup.find(id='max-temp-1')
    return temperaturaMaxima.text, temperaturaMinima.text

# Mostra resultados #
print(' Temperatura Mínima: ', temperatura(url)[1])
print(' Temperatura Mínima: ', temperatura(url)[0])
