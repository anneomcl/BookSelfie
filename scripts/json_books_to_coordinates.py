import json
import re
from urllib.request import urlopen
import codecs

json_data = open("data/parsed_book_data.json").read()
data = json.loads(json_data)
reader = codecs.getreader("utf-8")
for item in data:
    if(item['setting']):
        location = item['setting'][0]
        if(" " in location):
            location = re.sub(" ", "+", location, 0, 0)
        if((", ") in location):
            location = re.sub(",", "+,", location, 0, 0)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + \
              location + "&key=AIzaSyDyFuFFfe2jNj_EfDit-kv7PWe1gTdFgPQ"
        json_data = urlopen(url)
        google_maps_json = json.load(reader(json_data))
        if(google_maps_json["results"]):
            item["lat"] = google_maps_json["results"][0]["geometry"]["location"]["lat"]
            item["lng"] = google_maps_json["results"][0]["geometry"]["location"]["lng"]

with open('data/parsed_book_data.json','w') as outfile:
    json.dump(data,outfile)