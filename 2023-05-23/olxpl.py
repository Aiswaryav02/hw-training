import requests
import json
from parsel import Selector
from playwright.sync_api import sync_playwright
headers = {
    "accept": "*/*",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
    "referer": "https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"
  
}
property_data = []
def olx_data(data):
    property_count = 0
    if 'data' in data:
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
            # print(json.dumps(items, indent=5))
            property_count += 1
            property(items['url'], property_count,items)
            # with open("olxpl.json", 'a') as data_file:
            #     data_file.write(json.dumps(items, indent=5) + '\n')
        
    return property_count

def property(url, count,items):
    print(url)
    
    with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)

            # property_data = {}

            desc_element = page.query_selector('xpath=//div[@data-aut-id="itemDescriptionContent"]')
            if desc_element is not None:
                descriptions = desc_element.text_content()
            else:
                descriptions = None
            price_element = page.query_selector('xpath=//span[@data-aut-id="itemPrice"]')
            if price_element is not None:
                price = price_element.text_content()
            else:
                price = None
            title_element = page.query_selector('xpath=//h1[@data-aut-id="itemTitle"]')
            if title_element is not None:
                property_title = title_element.text_content()
            else:
                property_title = None
            bathrooms_element = page.query_selector('xpath=//span[@data-aut-id="value_bathrooms"]')
            if bathrooms_element is not None:
                bathrooms = bathrooms_element.text_content()
            else:
                bathrooms = None
            bedrooms_element = page.query_selector('xpath=//span[@data-aut-id="value_rooms"]')
            if bedrooms_element is not None:
                bedrooms = bedrooms_element.text_content()
            else:
                bedrooms = None
            type_element = page.query_selector('xpath=//span[@data-aut-id="value_type"]')
            if type_element is not None:
                property_type = type_element.text_content()
            else:
                property_type = None
            bread_element = page.query_selector('xpath=//div[@data-aut-id="breadcrumb"]')
            if bread_element is not None:
                breadcrumbs = bread_element.text_content()
            else:
                breadcrumbs = None
            loc_element = page.query_selector('xpath=//div[@data-aut-id="itemLocation"]')
            if loc_element is not None:
                location = loc_element.text_content()
            else:
                location = None
            sname_element = page.query_selector('xpath=//div[@data-aut-id="profileCard"]')
            if sname_element is not None:
                seller_name = sname_element.text_content()
            else:
                seller_name = None
            id_element = page.query_selector('xpath=//div[@class="_1-oS0"]')
            if id_element is not None:
                property_id = id_element.text_content()
                sliced_id = property_id[6:-14]
            else:
                property_id = None
                sliced_id = None
                
            property_dict = {
                'url': url,
                'property_title': property_title,
                'property_id': sliced_id,
                'breadcrumbs': breadcrumbs,
                'price': price,
                'descriptions': descriptions,
                'seller_name': seller_name,
                'location': location,
                'property_type': property_type,
                'bathrooms':bathrooms,
                'bedrooms':bedrooms,
                'image_url': items['image_url']  ,
                }
            property_data.append(property_dict)
            with open('property_data2.json', 'w') as file:
                json.dump(property_data, file,indent=2)
           
                   
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
