import nltk.data
from afinn import Afinn
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet

afinn = Afinn()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
word_tokenizer = RegexpTokenizer(r'\w+')

def analyze_text(text_file, output_file):
    fp = open(text_file, 'r', encoding="utf8")
    data = fp.read()
    output_csv = open(output_file, 'w', encoding='utf8')
    output_csv.write('Sentence,AFINN Score of Sentence\n')
    afinnarray = []
    sentences = tokenizer.tokenize(data)

    count = 0
    for s in sentences:
        count += 1
        output_csv.write(str(count) + ',' + str(afinn.score(s)) + '\n')
    
    output_csv.close()

def enhanced_analyze_text(text_file, output_file):
    fp = open(text_file, 'r', encoding="latin-1")
    data = fp.read()

    output_csv = open(output_file, 'w', encoding='utf8')
    output_csv.write('Sentence,AFINN Score of Sentence,Sentence Word Count,Total AFINN Score,Total Words\n')
    afinnarray = []
    sentences = tokenizer.tokenize(data)
    count = 0
    total_afinn_score = 0
    total_number_of_words = 0
    for s in sentences:
        count += 1
        # print('-' * 10 + s + '\n')
        sentence_score = 0
        words = word_tokenizer.tokenize(s)
        for w in words:
            if afinn.score(w) == 0:
                sentence_score += enhanced_afinn(w)
            else:
                sentence_score += afinn.score(w)
        
        total_afinn_score += sentence_score
        total_number_of_words += len(words)
        output_csv.write(','.join((str(count), str(sentence_score), str(len(words)), \
            str(total_afinn_score), str(total_number_of_words))) + '\n')
        # print('|'.join((str(sentence_score), s)))

    output_csv.close()



def enhanced_afinn(word):
    """Returns AFINN score enhanced by WordNet of a word

    Args:
        word (string): the input word

    Returns:
        float: the average AFINN score of the WordNet synonyms of a word
    """
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    total_scored_words = 0
    total_afinn_score = 0
    for s in synonyms:
        if afinn.score(s) != 0:
            total_scored_words += 1
            total_afinn_score += afinn.score(s)
    
    if total_scored_words == 0:
        return 0.0
    else:
        return float(total_afinn_score/total_scored_words)

def print_synonyms_and_antonyms(word):
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    print("Synonyms: " + str(synonyms) + '\n')
    print("Antonyms: " + str(antonyms) + '\n')

def print_sentence(text_file, sentence_number):
    with open(text_file, 'r', encoding="latin-1") as fp:
        data = fp.read()
        sentences = tokenizer.tokenize(data)
        print(sentences[sentence_number - 1])

def main():
    # analyze_text('aquila.txt', 'aquila.csv')
    # analyze_text('symmachus.txt', 'symmachus.csv')
    # analyze_text('theodotion.txt', 'theodotion.csv')
    # print(enhanced_afinn('flesh'))
    # print(enhanced_afinn('man'))
    # print(enhanced_afinn('wise'))
    # print(enhanced_afinn('lust'))
    # print(enhanced_afinn('beneficial'))
    # print(enhanced_afinn('sinful'))
    # enhanced_analyze_text('aquila.txt', 'aquila.csv')
    # enhanced_analyze_text('symmachus.txt', 'symmachus.csv')
    # enhanced_analyze_text('theodotion.txt', 'theodotion.csv')
    # enhanced_analyze_text('gone-with-the-wind.txt', 'gone-with-the-wind.csv')
    # enhanced_analyze_text('snow-white.txt', 'snow-white.csv')
    # enhanced_analyze_text('the-great-gatsby.txt', 'the-great-gatsby.csv')
    pass

if __name__ == '__main__':
    main()
