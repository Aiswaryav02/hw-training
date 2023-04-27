import requests
import json


headers = {
    "accept": "*/*",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
    "referer": "https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"
}


def Olx_data(data):
    for i in data['data']:
        items = {
            'property_name':i['title'],
            'property_id': i['ad_id'],
            'price': float(i['price']['value']['display'].replace(',', '').replace('₹', '')),
            'image_url': i['images'][0]['small']['url'],
            'description': i['description'].replace('\n', ' '),
            'property type': i['parameters'][0]['value_name'],
            'location': i['locations_resolved']['SUBLOCALITY_LEVEL_1_name'] + ',' +
                        i['locations_resolved']['ADMIN_LEVEL_3_name'] + ',' +
                        i['locations_resolved']['ADMIN_LEVEL_1_name'],
        }
        
        if i['main_info'] is None:
            print("No data")
        else:
            bathrooms_str =i['main_info'].split("-")[1].replace("Ba","").strip()
            items['bathrooms'] = int(bathrooms_str) if bathrooms_str.isnumeric() else None
            bedrooms_str = i['main_info'].split("-")[0].replace("Bds","").strip()
            items['bedrooms'] = int(bedrooms_str) if bedrooms_str.isnumeric() else None

        print(json.dumps(items, indent=5))
        with open("datssaolx.json", 'a') as data_file:
            data_file.write(json.dumps(items,indent=5) + '\n')




for page in range(1,15):  
    url = f"https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page={page}&platform=web-desktop&relaxedFilters=true&size=40&user=18797a3b7ebx73f05aab"
    response = requests.get(url,headers=headers)
    data = json.loads(response.text)
    Olx_data(data)

    
