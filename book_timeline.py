import xml.etree.ElementTree as ET
import goodreads_scrape

#year is the original publication year
#my_rating is 1-5, if it's 0 then I haven't read it yet
#average_rating is the public rating (1-5)

books = []

tree = ET.parse('data/raw_books.xml')
root = tree.getroot()
reviews = root[1]

for child in reviews:
    year = goodreads_scrape.get_original_publication_year(child[1][0].text)
    place = goodreads_scrape.get_setting(child[1][0].text)
    books.append(dict({'title' : child[1][4].text,
                       'id' : child[1][0].text,
                       'original_pub_year' : year,
                       'my_rating' : child[2].text,
                       'average_rating': child[1][16].text,
                       'setting': place}))

#for book in books:
    #print(book['title'], ": ", book['original_pub_year'], book['setting'])

f = open('book_data.txt','w')
f.write(str(books))
f.close()