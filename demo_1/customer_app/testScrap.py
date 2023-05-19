import requests
from bs4 import BeautifulSoup

# Изпращане на HTTP GET заявка към уебстраницата
url = 'https://www.abv.bg'
response = requests.get(url)

# Създаване на обект BeautifulSoup от HTML кода на уебстраницата
soup = BeautifulSoup(response.text, 'html.parser')

# Пример за извличане на заглавие и всички връзки от HTML кода
title = soup.title.text
links = soup.find_all('a')

# Извеждане на извлечените данни
print("Заглавие: ", title)
print("Връзки:")
for link in links:
    print(link.get('href'))