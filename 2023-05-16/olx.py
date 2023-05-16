import requests
import json
from parsel import Selector
import re

session = requests.Session()
headers = {

    "accept": "*/*",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
    "referer": "https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"
  
}

# url="https://www.olx.in/item/2bhk-semi-furnished-flat-for-rent-at-palazhi-kozhikode-iid-1675930329?bm-verify=AAQAAAAH//////hP0ZfiCcwa+bEWpMOAeX4C5NMXZq9BLJM1aE1ByX0MlFtVwmeV6NrFrMNJC1C4UnwROoigxUCdm2Y88TzKGqkveLRl2Nakgz3kgvXR4DwkEkeGk/amQk4+f+g4k6+0ojvWBNvylK5+q6FsVOX12t8BVGycEWj1Z9CaY03oAhlV19kCUXQMysYzGITftAefV2R9cD2pPYeizjTVCTeuFZuuyDzzLU1yoH5N6ssvp7cfiPc2TYg0iOd8mYTTJ/W6EnUMi3/LvJO3AfR5OFQJbazjwX9g9/8jwomJ2vgT7pJBnB30Th3IbGyxECD9XOAWKLECm8hmP1MTDIV8Yx3kbxkjEGJr2xUJWkoVwuZ5qXZM4BnieZrz45SWV/3AOyN70DNkR9bo49MYQW83n5yQnZeSUglA173UkGpoE/j9PLEZz1oNrxVnUd4dNQTcSeDMzTneeSI6GmEd1w=="
urls="https://www.olx.in//item/2bhk-semi-furnished-flat-for-rent-at-olavanna-iid-1593111598"
response = session.get(urls,headers=headers)
print(response.status_code)
print(response.text)
print("___________________________________________")

# regex of bm:verify

match = re.findall(r'"bm-verify":\s*"(.*?)"', response.text)
if match:
    bm_verify = match[0]
    print("value of bm-verify:", bm_verify)
else:
    print("bm-verify not found ")

# regex of content-type
match_content = re.findall(r'xhr.setRequestHeader\("Content-Type", "(.*?)"\);', response.text)
if match_content:
    contentty = match_content[0]
    print("Content type:", contentty)
else:
    print("Not found ")


# regex of var i
match_i = re.findall(r'var i = (\d+);', response.text)
if match_i:
    i = int(match_i[0])
    print("Value of i:", i)
else:
    print("var i not found ")


# regex of var j
match_j = re.findall(r'var j = i \+ Number\("(\d+)" \+ "(\d+)"\);',response.text)
if match_j:
    j_part1 = match_j[0][0]
    j_part2 = match_j[0][1]
    j = i + int(j_part1 + j_part2)
    print("Value of j:",j)
else:
    print("var j not found")

url="https://www.olx.in/_sec/verify?provider=interstitial"
obj={"bm-verify": bm_verify,
    "pow":j}
# response1 = session.get(urls,headers=data)
response1 = session.post(url,headers=headers,data=obj)

print("Status code of bm:verify",response1.status_code)
print("Status code of property url",response.status_code)
print(response1)
selector = Selector(response.text)
descriptions= selector.xpath('//div[@data-aut-id="itemDescriptionContent"]//text()').extract()
print(descriptions)
descriptions= selector.xpath('//div[@data-aut-id="itemDescriptionContent"]//text()').extract()
print(descriptions)
price=selector.xpath('//span[@data-aut-id="itemPrice"]/text()').extract()
print(price)
property_title=selector.xpath('//h1[@data-aut-id="itemTitle"]//text()').extract()
print(property_title)
bathrooms=selector.xpath('//span[@data-aut-id="value_bathrooms"]//text()').extract()
print(bathrooms)
bedrooms=selector.xpath('//span[@data-aut-id="value_rooms"]//text()').extract()
print(bedrooms)
property_type=selector.xpath('//span[@data-aut-id="value_type"]//text()').extract()
print(property_type)
breadcrumbs=selector.xpath('//div[@data-aut-id="breadcrumb"]//text()').extract()
print(breadcrumbs)
