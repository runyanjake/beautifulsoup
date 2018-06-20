
#Jake Runyan 2018
#https://github.com/runyanjake/beautifulsoup
#using beautifulsoup version 4.5.3
#https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/
#using >>>>>>>python3<<<<<< and installing with pip3

from bs4 import BeautifulSoup as bs
import urllib

# sentdex's tutorial
# this works for the example website https://pythonprogramming.net/parsememcparseface/ but not for rltrades
# URL = 'http://www.rl-trades.com/'
URL = 'https://coinmarketcap.com'
sauce = urllib.request.urlopen(URL).read()
soup2 = bs(sauce, 'html5lib')
print(soup2)
exit(0)

#TODO: write code for coinmarketcap if it is giving me the right html

with open("./testhtml/rltrades.html") as file:
    soup = bs(file, "html5lib")
    index = 1

    for item in soup.find_all("div", {"class": "contents"}): 
        for newtrade in item.find_all("div", {"class": "new"}):
            trade = newtrade.find_all("div", recursive=False)
            link = ""
            for l in newtrade.find_all("a", href=True):
                link = l['href']
            haves = trade[1].get_text()
            wants = trade[2].get_text()
            time = trade[3].get_text()
            print(str(index) + ": [" + link + "; " + haves + "; " + wants + "; " + time + "]\n")
            index = index + 1

    file.close()