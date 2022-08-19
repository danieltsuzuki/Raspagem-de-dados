import requests
from bs4 import BeautifulSoup


url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/593/palmas-to"
url2 = "https://www.climatempo.com.br/previsao-do-tempo/cidade/1036/balsas-ma"
def temperatura(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,"html.parser")
    temperaturaMinima = soup.find(id='min-temp-1')
    temperaturaMaxima = soup.find(id='max-temp-1')
    return temperaturaMaxima.text, temperaturaMinima.text

# Mostra resultados #
print('Palmas-TO')
print('Temperatura Mínima: ', temperatura(url)[1])
print('Temperatura Mínima: ', temperatura(url)[0],'\n\n')

print('Balsas-MA')
print('Temperatura Mínima: ', temperatura(url2)[1])
print('Temperatura Mínima: ', temperatura(url2)[0])

