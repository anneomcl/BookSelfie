from rauth.service import OAuth1Service, OAuth1Session

CONSUMER_KEY = 'zhrn3T5TKcT4q5ZE1h1kVQ'
CONSUMER_SECRET = 'NsgqMJIqnVUXq5n63uUty83faWl20FQp4vsA5Yb5iQ'

goodreads = OAuth1Service(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    name='goodreads',
    request_token_url='http://www.goodreads.com/oauth/request_token',
    authorize_url='http://www.goodreads.com/oauth/authorize',
    access_token_url='http://www.goodreads.com/oauth/access_token',
    base_url='http://www.goodreads.com/'
)
# head_auth=True is important here; this doesn't work with oauth2 for some reason
request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

authorize_url = goodreads.get_authorize_url(request_token)

print('Visit this URL in your browser: ' + authorize_url)
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = input('Have you authorized me? (y/n) ')

session = goodreads.get_auth_session(request_token, request_token_secret)
id ='10534003-anne'
f = open('my_books','w')
print(session.get('https://www.goodreads.com/review/list?format=xml&v=2&page=1&per_page=200&id='+id).content, file = f)
f.close()

'''# book_id 631932 is "The Greedy Python"
data = {'name': 'to-read', 'book_id': 631932}

# add this to our "to-read" shelf
response = session.post('http://www.goodreads.com/shelf/add_to_shelf.xml', data)
'''

# these values are what you need to save for subsequent access.
ACCEESS_TOKEN = session.access_token
ACCESS_TOKEN_SECRET = session.access_token_secret
