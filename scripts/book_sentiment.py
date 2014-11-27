from urllib import request
import nltk, re, pprint
from nltk import word_tokenize, FreqDist


url = "http://www.gutenberg.org/files/2554/2554.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = word_tokenize(raw)
print(raw[:75])

#print("Tokens: " + str(tokens[:10]))
#pos_tokens = nltk.pos_tag(tokens)
#print(pos_tokens)
#for word in pos_tokens:

#fdist1 = FreqDist(tokens)
#print(fdist1.most_common(100))
