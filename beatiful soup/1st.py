from bs4 import BeautifulSoup
import requests

url="https://www.york.ac.uk/teaching/cws/wws/webpage1.html"

page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
soup.find('i')
print(soup.find_all('i'))
