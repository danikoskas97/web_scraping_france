import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris/414.html?giropharm=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
adress = soup.find(class_='pharmacie_coordonnee')
tel = soup.find(class_='pharmacie_coordonnee_tel')
pharmacies_info = soup.find(class_='pharmacie_info')

all_pharma_info = pharmacies_info.get_text()



print(all_pharma_info)

























