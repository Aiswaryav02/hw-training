import requests
from parsel import Selector

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
url = "https://www.edeka24.de/"

def url_links(selector, xpath_expression, page=''):
    links = selector.xpath(xpath_expression).extract()
    repeated = set()
    for link in links:
        urls = link.split('?')[0]
        if urls in repeated:
            break
        repeated.add(urls)
        print(urls + "?pgNr=" + str(page))

def main_list(page=1):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    selector = Selector(response.text)
    url_links(selector, '//a/@data-link', page)
    url_links(selector, "//li[@class='nav-item-mobile is-level-2']/a/@href", page)
    url_links(selector, '//li[@class="nav-item-mobile is-level-1"]/span/a/@href', page)
    main_list(page + 1)
main_list(1) 
