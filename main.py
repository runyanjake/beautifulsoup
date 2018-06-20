
#Jake Runyan 2018
#https://github.com/runyanjake/beautifulsoup
#using beautifulsoup version 4.5.3
#https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/
#using >>>>>>>python3<<<<<< and installing with pip3

from bs4 import BeautifulSoup as bs
import urllib


# r = urllib.request.urlopen('https://www.rl-trades.com/')
# ck = r.getheader('Set-Cookie')
# print("Cookie: " + str(ck))

import requests
# url = 'https://www.rl-trades.com/'
url = 'https://pythonprogramming.net/parsememcparseface/'
r = requests.get(url)
ck = r.cookies #this does return a RequestsCookieJar[] object, not sure if it has anything inside
r2 = requests.get(url, cookies=ck)
print(r2)
print(r2.content)

# import requests
# url2 = 'https://www.rl-trades.com/'
# r = urllib.request.urlopen(url2)
# ck = r.getheader('Set-Cookie')
# headers = {
#     "Method":"GET",
#     "Pragma":"no-cache",
#     "Cookie": ck,
#     'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
# }
# html2 = requests.get(url2, headers=headers).content
# soup2 = bs(html2, "html5lib")
# print(soup2)


# sentdex's tutorial
# this works for the example website https://pythonprogramming.net/parsememcparseface/ but not for rltrades
# URL = 'http://www.rl-trades.com/'
# sauce = urllib.request.urlopen(URL).read()
# soup2 = bs(sauce, 'html5lib')
# print(soup2)
# exit(0)

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




# with open("./testhtml/rltrades.html") as file:
#     soup = bs(file, "html5lib")
#     index = 1

#     for item in soup.find_all("div", {"class": "contents"}): 
#         for newtrade in item.find_all("div", {"class": "new"}):
#             trade = newtrade.find_all("div", recursive=False)
#             link = ""
#             for l in newtrade.find_all("a", href=True):
#                 link = l['href']
#             haves = trade[1].get_text()
#             wants = trade[2].get_text()
#             time = trade[3].get_text()
#             print(str(index) + ": [" + link + "; " + haves + "; " + wants + "; " + time + "]\n")
#             index = index + 1

#     file.close()