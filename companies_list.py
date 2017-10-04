#This take all text on page and outputs it here. Note for the extra text at the
#beginning of the page and at the end. Assuming companies don't dissapear, we could
#have it start appending to list once it hits the first company name and stop at
#the final one.

# Another problem is that this output is being treated as individual characters and not strings found in a tag.
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://www.sec.gov/rules/other/4-460list.htm")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(html)
print(len(bsObj.text))



import pdfkit
pdfkit.from_url('http://google.com', 'out.pdf')
