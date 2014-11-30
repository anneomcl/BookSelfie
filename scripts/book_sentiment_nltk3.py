from urllib import request
import nltk, re, pprint
from nltk import word_tokenize, FreqDist, pos_tag


crime_and_punishment = [('Raskolnikov', 778), ('man', 474), ('Sonia', 399), ('time', 367), ('Razumihin', 346), ('Dounia', 317), ('Ivanovna', 300), ('Petrovitch', 286), ('something', 282), ('room', 274), ('way', 255), ('nothing', 246), ('face', 235), ('eyes', 226), ('door', 224), ('Katerina', 215), ('Porfiry', 206), ('Svidrigailov', 204), ('woman', 200), ('moment', 196), ('day', 192), ('mother', 189), ('head', 188), ('Well', 182), ('Pyotr', 172), ('Do', 171), ('course', 169), ('money', 167), ('people', 165), ('hand', 153), ('Yes', 152), ('hands', 148), ('anything', 143), ('word', 133), ('thing', 133), ('heart', 132), ('life', 130), ('everything', 130), ('yesterday', 129), ('mind', 128), ('Rodya', 127), ('sister', 126), ('Pulcheria', 123), ('Alexandrovna', 121), ('question', 117), ('Avdotya', 115), ('Romanovna', 115), ('His', 114), ('Oh', 113), ('God', 113)]
phaedrus = [('love', 87), ('art', 84), ('soul', 83), ('truth', 76), ('nature', 72), ('lover', 68), ('Socrates', 63), ('man', 62), ('speech', 58), ('Project', 56), ('Phaedrus', 54), ('work', 46), ('men', 42), ('Lysias', 41), ('knowledge', 39), ('Plato', 38), ('time', 38), ('world', 38), ('\\r\\n\\r\\nSOCRATES', 37), ('way', 36), ('mind', 35), ('(', 35), ('beauty', 34), ('things', 33), ('Gutenberg-tm', 33), ('\\r\\nand', 31), ('life', 30), ('place', 30), ('power', 30), ('god', 29), ('reason', 29), ('form', 28), ('others', 28), ('words', 28), (')', 27), ('works', 25), ('desire', 24), ('word', 24), ('discourse', 24), ('manner', 23), ('Yes', 23), ('name', 22), ('God', 21), ('sort', 21), ('gods', 20), ('charioteer', 20), ('sense', 20), ('anything', 20), ('use', 20), ('philosophy', 20)]
civilization_and_discontents = [('life', 88), ('man', 80), ('culture', 66), ('guilt', 63), ('love', 59), ('s', 59), ('sense', 59), ('way', 58), ('men', 56), ('civilization', 55), ('ego', 53), ('happiness', 53), ('conscience', 46), ('nature', 45), ('world', 44), ('development', 44), ('towards', 42), ('super-ego', 41), ('part', 37), ('instinct', 35), ('instincts', 33), ('work', 33), ('time', 33), ('people', 32), ('others', 31), ('aggression', 29), ('In', 28), ('mind', 27), ('power', 27), ('things', 26), ('process', 26), ('something', 25), ('state', 25), ('fact', 24), ('view', 24), ('aggressiveness', 24), ('feeling', 23), ('form', 23), ('course', 22), ('satisfaction', 22), ('kind', 22), ('nothing', 22), ('relations', 22), ('aim', 21), ('father', 21), ('means', 21), ('religion', 21), ('child', 20), ('human', 20), ('point', 20)]



'''
url = "http://www.gutenberg.org/files/1636/1636.txt"
response = request.urlopen(url)
raw = response.read()

f =open('BookSelfie/text/','w')
f.write(str(raw))
f.close()

tokens = str(word_tokenize(raw))
f = open('tokenized_text','w')
f.write(tokens)
f.close()


f = open('tokenized_text','r')
words = f.read()
f.close()
#fdist1 = FreqDist(tokens)
#print(fdist1.most_common(100))'''
