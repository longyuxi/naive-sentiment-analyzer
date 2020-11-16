import nltk.data
from afinn import Afinn

afinn = Afinn()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt", encoding="utf8")
data = fp.read()
sentences = tokenizer.tokenize(data)
print ('\n-----\n'.join(sentences))

for s in sentences:
    print(s + str(afinn.score(s)))

