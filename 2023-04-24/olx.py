import requests
import json
from pymongo import MongoClient



client = MongoClient('localhost',27017)
db = client['olx_taskdb']  # Use or create a database
collection = db['olx_taskcollection']  # Use or create a collection


url = "https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page=1&platform=web-desktop&relaxedFilters=true&size=40&user=18797a3b7ebx73f05aab"
headers={"accept": "*/*",
         "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
         "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
         "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
         "referer":"https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"}
response = requests.get(url,headers=headers)
data = json.loads(response.text)
print(response.status_code)

items_list=[]
for i in data['data']:
            items = {
                'property_id':i['ad_id'],
                'price': i['price']['value']['display'],
                'image_url':i['images'][0]['small']['url'] ,
                'description': i['description'].replace('\n', ' '),
                'location': i['locations_resolved']['SUBLOCALITY_LEVEL_1_name'] +','+
                           i['locations_resolved']['ADMIN_LEVEL_3_name'] +','+
                            i['locations_resolved']['ADMIN_LEVEL_1_name'],
                'property type':i['parameters'][0]['value_name'],
                'bathrooms': i['main_info'].split("-")[1],
                'bedrooms': i['main_info'].split("-")[0], 
                'furnishing':i['parameters'][3]['value_name'], 
                'super buildup area':i['parameters'][5]['value_name'],
                'carpet area':i['parameters'][6]['value_name'],
                'total_sqft': i['main_info'].split("-")[2],    
            }
            items_list.append(items)
            print(json.dumps(items, indent=5))
            # with open("aspx.json", 'a') as data:
            #     data.write(json.dumps(items)  + '\n')
            result = collection.insert_many(items_list)

