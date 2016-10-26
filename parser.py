from bs4 import BeautifulSoup
import urllib

# result file
file = open('marathon_results.csv', 'a')
header = "place;bib number;name;category;time\n"
file.write(header.encode('utf-8'))

print("writing csv file")

# loop on all pages
for i in range(1,29):
    
    print("writing page " + str(i) + "...")
    
    # open url
    url = urllib.urlopen('https://www.marathon-toulousemetropole.fr/fr/resultats?type=&annee=&nom=&prenom=&club=&dossard=&sexe=&categorie=&p='+str(i)).read()
    soup = BeautifulSoup(url, "html5lib")
    
    # get all the rows
    rows = soup.find_all('table')[0].find_all('tr')
    
    # for each row
    for tr_soup in rows:
        
        # get all the cols
        col = tr_soup.find_all('td')
        
        if len(col) > 0:
            
            # getting only the relevant info : spot;bib number;name;time
            line = col[0].getText() + ";" + col[1].getText() + ";" + col[2].getText() +";" + col[3].getText() + ";" + col[4].getText() + "\n"
            
            # writing to result file
            file.write(line.encode('utf-8'))

file.close();

print("finished !")