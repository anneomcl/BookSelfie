import requests
import bs4
import re

def get_original_publication_year(book_id):
    response = requests.get('https://www.goodreads.com/book/show/' + book_id)
    soup = bs4.BeautifulSoup(response.text)
    something = soup.select('#details')
    something = str(something)
    soup = bs4.BeautifulSoup(something)
    something = soup.select('.greyText')
    something = str(something[0])

    list = re.findall('\d+', something)
    i = 0
    for item in list:
        if len(item) > 2:
            return list[i]
            break
        i+=1

def get_setting(book_id):
    response = requests.get('https://www.goodreads.com/book/show/' + book_id)
    soup = bs4.BeautifulSoup(response.text)
    something = soup.select('#bookDataBox')
    something = str(something)
    soup = bs4.BeautifulSoup(something)
    x = soup.findAll('div', attrs = {'class' : 'infoBoxRowItem'})
    x = str(x)
    soup = bs4.BeautifulSoup(x)
    otherthing = soup.findAll('a', href=True)
    other_list = []
    for item in otherthing:
        if "places" in str(item):
            other_list.append(item)
    place = []
    for item in other_list:
        for child in item:
            place.append(child)

    if soup.findAll('span', attrs = {'class' : 'darkGreyText'}):
        something = soup.findAll('span', attrs = {'class' : 'darkGreyText'})[0].getText()
        something = str(something)
        for letter in something:
            if letter == '(' or letter == ')':
                something = something.replace(letter,"")
        place.append(something)

    return place


x = '52357'
#get_original_publication_year(x)
get_setting(x)