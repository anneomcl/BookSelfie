import requests
import bs4
import re

def get_author_birthplace(book_id):
    response = requests.get('https://www.goodreads.com/author/show/' + book_id)
    soup = bs4.BeautifulSoup(response.text)
    something = soup.select('.bigGreyBoxContent')
    something = str(something)
    #print(something)
    soup = bs4.BeautifulSoup(something)
    something = soup.select('.dataTitle')
    if(len(something) > 0):
        something = str(something[0].nextSibling)
        if("in " in something):
            something = something.split("in ",1)[1].strip()
        return something
    else:
        return None


x = '1069006'
#get_original_publication_year(x)
get_author_birthplace(x)