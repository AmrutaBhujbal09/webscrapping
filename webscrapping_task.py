import pandas
from bs4 import BeautifulSoup
import requests

"""
# step 1 : get the html
r = requests.get("file:///E:/tabs/file_data.htm")
htmlContent = r.content
print(htmlContent)



import html5lib
with open("file_data.htm","rb") as f:
    document = html5lib.parse(f)



import html5lib
document = html5lib.parse("file_data.htm")

htmlContent = document.content
print(htmlContent)


"""

from bs4 import BeautifulSoup
import html5lib
myFile=open('file_data.htm','r')
soup = BeautifulSoup(myFile,"html5lib")
#print(soup.prettify())
# step: html tree travarsal

title = soup.title
print(title)

#tables = soup.find_all("table")
#print(tables)

paras = soup.find('b')
print(paras)

h2 = soup.find('h2')
print(h2)


#areaId = soupHandler.find('input', attrs={'name':'form_build_id', 'type':'hidden'})

#CON= soup.find("META", attrs= {'CONTENT':'Chile','NAME':'Country'}).get(Content)


#soup.find(name="Country")