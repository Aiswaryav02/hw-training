import requests
import json
from parsel import Selector

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
url = "https://www.edeka24.de/"


def mainlist():

    response = requests.get(url, headers=headers)
    print(response.status_code)

    selector = Selector(response.text)
    prices = selector.xpath('//div[@class="price"]/text()').extract()
    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
    categories = selector.xpath("//h2[@class='is-h2 text-align-center bordered-bottom']/text()").extract()
    category = ', '.join(categories)
    print("category:", category)
    for i in range(len(prices)):
        price = prices[i].strip()
        title = titles[i].strip()
        image = images[i].strip()

        print("Title:", title)
        print("Price:", price)
        print("Image:", image)
        print()  



def grocery():
    def coffeetea():
        cof_url = url + "Lebensmittel/Kaffee-Tee/"
        response = requests.get(cof_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def coffeewholebeans():
        cofb_url = url + "Lebensmittel/Kaffee-Tee/Kaffee-ganze-Bohnen/"
        response = requests.get(cofb_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()


    def grndcofinstant():
        grndinst_url = url + "Lebensmittel/Kaffee-Tee/Kaffee-gemahlen-Instant/"
        response = requests.get(grndinst_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
           

    def coffeepods():
        cofpods_url = url + "Lebensmittel/Kaffee-Tee/Kaffeepads/"
        response = requests.get(cofpods_url, headers=headers)
        selector = Selector(response.text)

        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def coffeecapsules():

        cofcaps_url = url + "Lebensmittel/Kaffee-Tee/Kaffeekapseln/"
        response = requests.get(cofcaps_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def cappuccino():

        cofcaps_url = url + "Lebensmittel/Kaffee-Tee/Cappuccino-Kakao/"
        response = requests.get(cofcaps_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def cfilter():

        filt_url = url + "Lebensmittel/Kaffee-Tee/Filter/"
        response = requests.get(filt_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def milkcraalter():

        milk_url = url + "Lebensmittel/Kaffee-Tee/Milch-Sahne-Alternativen/"
        response = requests.get(milk_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def tee():

        tee_url = url + "Lebensmittel/Kaffee-Tee/tee/"
        response = requests.get(tee_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def beverages():

        bev_url = url + "Lebensmittel/Getraenke/"
        response = requests.get(bev_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def energydrinks():

        eng_url = url + "Lebensmittel/Getraenke/Energydrinks/"
        response = requests.get(eng_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def juices():

        juice_url = url + "Lebensmittel/Getraenke/Saefte/"
        response = requests.get(juice_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def beer():

        beer_url = url + "Wein-Spirituosen/Bier/"
        response = requests.get(beer_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def cola():

        cola_url = url + "Lebensmittel/Getraenke/Cola/"
        response = requests.get(cola_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def icetea():

        icetea_url = url + "Lebensmittel/Getraenke/Eistee/"
        response = requests.get(icetea_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def instdrinks():

        inst_url = url + "Lebensmittel/Getraenke/Instant-Getraenke/"
        response = requests.get(inst_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def lemonade():

        lemon_url = url + "Lebensmittel/Getraenke/Limonade/"
        response = requests.get(lemon_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def syrup():

        syrup_url = url + "Lebensmittel/Getraenke/Sirup/"
        response = requests.get(syrup_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def water():

        water_url = url + "Lebensmittel/Getraenke/Wasser/"
        response = requests.get(water_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def backingdessert():

        backing_url = url + "/Lebensmittel/Backen-Desserts/"
        response = requests.get(backing_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def margarine():

        marg_url = url + "Lebensmittel/Backen-Desserts/Margarine-Butterschmalz/"
        response = requests.get(marg_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def flavor():

        flavor_url = url + "Lebensmittel/Backen-Desserts/Aromen-Vanille/"
        response = requests.get(flavor_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def baking():

        baking_url = url + "Lebensmittel/Backen-Desserts/Backmischungen/"
        response = requests.get(baking_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def bakingdecor():

        bakingd_url = url + "Lebensmittel/Backen-Desserts/Backzutaten-Dekor/"
        response = requests.get(bakingd_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def gelingagent():

        gel_url = url + "Lebensmittel/Backen-Desserts/Geliermittel-Sahnefest/"
        response = requests.get(gel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def couvertur():

        cov_url = url + "Lebensmittel/Backen-Desserts/Kuvertuere-Glasur/"
        response = requests.get(cov_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def flour():

        flr_url = url + "Lebensmittel/Backen-Desserts/Mehl-Backpulver-Hefe/"
        response = requests.get(flr_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def nuts():

        nuts_url = url + "Lebensmittel/Backen-Desserts/Nuesse-mehr/"
        response = requests.get(nuts_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def pudding():

        pud_url = url + "Lebensmittel/Backen-Desserts/Pudding-Dessert/"
        response = requests.get(pud_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sugar():

        sug_url = url + "Lebensmittel/Backen-Desserts/Zucker-Zuckerersatz/"
        response = requests.get(sug_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def breakfast():

        brkfst_url = url + "Lebensmittel/Fruehstueck-Snacks/"
        response = requests.get(brkfst_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def bun():

        bun_url = url + "Lebensmittel/Fruehstueck-Snacks/Brot-Broetchen/"
        response = requests.get(bun_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def finishedcake():

        fcake_url = url + "Lebensmittel/Fruehstueck-Snacks/Fertige-Kuchen/"
        response = requests.get(fcake_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def crispbread():

        crisp_url = url + "Lebensmittel/Fruehstueck-Snacks/Knaeckebrot-Zwieback-Getreidewaffeln/"
        response = requests.get(crisp_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def museli():

        mus_url = url + "Lebensmittel/Fruehstueck-Snacks/Muesli-Fruchtriegel/"
        response = requests.get(mus_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def creals():

        cre_url = url + "Lebensmittel/Fruehstueck-Snacks/Muesli-Cerealien/"
        response = requests.get(cre_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def honey():

        honey_url = url + "Lebensmittel/Fruehstueck-Snacks/Honig/"
        response = requests.get(honey_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def jam():

        jam_url = url + "Lebensmittel/Fruehstueck-Snacks/Konfituere-Fruchtaufstriche/"
        response = requests.get(jam_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def cheese():

        cheese_url = url + "Lebensmittel/Fruehstueck-Snacks/Kaese-cremes/"
        response = requests.get(cheese_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def spread():

        spread_url = url + "Lebensmittel/Fruehstueck-Snacks/Streichcreme-Aufstrich/"
        response = requests.get(spread_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sausage():

        sausage_url = url + "Lebensmittel/Fruehstueck-Snacks/Wurst-Schinken/"
        response = requests.get(sausage_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def continental():

        con_url = url + "Lebensmittel/Wuerzmittel-Bruehen/"
        response = requests.get(con_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def oil():

        oil_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Oele/"
        response = requests.get(oil_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def broths():

        broths_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Bruehen/"
        response = requests.get(broths_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def vinegar():

        vin_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Essig/"
        response = requests.get(vin_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def seasoning():

        sea_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Feinwuerzmittel/"
        response = requests.get(sea_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def spice():

        spice_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Gewuerze-Kraeuter/"
        response = requests.get(spice_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def salad():

        salad_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Salatkraeuter/"
        response = requests.get(salad_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def salt():

        salt_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Salz/"
        response = requests.get(salt_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def soup():

        soup_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Suppeneinlagen/"
        response = requests.get(soup_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def mix():

        mix_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Wuerzmischungen/"
        response = requests.get(mix_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sauce():

        sauce_url = url + "Lebensmittel/Sossen/"
        response = requests.get(sauce_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def fxpro():

        fix_url = url + "Lebensmittel/Sossen/Fix-Produkte/"
        response = requests.get(fix_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def readys():

        ready_url = url + "Lebensmittel/Sossen/Fertige-Sossen/"
        response = requests.get(ready_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def fundsauce():
        fund_url = url + "Lebensmittel/Sossen/Fonds-Sossenbinder/"
        response = requests.get(fund_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def barbeque():
        brbq_url = url + "Lebensmittel/Sossen/Grillsaucen/"
        response = requests.get(brbq_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def ketchup():
        ket_url = url + "Lebensmittel/Sossen/Ketchup-Mayonnaise/"
        response = requests.get(ket_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def saladsp():
        salsp_url = url + "Lebensmittel/Sossen/Salatdressing/"
        response = requests.get(salsp_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def mustard():
        mustard_url = url + "Lebensmittel/Sossen/Senf-Meerrettich/"
        response = requests.get(mustard_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def stirfry():
        stir_url = url + "Lebensmittel/Sossen/Sossen-zum-Anruehren/"
        response = requests.get(stir_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def tomato():
        tom_url = url + "Lebensmittel/Sossen/Tomatensosse-Pesto/"
        response = requests.get(tom_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def relish():
        rel_url = url + "Lebensmittel/Sossen/Wuerzsaucen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sidedish():
        rel_url = url + "Lebensmittel/Beilagen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def rice():
        rel_url = url + "Lebensmittel/Beilagen/Reis/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def pasta():
        rel_url = url + "Lebensmittel/Beilagen/Nudeln/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def seed():
        rel_url = url + "Lebensmittel/Beilagen/Samen-Saaten/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def patties():
        rel_url = url + "Lebensmittel/Beilagen/Bratlinge/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def legumes():
        rel_url = url + "Lebensmittel/Beilagen/Huelsenfruechte/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def dmppot():
        rel_url = url + "Lebensmittel/Beilagen/Knoedel-Kartoffelprodukte/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def canned():
        rel_url = url + "Lebensmittel/Konserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def cannedfish():
        rel_url = url + "Lebensmittel/Konserven/Fischkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def cannedmeat():
        rel_url = url + "Lebensmittel/Konserven/Fischkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def cannedveg():
        rel_url = url + "Lebensmittel/Konserven/Gemuesekonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def fruit():
        rel_url = url + "Lebensmittel/Konserven/Obstkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def olive():
        rel_url = url + "Lebensmittel/Konserven/Oliven-Peperoni/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sausagejar():
        rel_url = url + "Lebensmittel/Konserven/Wuerstchen-im-Glas/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def cansas():
        rel_url = url + "Lebensmittel/Konserven/Wurstkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sweet():
        rel_url = url + "Lebensmittel/Suess-Salzig/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def chocolate():
        rel_url = url + "Lebensmittel/Suess-Salzig/Schokoriegel/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def candy():
        rel_url = url + "Lebensmittel/Suess-Salzig/Bonbons-Kaugummi/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def fruitgum():
        rel_url = url + "Lebensmittel/Suess-Salzig/Fruchtgummi-Lakritz/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def chotreat():
        rel_url = url + "Lebensmittel/Suess-Salzig/Schoko-Leckereien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def barcho():
        rel_url = url + "Lebensmittel/Suess-Salzig/Tafelschokolade/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        # prices = selector.xpath('//div[@class="price"]/text()').extract()
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def chips():
        rel_url = url + "Lebensmittel/Suess-Salzig/Chips-Knabbereien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def pastry():
        rel_url = url + "Lebensmittel/Suess-Salzig/Gebaeck-Kekse-Waffeln/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def nutsdry():
        rel_url = url + "Lebensmittel/Suess-Salzig/Nuesse-getrocknete-Fruechte/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def easter():
        rel_url = url + "Lebensmittel/Suess-Salzig/Oster-Leckereien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def readymeals():
        rel_url = url + "Lebensmittel/Fertiggerichte"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def dishstir():
        rel_url = url + "Lebensmittel/Fertiggerichte/Gerichte-zum-Anruehren/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def dishheat():
        rel_url = url + "Lebensmittel/Fertiggerichte/Gerichte-zum-Erhitzen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def soupmix():
        rel_url = url + "Lebensmittel/Fertiggerichte/Suppen-zum-Anruehren/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def soupstew():
        rel_url = url + "Lebensmittel/Fertiggerichte/Suppen-Eintoepfe/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def drinkmeal():
        rel_url = url + "Lebensmittel/Fertiggerichte/Trinkmahlzeiten/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def international():
        rel_url = url + "Lebensmittel/Internationales/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    coffeetea()
    coffeewholebeans()
    grndcofinstant()
    coffeepods()
    coffeecapsules()
    cappuccino()
    cfilter()
    milkcraalter()
    tee()
    beverages()
    energydrinks()
    juices()
    beer()
    cola()
    icetea()
    instdrinks()
    lemonade()
    syrup()
    water()
    backingdessert()
    margarine()
    flavor()
    baking()
    bakingdecor()
    gelingagent()
    couvertur()
    nuts()
    pudding()
    sugar()
    breakfast()
    bun()
    finishedcake()
    crispbread()
    museli()
    creals()
    honey()
    jam()
    nuts()
    cheese()
    spread()
    sausage()
    continental()
    oil()
    broths()
    vinegar()
    seasoning()
    spice()
    salad()
    salt()
    soup()
    mix()
    sauce()
    fxpro()
    readys()
    fundsauce()
    barbeque()
    ketchup()
    saladsp()
    mustard()
    stirfry()
    tomato()
    relish()
    sidedish()
    rice()
    pasta()
    seed()
    patties()
    legumes()
    dmppot()
    canned()
    cannedfish()
    cannedmeat()
    cannedveg()
    fruit()
    olive()
    sausagejar()
    cansas()
    sweet()
    candy()
    fruitgum()
    chotreat()
    barcho()
    chips()
    pastry()
    nutsdry()
    easter()
    readymeals()
    dishstir()
    dishheat()
    soupmix()
    soupstew()
    drinkmeal()
    international()


def organic_products():
    def organic_brands():
        rel_url = url + "Bio-Produkte/Bio-Marken/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def unpackpro():
        rel_url = url + "Bio-Produkte/Bio-Marken/Unverpackt/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def edkabio():
        rel_url = url + "Bio-Produkte/Bio-Marken/EDEKA-Bio/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def bauckhof():
        rel_url = url + "Bio-Produkte/Bio-Marken/Bauckhof/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def beshorg():
        rel_url = url + "Bio-Produkte/Bio-Marken/BESH-Bio-Konserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def gepa():
        rel_url = url + "Bio-Produkte/Bio-Marken/Gepa/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def recgood():
        rel_url = url + "Bio-Produkte/Bio-Marken/Rettergut/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def veganz():
        rel_url = url + "Bio-Produkte/Bio-Marken/Veganz/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def orggrounments():
        rel_url = url + "Bio-Produkte/Bio-Marken/Bio-Gourmet/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def hipbio():
        rel_url = url + "Bio-Produkte/Bio-Marken/Hipp-Bio/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def littlunch():
        rel_url = url + "Bio-Produkte/Bio-Marken/Little-Lunch/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def more():
        rel_url = url + "Bio-Produkte/Bio-Marken/mehr/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def alnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def bakingalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Backzutaten-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def readymeals():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Fertiggerichte-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
          

    def pastalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Gebaeck-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def ketchupalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Ketchup-Gewuerzsaucen-von-Alnatura"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturapreserve():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Konserven-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def muselialnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Muesliriegel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturapasta():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Nudeln-Sossen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def ricealnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Reis-Beilagen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturasweet():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Suesses-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def sugaralnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Zucker-Suessstoff-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturababy():
        rel_url = url + "Alnatura-Produkte-Babynahrung/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturabroths():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Gewuerze-Bruehen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def nutalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Nuesse-Fruechte-Samen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturaoil():
        rel_url = url + "/Bio-Produkte/Lebensmittel-von-Alnatura/Pflanzenoel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturabrkfst():
        rel_url = url + "Bio-Produkte/Fruehstuecksartikel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def breadalnatura():
        rel_url = url + "Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Brot-Knaecke-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnaturaspread():
        rel_url = url + "/Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Brotaufstriche-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def fuitspreadalnatura():
        rel_url = url + "Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Fruchtaufstriche-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def muscereal():
        rel_url = url + "/Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Muesli-Cerealien-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    def alnatdrinks():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
   
    def alnaturacoffee():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Kaffee-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def alnaturajuice():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Saefte-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()  
    def alnaturatea():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Tee-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def alnaturawine():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Weine-von-Alnatura"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()

    organic_brands()
    unpackpro()
    edkabio()
    bauckhof()
    beshorg()
    gepa()
    recgood()
    veganz()
    orggrounments()
    hipbio()
    littlunch()
    more()
    alnatura()
    bakingalnatura()
    readymeals()
    pastalnatura()
    ketchupalnatura()
    alnaturapreserve()
    muselialnatura()
    alnaturapasta()
    ricealnatura()
    alnaturasweet()
    sugaralnatura()
    alnaturababy()
    alnaturabroths()
    nutalnatura()
    alnaturaoil()
    alnaturabrkfst()
    breadalnatura()
    alnaturaspread()
    fuitspreadalnatura()
    muscereal()
    alnatdrinks()
    alnaturacoffee()
    alnaturajuice()
    alnaturatea()
    alnaturawine()


def winespirit():

    def redwine():
        rel_url = url + "Wein-Spirituosen/Rotwein/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def germany():
        rel_url = url + "Wein-Spirituosen/Rotwein/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def italy():
        rel_url = url + "Wein-Spirituosen/Rotwein/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def france():
        rel_url = url + "Wein-Spirituosen//Rotwein/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()   
    def spain():
        rel_url = url + "Wein-Spirituosen/Rotwein/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def austria():
        rel_url = url + "Wein-Spirituosen/Rotwein/Oesterreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def overseas():
        rel_url = url + "Wein-Spirituosen//Rotwein/Uebersee/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
         
    def organic():
        rel_url = url + "Wein-Spirituosen/Rotwein/Bio//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def portugal():
        rel_url = url + "Wein-Spirituosen/Rotwein/Portugal/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def whitevine():
        rel_url = url + "Wein-Spirituosen/Weisswein/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def germanyw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def italyw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def francew():
        rel_url = url + "Wein-Spirituosen//Weisswein/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()       
        print("france")
        for price in prices:
            print(price.strip())   
    def spainw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()  
    def austriaw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Oesterreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def overseasw():
        rel_url = url + "Wein-Spirituosen//Weisswein/Uebersee/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def organicw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Bio//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def portugalw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Portugal/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def rosewine():
        rel_url = url + "Wein-Spirituosen/Ros-weine/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def germanyr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def italyr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def francer():
        rel_url = url + "Wein-Spirituosen//Ros-weine/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()  
    def spainr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def austriar():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Oesterreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def overseasr():
        rel_url = url + "Wein-Spirituosen//Ros-weine/Uebersee/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()  
    def organicr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Bio//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def portugalr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Portugal/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def sparkling():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/"
        response = requests.get(rel_url, headers=headers)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def nonalcoholic():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/ALKOHOLFREI/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def germanysp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def italysp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def francesp():
        rel_url = url + "Wein-Spirituosen//Sekt-Prosecco/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def spainsp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def organisp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Bio/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()               
    def spirit():
        rel_url = url + "Wein-Spirituosen/Spirituosen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def fires():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Braende/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()                
    def brandy():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Brandy-Weinbrand/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def cognac():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Cognac/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()                
    def gin():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Gin/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def grappa():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Grappa/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()               
    def liquire():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Likoere-Bitter//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def mead():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Met/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def canmix():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Mixgetraenke-in-Dosen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()                
    def party():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Party-Schnaps/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def port():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Portwein-Sherry-Likoerwein/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print() 
    def rum():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Rum/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()              
    def tequila():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Tequila/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def vodka():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Vodka/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()
    def vermouth():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Wermut/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()              
    def whisky():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Whisky/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
        images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
        categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
        category = ', '.join(categories)

        print("category:", category)
        for i in range(len(prices)):
            price = prices[i].strip()
            title = titles[i].strip()
            image = images[i].strip()

            print("Title:", title)
            print("Price:", price)
            print("Image:", image)
            print()


    redwine()
    germany()
    italy()
    france()
    spain()
    austria()
    overseas()
    organic()
    portugal()
    whitevine()
    germanyw()
    italyw()
    francew()
    spainw()
    austriaw()
    overseasw()
    organicw()
    portugalw()
    rosewine()
    germanyr()
    italyr()
    francer()
    spainr()
    austriar()
    overseasr()
    organicr()
    portugalr()
    sparkling()
    nonalcoholic()
    germanysp()
    italysp()
    francesp()
    spainsp()   
    organisp() 
    spirit()
    fires()
    brandy()
    cognac()
    gin()
    grappa()
    liquire()
    mead()
    canmix()
    party()
    port()
    rum()
    tequila()
    vodka()
    vermouth()
    whisky()

def drugstore():
	def babytoddlers():
	    rel_url = url + "Drogerie/Baby-Kleinkind/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	babytoddlers()

	def folowmilk():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Folgemilch/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	folowmilk()

	def glass():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Glaesschen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	glass()

	def childishes():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Kinder-Gerichte/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	childishes()

	def childrinks():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Kinder-Getraenke/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	childrinks()
	def carewash():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Pflegen-Waschen-Reinigen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	carewash()

	def snacks():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Snacks/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	snacks()
	def diapers():
	    rel_url = url + "Drogerie/Baby-Kleinkind/Windeln/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	diapers()
	def personlhyg():
	    rel_url = url + "Drogerie/Koerperhygiene/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	personlhyg()

	def stationary():
	    rel_url = url + "Drogerie/Koerperhygiene/Papierware/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	stationary()

	def pads():
	    rel_url = url + "Drogerie/Koerperhygiene/Binden-Slipeinlagen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	pads()

	def blader():
	    rel_url = url + "Drogerie/Koerperhygiene/Blasenschwaeche/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	blader()

	def cond():
	    rel_url = url + "Drogerie/Koerperhygiene/Kondome-Gleitgele/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	cond()
	def contlens():
	    rel_url = url + "Drogerie/Koerperhygiene/Kontaktlinsen-Pflege/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	contlens()

	def shaving():
	    rel_url = url + "Drogerie/Koerperhygiene/Rasier-Enthaarungsartikel/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	shaving()
	def travelsize():
	    rel_url = url + "Drogerie/Koerperhygiene/Reisegroessen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	travelsize()

	def tampons():
	    rel_url = url + "Drogerie/Koerperhygiene/Tampons/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	tampons()
	def wound():
	    rel_url = url + "Drogerie/Koerperhygiene/Wundschutz/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	wound()
	def personlhygeine():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	personlhygeine()

	def malegoom():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Maennerpflege/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	malegoom()

	def cream():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Creme-Lotions/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	cream()

	def deodrant():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Deodorant/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	deodrant()

	def shower():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Duschgel-Badezusatz/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	shower()
	def faccare():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Gesichtspflege/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	faccare()

	def hairsty():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Haarstyling-Schutz/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	hairsty()
	def hand():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Hand-Fusspflege/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	hand()

	def soap():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Seife/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	soap()
	def shampoo():
	    rel_url = url + "Drogerie/Drogerie/Koerperpflege-oxid/Shampoo-Spuelung//"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	shampoo()

	def sun():
	    rel_url = url + "Drogerie/Koerperpflege-oxid/Sonnenschutz/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	sun()
	def dental():
	    rel_url = url + "Drogerie/Drogerie/Koerperpflege-oxid/Zahnpflege/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	dental()
	def cleanwash():
	    rel_url = url + "Drogerie/Reinigen-Waschen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	cleanwash()

	def dishwash():
	    rel_url = url + "Drogerie/Reinigen-Waschen/Geschirrspuelmittel/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	dishwash()

	def roomf():
	    rel_url = url + "Drogerie/Reinigen-Waschen/Raumerfrischer/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	roomf()

	def cleanser():
	    rel_url = url + "Drogerie/Reinigen-Waschen/Reiniger/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	cleanser()

	def texpaint():
	    rel_url = url + "Drogerie/Reinigen-Waschen/Textilfarbe/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	texpaint()
	def laundry():
	    rel_url = url + "Drogerie/Reinigen-Waschen/Waschmittel/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	laundry()
	def fabsoft():
	    rel_url = url + "Drogerie/Reinigen-Waschen/Weichspueler-Waescheparfuem/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	fabsoft()

	def petfood():
	    rel_url = url + "Drogerie/Tiernahrung/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	petfood()

	def drycat():
	    rel_url = url + "Drogerie/Tiernahrung/Katzenfutter-trocken/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	drycat()

	def catfood():
	    rel_url = url + "Drogerie/Tiernahrung/Katzenfutter-nass/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	catfood()

	def catsnacks():
	    rel_url = url + "Drogerie/Tiernahrung/Katzen-Snacks/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	catsnacks()

	def drydog():
	    rel_url = url + "Drogerie/Tiernahrung/Hundefutter-trocken/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	drydog()
	def wetdog():
	    rel_url = url + "Drogerie/Tiernahrung/Hundefutter-nass/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	wetdog()
	def dogsnack():
	    rel_url = url + "Drogerie/Tiernahrung/Hunde-Snacks/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	dogsnack()
	def rodent():
	    rel_url = url + "Drogerie/Tiernahrung/Nagerfutter/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	rodent()
	def birdseed():
	    rel_url = url + "Drogerie/Tiernahrung/Vogelfutter/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	birdseed()
	def house():
	    rel_url = url + "Drogerie/Haushalt/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	house()

	def pouch():
	    rel_url = url + "Drogerie/Haushalt/Beutel-Folien/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	pouch()

	def kitchen():
	    rel_url = url + "Drogerie/Haushalt/Kuechenzubehoer/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	kitchen()

	def other():
	    rel_url = url + "Drogerie/Haushalt/Weitere-Haushaltsartikel/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	other()

	def battery():
	    rel_url = url + "Drogerie/Haushalt/Batterien/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	battery()
	def fuel():
	    rel_url = url + "Drogerie/Haushalt/Brennstoffe-Grill/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	fuel()
	def insect():
	    rel_url = url + "Drogerie/Haushalt/Insektenschutz/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	insect()
	def candle():
	    rel_url = url + "Drogerie/Haushalt/Kerzen-Teelichter-Duftkerzen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	candle()
	def papertow():
	    rel_url = url + "Drogerie/Haushalt/Kuechenrollen/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	papertow()
	def station():
	    rel_url = url + "Drogerie/Haushalt/Schreibwaren/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[4]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	station()
	def dietary():
	    rel_url = url + "Drogerie/Nahrungsergaenzungsmittel/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	dietary()
	def smoking():
	    rel_url = url + "Drogerie/Haushalt/Raucherbedarf/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	smoking()
	def acold():
	    rel_url = url + "Drogerie/Erkaeltung/"
	    response = requests.get(rel_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	    images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	    categories = selector.xpath("//div[@class='breadcrumb']/ul/li[3]/a/text()").extract()
	    category = ', '.join(categories)

	    print("category:", category)
	    for i in range(len(prices)):
	        price = prices[i].strip()
	        title = titles[i].strip()
	        image = images[i].strip()

	        print("Title:", title)
	        print("Price:", price)
	        print("Image:", image)
	        print()

	acold()
def leisure():
	rel_url = url + "Nonfood-Angebote/"
	response = requests.get(rel_url, headers=headers)
	selector = Selector(response.text)
	prices = selector.xpath('//div[@class="price"]/text()').extract()
	titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	categories = selector.xpath("//div[@class='breadcrumb']/ul/li[2]/a/text()").extract()
	category = ', '.join(categories)

	print("category:", category)
	for i in range(len(prices)):
	    price = prices[i].strip()
	    title = titles[i].strip()
	    image = images[i].strip()

	    print("Title:", title)
	    print("Price:", price)
	    print("Image:", image)
	    print()
def foroffice():
	rel_url = url + "Fuers-Buero/"
	response = requests.get(rel_url, headers=headers)
	selector = Selector(response.text)
	prices = selector.xpath('//div[@class="price"]/text()').extract()
	titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	categories = selector.xpath("//div[@class='breadcrumb']/ul/li[2]/a/text()").extract()
	category = ', '.join(categories)

	print("category:", category)
	for i in range(len(prices)):
	    price = prices[i].strip()
	    title = titles[i].strip()
	    image = images[i].strip()

	    print("Title:", title)
	    print("Price:", price)
	    print("Image:", image)
	    print()
def spcloffer():
	rel_url = url + "Sonderaktion-oxid"
	response = requests.get(rel_url, headers=headers)
	selector = Selector(response.text)
	prices = selector.xpath('//div[@class="price"]/text()').extract()
	titles = selector.xpath('//div[@class="product-details"]/a/h2/text()').extract()
	images = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	categories = selector.xpath("//a[@data-title='Sonderaktion']/text()").extract()
	category = ', '.join(categories)
	print("category:", category)
	for i in range(len(prices)):
	    price = prices[i].strip()
	    title = titles[i].strip()
	    image = images[i].strip()

	    print("Title:", title)
	    print("Price:", price)
	    print("Image:", image)
	    print()

mainlist()
grocery()
organic_products()
winespirit()
drugstore()
leisure()
foroffice()
spcloffer()
