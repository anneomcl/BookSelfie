import json

json_data = open("data/parsed_book_data.json").read()
data = json.loads(json_data)

i=0
for item in data:
    if(item['original_pub_year']):
        year = item['original_pub_year']
        if(int(year) >= 1000 and int(year) < 1500):#medieval
            era_color = "#CC00CC"
        elif(int(year) < 1000): #ancient
            era_color = "#FF0000"
        elif(int(year) >= 1500 and int(year) < 1800): #renaissance
            era_color = "#00FF00"
        elif(int(year) >= 1800 and int(year) < 1900): #romantic
            era_color = "#0066FF"
        elif(int(year) >= 1900 and int(year) < 1970): #modern
            era_color = "#00FFFF"
        elif(int(year) >= 1970 and int(year) < 2014): #post-modern
            era_color = "#FFFFFF"
        print('gt50' + str(i) + ": '" + era_color + "',")
    i+=1
