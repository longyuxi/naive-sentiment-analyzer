import nltk.data
from afinn import Afinn
from bs4 import BeautifulSoup

f = open("Joseph & Aseneth_ Translated by David Cook.html", "r", encoding="iso-8859-1")
page = f.read()

soup = BeautifulSoup(page, 'html.parser')
chapters = soup.findAll('tbody')[0].findAll('tr')

save_file = open('aseneth.txt', 'a', encoding='utf8')
z = 0

for c in chapters:
    s = c.findAll('td')[0].findAll('blockquote')[0].findAll('p')[0].get_text()
    print(s)
    print('z: ' + str(z))
    save_file.write(s + '\n')
    z+=1