from bs4 import BeautifulSoup
import urllib

#for i in range(1,28):


r = urllib.urlopen('https://www.marathon-toulousemetropole.fr/fr/resultats?type=&annee=&nom=&prenom=&club=&dossard=&sexe=&categorie=&p=1').read()
soup = BeautifulSoup(r, "html5lib")
rows = soup.find_all('table')[0].find_all('tr')
for tr_soup in rows:
    col = tr_soup.find_all('td')
    if len(col) > 0:
        print("Nom : " + col[2].getText())
