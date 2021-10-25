from bs4 import BeautifulSoup
import requests
import bs4

url = "http://basketball-reference.com/players/j/jamesle01.html"
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
test = soup.select('.poptip')
print(test)