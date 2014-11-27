import xml.etree.ElementTree as ET
import json

import goodreads_author_scrape



#year is the original publication year
#my_rating is 1-5, if it's 0 then I haven't read it yet
#average_rating is the public rating (1-5)
from scripts import goodreads_scrape

books = []

tree = ET.parse('data/raw_books.xml')
root = tree.getroot()
reviews = root[1]
i=0
for child in reviews:
    year = goodreads_scrape.get_original_publication_year(child[1][0].text)
    place = goodreads_scrape.get_setting(child[1][0].text)
    if(len(child[1][19]) > 0):
        author_birthplace = goodreads_author_scrape.get_author_birthplace(child[1][19][0][0].text)
        if(len(child[1][19][0]) > 0):
            author = child[1][19][0][1].text
            author = author.replace(".", "")
    books.append(dict({'title' : child[1][4].text,
                       'id' : child[1][0].text,
                       'original_pub_year' : year,
                       'my_rating' : child[2].text,
                       'average_rating': child[1][16].text,
                       'setting': place,
                        'author_birthplace': author_birthplace,
                        'author': author}))
    print(i)
    i+=1

#for book in books:
   #print(book['title'], ": ", book['original_pub_year'], book['setting'])

with open('data/parsed_book_data.json','w') as outfile:
    json.dump(books,outfile)