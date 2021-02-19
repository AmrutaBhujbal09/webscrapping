import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"

# step 1 : get the html

r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# step 2 : parse the html

soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

# comment object
markup = "<p><!--this is a comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


'''step3  : html tress travasal '''
title = soup.title

# get the title of HTML page
print(title)

# print(type(title.string))
# it gives special type of object which is implemented by BeautifulSoup

# get all paras
paras = soup.findAll('p')
#print(paras)

# get all anchors tags
anchors = soup.findAll('a')

# get all links in html page
for links in anchors:
    print(links.get('href'))


# get classes of any element in the html page
print(soup.find('p')['class'])


# print(soup.find('p')['id'])

# get class with a name lead in the html page
print(soup.find_all("p",class_="lead"))

# get text from tags/soup
print(soup.get_text())

# get all anchors tags
anchors = soup.findAll('a')
all_links = set()
# get all links in html page
for links in anchors:
    if linksText.get('href') != '#':
        link = "https://codewithharry.com" + links.get('href')
        all_links.add(link)
        print(linkText)




