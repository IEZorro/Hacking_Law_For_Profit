from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://www.sec.gov/rules/other/4-460list.htm")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.td)
