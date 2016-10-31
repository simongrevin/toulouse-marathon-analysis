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
    for row in rows:
        
        # get all the cols
        cols = row.find_all('td')
        
        if len(cols) > 0:
            
            # getting only the relevant info : spot;bib number;name;time
            line = cols[0].getText() + ";" + cols[1].getText() + ";" + cols[2].getText() +";" + cols[3].getText() + ";" + cols[4].getText() + "\n"
            
            # writing to result file
            file.write(line.encode('utf-8'))

file.close();

print("finished !")