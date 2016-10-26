from bs4 import BeautifulSoup
import urllib

for i in range(1,28):
    r = urllib.urlopen('https://www.marathon-toulousemetropole.fr/fr/resultats?type=&annee=&nom=&prenom=&club=&dossard=&sexe=&categorie=&p='+str(i)).read()
    soup = BeautifulSoup(r, "html5lib")
    rows = soup.find_all('table')[0].find_all('tr')
    file = open('result.txt', 'a')
    for tr_soup in rows:
        col = tr_soup.find_all('td')
        if len(col) > 0:
            print(col[0].getText() + ";" + col[1].getText() + ";" + col[2].getText() + ";" + col[4].getText() + ";\n")
            line = col[0].getText() + ";" + col[1].getText() + ";" + col[2].getText() + ";" + col[4].getText() + ";\n"
            file.write(line.encode('utf-8'))

file.close();