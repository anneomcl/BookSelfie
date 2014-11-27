import json
import re
from urllib.request import urlopen
import codecs

json_data = open("data/parsed_book_data.json").read()
data = json.loads(json_data)
reader = codecs.getreader("utf-8")
i=0
for item in data:
    print(i)
    if(item['author_birthplace']):
        location = item['author_birthplace']
        if(" " in location):
            location = re.sub(" ", "+", location, 0, 0)
        if((", ") in location):
            location = re.sub(",", "+,", location, 0, 0)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + \
              location + "&key=AIzaSyDyFuFFfe2jNj_EfDit-kv7PWe1gTdFgPQ"
        json_data = reader(urlopen(url))
        google_maps_json = json.load(json_data)
        print(location)
        if(google_maps_json["results"]):
            item["author_lat"] = google_maps_json["results"][0]["geometry"]["location"]["lat"]
            item["author_lng"] = google_maps_json["results"][0]["geometry"]["location"]["lng"]
    i+=1

with open('data/parsed_book_data.json','w') as outfile:
    json.dump(data,outfile)