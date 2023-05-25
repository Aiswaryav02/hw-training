import requests
# import json
from parsel import Selector

url= " https://www.dari.ae/en/app/directory?category=projects "
# url="https://www.dari.ae/en/app/directory/project/496"

headers={"accept": "*/*",
         "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
         "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
         "referer":"https://www.dari.ae/",
         }


response = requests.get(url,headers=headers)
print(response.status_code)
# print(response.text)
# data = response.json()


selector = Selector(response.text)

property_title=selector.xpath('//p[@class="MuiTypography-root jss2782 MuiTypography-body1"]//text()').extract()
print(property_title)
property_number=selector.xpath('//p[@class="MuiTypography-root jss3175 MuiTypography-body1"]//text()').extract()
print(property_number)
property_url=f"https://www.dari.ae/en/app/directory/project/{property_number}"
print(property_url)
location=selector.xpath('//p[@class="MuiTypography-root jss3519 MuiTypography-body1"]//text()').extract()
print(location)
percentage_of_completion= selector.xpath('//p[@class="MuiTypography-root jss2098 MuiTypography-body1"]//text()').extract()
print(percentage_of_completion)
property_type=selector.xpath('//span[@class="MuiChip-label"]//text()').extract()
print(property_type)


# data = json.loads(response.text)

# for i in data['data']:
#         properties = {
#             'property_title':i['name'],
#             'property_number': i['id'],
#             'property_type': i['type'],
#             'location': i['districtEn'],
#             'percentage_of_completion' : i['progressPercentage'],

#         }
#         print(json.dumps(properties, indent=5))


