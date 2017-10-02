import bs4 as bs
from urlib2 import urlopen

sauce = urllib.request.urlopen('https://www.sec.gov/rules/other/4-460list.htm').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
print(soup)
