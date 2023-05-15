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

# Send a GET request to the URL
url="https://www.olx.in//item/2bhk-semi-furnished-flat-for-rent-at-olavanna-iid-1593111598"
response = session.get(url,headers=headers)
print(response.text)
match = re.search(r'bm-verify=([^&]+)', response.text)
if match:
    bm_verify = match.group(1)
    print("bm-verify value:::::::", bm_verify)
else:
    print("bm-verify value not found in response text")
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
match2 =re.search(r'pow=([^&]+)',response.text)
if match2:
    poww = match.group(1)
    print("pow value:::::::", poww)
else:
    print("bbbbbbbbbbbbbbb")
print('bm-verify:', bm_verify)
# print('pow:', pow_value)
# print('i:', i_value) 
# print('j:', j_value)

selector = Selector(response.text)
descriptions= selector.xpath('//div[@data-aut-id="itemDescriptionContent"]//text()').extract()
# print(descriptions)
