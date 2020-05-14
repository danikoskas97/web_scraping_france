from bs4 import BeautifulSoup
import requests
from csv import writer

with open('pharmacy.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Address', 'Telephone number']
    csv_writer.writerow(headers)
    for index in range(1008, 1, -9):
        response = requests.get(f'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris/{index}.html?giropharm=0')
        beauty = BeautifulSoup(response.text, 'html.parser')

        pharmacies = beauty.find_all(class_='pharmacie_info')

        for pharmacy in pharmacies:
            Name = pharmacy.find('h2').get_text().replace('\n', '')
            Address = pharmacy.find(class_='pharmacie_coordonnee').get_text().replace(' ', '').replace('\n', '')
            raw_phone_number = str(str(pharmacy.find(class_='pharmacie_coordonnee_tel').contents[1].get_text()).encode('utf-8', 'ignore'))
            Telephone_number = ""
            for char in raw_phone_number:
                if char.isdigit():
                    Telephone_number+=char
            Telephone_number = Telephone_number[len(Telephone_number)-10:]
            csv_writer.writerow([Name, Address, Telephone_number])

