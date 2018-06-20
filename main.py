
#Jake Runyan 2018
#https://github.com/runyanjake/beautifulsoup
#using beautifulsoup version 4.5.3
#https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/
#using >>>>>>>python3<<<<<< and installing with pip3

from bs4 import BeautifulSoup as bs

# import requests
# #Requesting Website with requests
# r = requests.get("https://www.rl-trades.com/")
# print("\n\n\n\n")
# print("Status Code: " + str(r.status_code))
# print("Text: " + str(r.text))
# print("Content: " + str(r.content))
# print("\n\n\n\n")

import urllib
#Requesting Website with urllib's urlopen
# returns just "b''"?
# with urllib.request.urlopen("http://www.rl-trades.com/") as response:
#     html = response.read()
#     print("\n\n\n\n")
#     print(html)
#     print("\n\n\n\n")


#Requesting Website with urllib's urlretrive
#returns: <_io.TextIOWrapper name='/var/folders/tw/5r3fybdx4s7412b_l445s1c00000gn/T/tmp6kdpa9rf' mode='r' encoding='UTF-8'>
# local_filename, headers = urllib.request.urlretrieve("http://www.rl-trades.com/")
# html = open(local_filename)
# print("\n\n\n\n")
# print(html)
# print("\n\n\n\n")




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