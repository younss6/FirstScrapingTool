#Mise à jour des points des équipes en PL
#requests et BeautifulSoup = module pour Scraping

import requests
from bs4 import BeautifulSoup

#lien du site à scrapper
url = 'https://www.skysports.com/premier-league-table'

#données dans l'url
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

league_table = soup.find('table', class_ ='standing-table__table callfn')

#pour "équipe" dans leaguetable, tbody=corps 

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip() #text=spécifie valeur==txt et strip=enleve les sauts de lignes
        pl_points = row.find_all('td', class_ = 'standing-table__cell')[3].text
        print(pl_team, pl_points)

#td class dans le code source = colonne
#[3]= nbr de valeur avec standing-table__cell dont on a besoin