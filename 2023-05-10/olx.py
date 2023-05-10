import requests
import json
from parsel import Selector

headers = {
    "accept": "*/*",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
    "referer": "https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"
  
}
# proxy_servers = {
#   'http': 'http://localhost:7777',
#   'https': 'http://localhost:7777',
# }

def olx_data(data):
    property_count = 0
    for i in data['data']:
        items = {
            'property_name': i['title'],
            'property_id': i['ad_id'],
            'price': float(i['price']['value']['display'].replace(',', '').replace('₹', '')),
            'image_url': i['images'][0]['small']['url'],
            'description': i['description'].replace('\n', ' '),
            'property type': i['parameters'][0]['value_name'],
            'location': i['locations_resolved']['SUBLOCALITY_LEVEL_1_name'] + ',' +
                        i['locations_resolved']['ADMIN_LEVEL_3_name'] + ',' +
                        i['locations_resolved']['ADMIN_LEVEL_1_name'],

            'url': "https://www.olx.in/item/" + i['ad_id']
        }

        if i['main_info'] is None:
            print("No data")
        else:
            bathrooms_str = i['main_info'].split("-")[1].replace("Ba", "").strip()
            items['bathrooms'] = int(bathrooms_str) if bathrooms_str.isnumeric() else None
            bedrooms_str = i['main_info'].split("-")[0].replace("Bds", "").strip()
            items['bedrooms'] = int(bedrooms_str) if bedrooms_str.isnumeric() else None
        print(json.dumps(items, indent=5))
        property_count += 1
        property(items['url'], property_count)
        with open("olx5.json", 'a') as data_file:
            data_file.write(json.dumps(items, indent=5) + '\n')
        break
    return property_count

def property(url, count):
    # print(url)
    urls="https://www.olx.in/item/3-bhk-furnished-flat-for-rent-at-meenchanda-calicut-iid-1727454523"
    response = requests.get(url, headers=headers)

    # response = requests.get(url, proxies=proxy_servers)
    selector = Selector(response.text)
    # print("selector",selector)
    # descriptions= selector.xpath('//script[@data-rh="true"]/text()').extract()
    descriptions= response.xpath('//div[@data-aut-id="itemDescriptionContent"]//text()').extract()

    print(descriptions)

    print(f"Property count: {count}, status code: {response.status_code}")
   
    print(response.text)
    print(response.text)
    with open('sampleresponse.txt','a') as f:
        f.write(response.text)
    print("hlo")

   
def paginate_olx_data(page=1):
    paginate_count = 0
    total_count = 1
    url = f"https://www.olx.in/api/relevance/v4/search?category=1723&facet_limit=100&lang=en-IN&location=4058877&location_facet_limit=20&page={page}&platform=web-desktop&relaxedFilters=true&size=40&user=18797a3b7ebx73f05aab"
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    if not json_data:
        print("end of list")
        return
    property_count = olx_data(json_data)
    total_count = property_count*page
    paginate_count += 1
    print(f"Total properties count: {total_count}")
    paginate_olx_data(page + 1)

if __name__ == "__main__":
    paginate_olx_data()

