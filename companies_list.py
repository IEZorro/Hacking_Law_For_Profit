#This take all text on page and outputs it here. Note for the extra text at the
#beginning of the page and at the end. Assuming companies don't dissapear, we could
#have it start appending to list once it hits the first company name and stop at
#the final one.
# https://www.sec.gov/rules/other/4-460list.htm

#Took Forever

#import necessary modules
import requests, bs4

#call the webpage
res = requests.get('https://www.sec.gov/rules/other/4-460list.htm')

noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml')



#Sends the Text of the web page to the txt file in the txt folder 
writing = open('txt/companies_list.txt', 'w')
writing.write(noStarchSoup.text)
