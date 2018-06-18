
#Jake Runyan 2018
#https://github.com/runyanjake/beautifulsoup
#using beautifulsoup version 4.5.3
#https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/
#using >>>>>>>python3<<<<<< and installing with pip3

from bs4 import BeautifulSoup as bs

with open("./testhtml/rltrades.html") as file:
    soup = bs(file, "html5lib")

    title = soup.title
    titlestr = soup.title.string

    print("Title is: " + str(titlestr))

    index = 1
    c = soup.find_all("div", {"class": "contents"}) #contents portion
    for item in c: 
        tradebox = item.find_all("div", {"class": "new"}) #the single tb holding trades
        for newtrade in tradebox:
            trade = newtrade.find_all("div", recursive=False)
            link = trade[0]
            haves = trade[1].get_text()
            wants = trade[2].get_text()
            time = trade[3].get_text()
            print(str(index) + ": " + str(haves) + "\n")
            index = index + 1

    file.close()