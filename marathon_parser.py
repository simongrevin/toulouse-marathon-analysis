from bs4 import BeautifulSoup
import urllib
import sys

if len(sys.argv) < 3:
	print("Need the year and number of pages parameters")
	sys.exit()

year = sys.argv[1]
nb_pages = sys.argv[2]

# result file
file = open('marathon_'+ year +'_results.csv', 'a')
header = "place;bib number;name;category;time\n"
file.write(header.encode('utf-8'))
print("writing csv file")

# loop on all pages
for i in range(1, int(nb_pages)+2):

    print("writing page " + str(i) + "...")

    # open url
    url = urllib.urlopen('https://www.marathon-toulousemetropole.fr/fr/resultats?type=&annee='+year+'&nom=&prenom=&club=&dossard=&sexe=&categorie=&p='+str(i)).read()
    soup = BeautifulSoup(url, "html.parser")

    # get all the rows
    rows = soup.find_all('table')[0].find_all('tr')

    # for each row
    for row in rows:

        # get all the cols
        cols = row.find_all('td')

        if len(cols) > 0:

            # getting only the relevant info : spot;bib number;name;category;time
            line = cols[0].getText() + ";" + cols[1].getText() + ";" + cols[2].getText() +";" + cols[3].getText() + ";" + cols[4].getText() + "\n"

            # writing to result file
            file.write(line.encode('utf-8'))

file.close();

print("finished !")
