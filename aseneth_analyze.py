import nltk.data
from afinn import Afinn
from nltk.tokenize import RegexpTokenizer

word_tokenizer = RegexpTokenizer(r'\w+')

afinn = Afinn()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("aseneth.txt", 'r', encoding="utf8")
data = fp.readlines()
data = data[2:] # get rid of the first two useless lines

output_csv = open('aseneth_afinn.csv', 'w', encoding='utf8')
output_csv.write('Chapter in Aseneth,AFINN Score of Chapter,Word Count,AFINN Score per Word\n')

afinnarray = []
chapter_number = 1
for chapter in data:
    chapter_word_count = len(word_tokenizer.tokenize(chapter))
    afinnarray.append(afinn.score(chapter))
    output_csv.write(str(chapter_number) + ',' + \
        str(afinn.score(chapter)) + ',' + \
        str(chapter_word_count) + ',' + \
        str(float(afinn.score(chapter))/float(chapter_word_count))+ ',\n')
    chapter_number += 1

output_csv.close()
print(afinnarray)
