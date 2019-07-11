from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
import json

def dict(x,y):
	val = {}
	val['name']=x
	val['rating']=y
	return val	 

url= 'https://www.imdb.com/chart/toptv/'
print(url)
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
bs4.BeautifulSoup
title = soup.title
text = soup.get_text()
mytrs = soup.find("tbody", class_="lister-list")

data={}
for tr in mytrs.find_all('tr'):
	x=tr.find("td", { "class" : "titleColumn" })
	y=tr.find("td", { "class" : "ratingColumn imdbRating" })
	x1=x.find("a")
	z=x1.text
	a1=y.text.lstrip("\n")
	a=a1.rstrip("\n")
	data[z]=dict(z,a)
#print (data)

with open(r'Top250shows.json','w') as jsonFile:
	jsonFile.write(json.dumps(data,indent=4))
