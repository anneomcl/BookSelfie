import nltk, re, pprint
from nltk import word_tokenize, FreqDist, pos_tag

raw = open('text/civ_and_dis','r')
text = raw.read().decode('ascii', 'ignore').encode('ascii')
tokens = word_tokenize(text)
raw.close()

noun_list = list()

pos_tokens = nltk.pos_tag(tokens)
for token in pos_tokens:
    if(token[1] == "NN" or token[1] == "NNS" or token[1] == "NNP" or token[1] == "NNPS"):
        noun_list.append(token[0])

fdist1 = FreqDist(noun_list)
print(fdist1.most_common(50))
