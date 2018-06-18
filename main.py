
#Jake Runyan 2018
#https://github.com/runyanjake/beautifulsoup
#using beautifulsoup version 4.5.3
#https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/
#using >>>>>>>python3<<<<<< and installing with pip3

from bs4 import BeautifulSoup as bs

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