from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

my_url = "https://docs.python.org/3/reference/index.html"
client = urlopen(my_url)
page_html = client.read()
client.close()
page_soup = soup(page_html,"html.parser")
index = page_soup.findAll("div", {"class":"toctree-wrapper compound"})
# index_items = index[0].ul
indexx = index[0].ul.findAll("li")
for item in indexx:
    print(item.text)
    
