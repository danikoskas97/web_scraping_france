import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


url_2 = f'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris/9.html?giropharm=0'

url = 'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris.html?giropharm=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
bloc = soup.find(class_='pharmacie_bloc_resultat contenu_vert_clair')

bloc_text = bloc.get_text()
print(len(url))




























