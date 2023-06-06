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
    prices = selector.xpath(
        ' //div[@class="price salesprice"]//text()').extract()

    for price in prices:
        print(price.strip())
    pricenote = selector.xpath(' //p[@class="price-note"]//text()').extract()

    for price in pricenote:
        print(price.strip())

    titles = selector.xpath(
        '//div[@class="product-details"]/a[@class="title"]/h2/text()').extract()
    for title in titles:
        print(title.strip())

    img = selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
    for image in img:
        print(image.strip())


def grocery():
    def coffeetea():

        cof_url = url + "Lebensmittel/Kaffee-Tee/"
        response = requests.get(cof_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_________grocery_____")
        for price in prices:
            print(price.strip())

    def coffeewholebeans():
        cofb_url = url + "Lebensmittel/Kaffee-Tee/Kaffee-ganze-Bohnen/"
        response = requests.get(cofb_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_________coffee wholebean____")
        for price in prices:
            print(price.strip())

    def grndcofinstant():

        grndinst_url = url + "Lebensmittel/Kaffee-Tee/Kaffee-gemahlen-Instant/"
        response = requests.get(grndinst_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_________ground coffee_____")
        for price in prices:
            print(price.strip())

    def coffeepods():

        cofpods_url = url + "Lebensmittel/Kaffee-Tee/Kaffeepads/"
        response = requests.get(cofpods_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("____coffeepods______")
        for price in prices:
            print(price.strip())

    def coffeecapsules():

        cofcaps_url = url + "Lebensmittel/Kaffee-Tee/Kaffeekapseln/"
        response = requests.get(cofcaps_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Coffee capsule_______")
        for price in prices:
            print(price.strip())

    def cappuccino():

        cofcaps_url = url + "Lebensmittel/Kaffee-Tee/Cappuccino-Kakao/"
        response = requests.get(cofcaps_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Cappuccino___")
        for price in prices:
            print(price.strip())

    def cfilter():

        filt_url = url + "Lebensmittel/Kaffee-Tee/Filter/"
        response = requests.get(filt_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Filter___")
        for price in prices:
            print(price.strip())

    def milkcraalter():

        milk_url = url + "Lebensmittel/Kaffee-Tee/Milch-Sahne-Alternativen/"
        response = requests.get(milk_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Milk cream___")
        for price in prices:
            print(price.strip())

    def tee():

        tee_url = url + "Lebensmittel/Kaffee-Tee/tee/"
        response = requests.get(tee_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Tea__")
        for price in prices:
            print(price.strip())

    def beverages():

        bev_url = url + "Lebensmittel/Getraenke/"
        response = requests.get(bev_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Beverages__")
        for price in prices:
            print(price.strip())

    def energydrinks():

        eng_url = url + "Lebensmittel/Getraenke/Energydrinks/"
        response = requests.get(eng_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Energy Drinks___")
        for price in prices:
            print(price.strip())

    def juices():

        juice_url = url + "Lebensmittel/Getraenke/Saefte/"
        response = requests.get(juice_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Juices___")
        for price in prices:
            print(price.strip())

    def beer():

        beer_url = url + "Wein-Spirituosen/Bier/"
        response = requests.get(beer_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___beer____")
        for price in prices:
            print(price.strip())

    def cola():

        cola_url = url + "Lebensmittel/Getraenke/Cola/"
        response = requests.get(cola_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Cola__")
        for price in prices:
            print(price.strip())

    def icetea():

        icetea_url = url + "Lebensmittel/Getraenke/Eistee/"
        response = requests.get(icetea_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Icetea__")
        for price in prices:
            print(price.strip())

    def instdrinks():

        inst_url = url + "Lebensmittel/Getraenke/Instant-Getraenke/"
        response = requests.get(inst_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Instant drinks__")
        for price in prices:
            print(price.strip())

    def lemonade():

        lemon_url = url + "Lebensmittel/Getraenke/Limonade/"
        response = requests.get(lemon_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Lemonade__")
        for price in prices:
            print(price.strip())

    def syrup():

        syrup_url = url + "Lebensmittel/Getraenke/Sirup/"
        response = requests.get(syrup_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___syrup__")
        for price in prices:
            print(price.strip())

    def water():

        water_url = url + "Lebensmittel/Getraenke/Wasser/"
        response = requests.get(water_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Water___")
        for price in prices:
            print(price.strip())

    def backingdessert():

        backing_url = url + "/Lebensmittel/Backen-Desserts/"
        response = requests.get(backing_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__baking dessrt__")
        for price in prices:
            print(price.strip())

    def margarine():

        marg_url = url + "Lebensmittel/Backen-Desserts/Margarine-Butterschmalz/"
        response = requests.get(marg_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Margarine___")
        for price in prices:
            print(price.strip())

    def flavor():

        flavor_url = url + "Lebensmittel/Backen-Desserts/Aromen-Vanille/"
        response = requests.get(flavor_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Flavors__")
        for price in prices:
            print(price.strip())

    def baking():

        baking_url = url + "Lebensmittel/Backen-Desserts/Backmischungen/"
        response = requests.get(baking_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Baking___")
        for price in prices:
            print(price.strip())

    def bakingdecor():

        bakingd_url = url + "Lebensmittel/Backen-Desserts/Backzutaten-Dekor/"
        response = requests.get(bakingd_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Baking decor___")
        for price in prices:
            print(price.strip())

    def gelingagent():

        gel_url = url + "Lebensmittel/Backen-Desserts/Geliermittel-Sahnefest/"
        response = requests.get(gel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___gelling__")
        for price in prices:
            print(price.strip())

    def couvertur():

        cov_url = url + "Lebensmittel/Backen-Desserts/Kuvertuere-Glasur/"
        response = requests.get(cov_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___couverture glaze __")
        for price in prices:
            print(price.strip())

    def flour():

        flr_url = url + "Lebensmittel/Backen-Desserts/Mehl-Backpulver-Hefe/"
        response = requests.get(flr_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___flour __")
        for price in prices:
            print(price.strip())

    def nuts():

        nuts_url = url + "Lebensmittel/Backen-Desserts/Nuesse-mehr/"
        response = requests.get(nuts_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___nuts __")
        for price in prices:
            print(price.strip())

    def pudding():

        pud_url = url + "Lebensmittel/Backen-Desserts/Pudding-Dessert/"
        response = requests.get(pud_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___pudding__")
        for price in prices:
            print(price.strip())

    def sugar():

        sug_url = url + "Lebensmittel/Backen-Desserts/Zucker-Zuckerersatz/"
        response = requests.get(sug_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___sugar__")
        for price in prices:
            print(price.strip())

    def breakfast():

        brkfst_url = url + "Lebensmittel/Fruehstueck-Snacks/"
        response = requests.get(brkfst_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__breakfast__")
        for price in prices:
            print(price.strip())

    def bun():

        bun_url = url + "Lebensmittel/Fruehstueck-Snacks/Brot-Broetchen/"
        response = requests.get(bun_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__bun__")
        for price in prices:
            print(price.strip())

    def finishedcake():

        fcake_url = url + "Lebensmittel/Fruehstueck-Snacks/Fertige-Kuchen/"
        response = requests.get(fcake_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___finished cake__")
        for price in prices:
            print(price.strip())

    def crispbread():

        crisp_url = url + "Lebensmittel/Fruehstueck-Snacks/Knaeckebrot-Zwieback-Getreidewaffeln/"
        response = requests.get(crisp_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___crispbread_")
        for price in prices:
            print(price.strip())

    def museli():

        mus_url = url + "Lebensmittel/Fruehstueck-Snacks/Muesli-Fruchtriegel/"
        response = requests.get(mus_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___museli__")
        for price in prices:
            print(price.strip())

    def creals():

        cre_url = url + "Lebensmittel/Fruehstueck-Snacks/Muesli-Cerealien/"
        response = requests.get(cre_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___cerealsr__")
        for price in prices:
            print(price.strip())

    def honey():

        honey_url = url + "Lebensmittel/Fruehstueck-Snacks/Honig/"
        response = requests.get(honey_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__honey_")
        for price in prices:
            print(price.strip())

    def jam():

        jam_url = url + "Lebensmittel/Fruehstueck-Snacks/Konfituere-Fruchtaufstriche/"
        response = requests.get(jam_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___jam__")
        for price in prices:
            print(price.strip())

    def cheese():

        cheese_url = url + "Lebensmittel/Fruehstueck-Snacks/Kaese-cremes/"
        response = requests.get(cheese_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___cheese__")
        for price in prices:
            print(price.strip())

    def spread():

        spread_url = url + "Lebensmittel/Fruehstueck-Snacks/Streichcreme-Aufstrich/"
        response = requests.get(spread_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___spread__")
        for price in prices:
            print(price.strip())

    def sausage():

        sausage_url = url + "Lebensmittel/Fruehstueck-Snacks/Wurst-Schinken/"
        response = requests.get(sausage_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___sausage__")
        for price in prices:
            print(price.strip())

    def continental():

        con_url = url + "Lebensmittel/Wuerzmittel-Bruehen/"
        response = requests.get(con_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___continental__")
        for price in prices:
            print(price.strip())

    def oil():

        oil_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Oele/"
        response = requests.get(oil_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___oil__")
        for price in prices:
            print(price.strip())

    def broths():

        broths_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Bruehen/"
        response = requests.get(broths_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___broths__")
        for price in prices:
            print(price.strip())

    def vinegar():

        vin_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Essig/"
        response = requests.get(vin_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___vinegar__")
        for price in prices:
            print(price.strip())

    def seasoning():

        sea_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Feinwuerzmittel/"
        response = requests.get(sea_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___seasoning__")
        for price in prices:
            print(price.strip())

    def spice():

        spice_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Gewuerze-Kraeuter/"
        response = requests.get(spice_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___spice__")
        for price in prices:
            print(price.strip())

    def salad():

        salad_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Salatkraeuter/"
        response = requests.get(salad_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___salad_")
        for price in prices:
            print(price.strip())

    def salt():

        salt_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Salz/"
        response = requests.get(salt_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___salt_")
        for price in prices:
            print(price.strip())

    def soup():

        soup_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Suppeneinlagen/"
        response = requests.get(soup_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___soup____")
        for price in prices:
            print(price.strip())

    def mix():

        mix_url = url + "Lebensmittel/Wuerzmittel-Bruehen/Wuerzmischungen/"
        response = requests.get(mix_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___seasoning mix___")
        for price in prices:
            print(price.strip())

    def sauce():

        sauce_url = url + "Lebensmittel/Sossen/"
        response = requests.get(sauce_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___sauce__")
        for price in prices:
            print(price.strip())

    def fxpro():

        fix_url = url + "Lebensmittel/Sossen/Fix-Produkte/"
        response = requests.get(fix_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___fix products__")
        for price in prices:
            print(price.strip())

    def readys():

        ready_url = url + "Lebensmittel/Sossen/Fertige-Sossen/"
        response = requests.get(ready_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___Readymade sauce_")
        for price in prices:
            print(price.strip())

    def fundsauce():
        fund_url = url + "Lebensmittel/Sossen/Fonds-Sossenbinder/"
        response = requests.get(fund_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__fund sauce_")
        for price in prices:
            print(price.strip())

    def barbeque():
        brbq_url = url + "Lebensmittel/Sossen/Grillsaucen/"
        response = requests.get(brbq_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__barbeque_")
        for price in prices:
            print(price.strip())

    def ketchup():
        ket_url = url + "Lebensmittel/Sossen/Ketchup-Mayonnaise/"
        response = requests.get(ket_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__ketchup_")
        for price in prices:
            print(price.strip())

    def saladsp():
        salsp_url = url + "Lebensmittel/Sossen/Salatdressing/"
        response = requests.get(salsp_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_salad spreading")
        for price in prices:
            print(price.strip())

    def mustard():
        mustard_url = url + "Lebensmittel/Sossen/Senf-Meerrettich/"
        response = requests.get(mustard_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("____mustard______")
        for price in prices:
            print(price.strip())

    def stirfry():
        stir_url = url + "Lebensmittel/Sossen/Sossen-zum-Anruehren/"
        response = requests.get(stir_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("____ stirfry_____")
        for price in prices:
            print(price.strip())

    def tomato():
        tom_url = url + "Lebensmittel/Sossen/Tomatensosse-Pesto/"
        response = requests.get(tom_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___tomato_____")
        for price in prices:
            print(price.strip())

    def relish():
        rel_url = url + "Lebensmittel/Sossen/Wuerzsaucen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___relishes_____")
        for price in prices:
            print(price.strip())

    def sidedish():
        rel_url = url + "Lebensmittel/Beilagen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___sidedishes_____")
        for price in prices:
            print(price.strip())

    def rice():
        rel_url = url + "Lebensmittel/Beilagen/Reis/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___rice_____")
        for price in prices:
            print(price.strip())

    def pasta():
        rel_url = url + "Lebensmittel/Beilagen/Nudeln/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___pasta___")
        for price in prices:
            print(price.strip())

    def seed():
        rel_url = url + "Lebensmittel/Beilagen/Samen-Saaten/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("______seed_____")
        for price in prices:
            print(price.strip())

    def patties():
        rel_url = url + "Lebensmittel/Beilagen/Bratlinge/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_____patties____")
        for price in prices:
            print(price.strip())

    def legumes():
        rel_url = url + "Lebensmittel/Beilagen/Huelsenfruechte/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("____legumes____")
        for price in prices:
            print(price.strip())

    def dmppot():
        rel_url = url + "Lebensmittel/Beilagen/Knoedel-Kartoffelprodukte/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("____dumpling potato___")
        for price in prices:
            print(price.strip())

    def canned():
        rel_url = url + "Lebensmittel/Konserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___canned goods__")
        for price in prices:
            print(price.strip())

    def cannedfish():
        rel_url = url + "Lebensmittel/Konserven/Fischkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___canned fish__")
        for price in prices:
            print(price.strip())

    def cannedmeat():
        rel_url = url + "Lebensmittel/Konserven/Fischkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___canned meat__")
        for price in prices:
            print(price.strip())

    def cannedveg():
        rel_url = url + "Lebensmittel/Konserven/Gemuesekonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__canned veg_")
        for price in prices:
            print(price.strip())

    def fruit():
        rel_url = url + "Lebensmittel/Konserven/Obstkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__fruit_")
        for price in prices:
            print(price.strip())

    def olive():
        rel_url = url + "Lebensmittel/Konserven/Oliven-Peperoni/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_olive__")
        for price in prices:
            print(price.strip())

    def sausagejar():
        rel_url = url + "Lebensmittel/Konserven/Wuerstchen-im-Glas/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_sausagejar_")
        for price in prices:
            print(price.strip())

    def cansas():
        rel_url = url + "Lebensmittel/Konserven/Wurstkonserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("canned sausage")
        for price in prices:
            print(price.strip())

    def sweet():
        rel_url = url + "Lebensmittel/Suess-Salzig/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("______sweet salt__")
        for price in prices:
            print(price.strip())

    def chocolate():
        rel_url = url + "Lebensmittel/Suess-Salzig/Schokoriegel/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("______chocolate__")
        for price in prices:
            print(price.strip())

    def candy():
        rel_url = url + "Lebensmittel/Suess-Salzig/Bonbons-Kaugummi/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("______candy__")
        for price in prices:
            print(price.strip())

    def fruitgum():
        rel_url = url + "Lebensmittel/Suess-Salzig/Fruchtgummi-Lakritz/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("___fruitgum__")
        for price in prices:
            print(price.strip())

    def chotreat():
        rel_url = url + "Lebensmittel/Suess-Salzig/Schoko-Leckereien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__chocolate treat_")
        for price in prices:
            print(price.strip())

    def barcho():
        rel_url = url + "Lebensmittel/Suess-Salzig/Tafelschokolade/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__chocolate bar_")
        for price in prices:
            print(price.strip())

    def chips():
        rel_url = url + "Lebensmittel/Suess-Salzig/Chips-Knabbereien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__chips_")
        for price in prices:
            print(price.strip())

    def pastry():
        rel_url = url + "Lebensmittel/Suess-Salzig/Gebaeck-Kekse-Waffeln/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__pastry___")
        for price in prices:
            print(price.strip())

    def nutsdry():
        rel_url = url + "Lebensmittel/Suess-Salzig/Nuesse-getrocknete-Fruechte/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__nutsdry___")
        for price in prices:
            print(price.strip())

    def easter():
        rel_url = url + "Lebensmittel/Suess-Salzig/Oster-Leckereien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__easter___")
        for price in prices:
            print(price.strip())

    def readymeals():
        rel_url = url + "Lebensmittel/Fertiggerichte"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__readymeals___")
        for price in prices:
            print(price.strip())

    def dishstir():
        rel_url = url + "Lebensmittel/Fertiggerichte/Gerichte-zum-Anruehren/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__dishtir___")
        for price in prices:
            print(price.strip())

    def dishheat():
        rel_url = url + "Lebensmittel/Fertiggerichte/Gerichte-zum-Erhitzen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__dishheat___")
        for price in prices:
            print(price.strip())

    def soupmix():
        rel_url = url + "Lebensmittel/Fertiggerichte/Suppen-zum-Anruehren/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__soupmix___")
        for price in prices:
            print(price.strip())

    def soupstew():
        rel_url = url + "Lebensmittel/Fertiggerichte/Suppen-Eintoepfe/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__soupstew___")
        for price in prices:
            print(price.strip())

    def drinkmeal():
        rel_url = url + "Lebensmittel/Fertiggerichte/Trinkmahlzeiten/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_drinkmeal___")
        for price in prices:
            print(price.strip())

    def international():
        rel_url = url + "Lebensmittel/Internationales/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__international__")
        for price in prices:
            print(price.strip())

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
        print("_organic brands___")
        for price in prices:
            print(price.strip())

    def unpackpro():
        rel_url = url + "Bio-Produkte/Bio-Marken/Unverpackt/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__unpack__")
        for price in prices:
            print(price.strip())

    def edkabio():
        rel_url = url + "Bio-Produkte/Bio-Marken/EDEKA-Bio/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_edkabio__")
        for price in prices:
            print(price.strip())

    def bauckhof():
        rel_url = url + "Bio-Produkte/Bio-Marken/Bauckhof/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__Bauckhof__")
        for price in prices:
            print(price.strip())

    def beshorg():
        rel_url = url + "Bio-Produkte/Bio-Marken/BESH-Bio-Konserven/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_beshorganic__")
        for price in prices:
            print(price.strip())

    def gepa():
        rel_url = url + "Bio-Produkte/Bio-Marken/Gepa/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__gepa__")
        for price in prices:
            print(price.strip())

    def recgood():
        rel_url = url + "Bio-Produkte/Bio-Marken/Rettergut/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_rescuegoods__")
        for price in prices:
            print(price.strip())

    def veganz():
        rel_url = url + "Bio-Produkte/Bio-Marken/Veganz/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("__veganz_")
        for price in prices:
            print(price.strip())

    def orggrounments():
        rel_url = url + "Bio-Produkte/Bio-Marken/Bio-Gourmet/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("organic grounments")
        for price in prices:
            print(price.strip())

    def hipbio():
        rel_url = url + "Bio-Produkte/Bio-Marken/Hipp-Bio/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_hipbio_")
        for price in prices:
            print(price.strip())

    def littlunch():
        rel_url = url + "Bio-Produkte/Bio-Marken/Little-Lunch/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("little lunch")
        for price in prices:
            print(price.strip())

    def more():
        rel_url = url + "Bio-Produkte/Bio-Marken/mehr/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_more_")
        for price in prices:
            print(price.strip())

    def alnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_food from alnatura_")
        for price in prices:
            print(price.strip())

    def bakingalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Backzutaten-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("baking ingredeints from alnatura")
        for price in prices:
            print(price.strip())

    def readymeals():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Fertiggerichte-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_readymeals_")
        for price in prices:
            print(price.strip())

    def pastalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Gebaeck-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_pastries from alnatura_")
        for price in prices:
            print(price.strip())

    def ketchupalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Ketchup-Gewuerzsaucen-von-Alnatura"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("ketchupfrom alnatura")
        for price in prices:
            print(price.strip())

    def alnaturapreserve():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Konserven-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura prserve_")
        for price in prices:
            print(price.strip())

    def muselialnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Muesliriegel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("museli from alnatura")
        for price in prices:
            print(price.strip())

    def alnaturapasta():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Nudeln-Sossen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura pasta_")
        for price in prices:
            print(price.strip())

    def ricealnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Reis-Beilagen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("riece from alnatura")
        for price in prices:
            print(price.strip())

    def alnaturasweet():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Suesses-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura sweet_")
        for price in prices:
            print(price.strip())

    def sugaralnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Zucker-Suessstoff-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("sugar from alnatura")
        for price in prices:
            print(price.strip())

    def alnaturababy():
        rel_url = url + "Alnatura-Produkte-Babynahrung/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura baby_")
        for price in prices:
            print(price.strip())

    def alnaturabroths():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Gewuerze-Bruehen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura broths_")
        for price in prices:
            print(price.strip())

    def nutalnatura():
        rel_url = url + "Bio-Produkte/Lebensmittel-von-Alnatura/Nuesse-Fruechte-Samen-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("nut from alnatura")
        for price in prices:
            print(price.strip())

    def alnaturaoil():
        rel_url = url + "/Bio-Produkte/Lebensmittel-von-Alnatura/Pflanzenoel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura oil_")
        for price in prices:
            print(price.strip())

    def alnaturabrkfst():
        rel_url = url + "Bio-Produkte/Fruehstuecksartikel-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura breakfast_")
        for price in prices:
            print(price.strip())

    def breadalnatura():
        rel_url = url + "Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Brot-Knaecke-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("bread from alnatura")
        for price in prices:
            print(price.strip())

    def alnaturaspread():
        rel_url = url + "/Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Brotaufstriche-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura spread_")
        for price in prices:
            print(price.strip())

    def fuitspreadalnatura():
        rel_url = url + "Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Fruchtaufstriche-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("fruit spread from alnatura")
        for price in prices:
            print(price.strip())

    def muscereal():
        rel_url = url + "/Bio-Produkte/Fruehstuecksartikel-von-Alnatura/Muesli-Cerealien-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_museli creal_")
        for price in prices:
            print(price.strip())

    def alnatdrinks():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura drinks_")
        for price in prices:
            print(price.strip())
   
    def alnaturacoffee():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Kaffee-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura coffee_")
        for price in prices:
            print(price.strip())
    def alnaturajuice():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Saefte-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura juice_")
        for price in prices:
            print(price.strip())   
    def alnaturatea():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Tee-von-Alnatura/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura tea_")
        for price in prices:
            print(price.strip())  
    def alnaturawine():
        rel_url = url + "Bio-Produkte/Getraenke-von-Alnatura/Weine-von-Alnatura"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_alnatura wine_")
        for price in prices:
            print(price.strip()) 
    def redwine():
        rel_url = url + "Wein-Spirituosen/Rotwein/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_redwine")
        for price in prices:
            print(price.strip())   
    def germany():
        rel_url = url + "Wein-Spirituosen/Rotwein/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_germany_")
        for price in prices:
            print(price.strip())  
    def italy():
        rel_url = url + "Wein-Spirituosen/Rotwein/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_italy_")
        for price in prices:
            print(price.strip()) 
    def france():
        rel_url = url + "Wein-Spirituosen//Rotwein/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("france")
        for price in prices:
            print(price.strip())   
    def spain():
        rel_url = url + "Wein-Spirituosen/Rotwein/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("spain")
        for price in prices:
            print(price.strip())  
    def austria():
        rel_url = url + "Wein-Spirituosen/Rotwein/Oesterreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("austria")
        for price in prices:
            print(price.strip()) 
    def overseas():
        rel_url = url + "Wein-Spirituosen//Rotwein/Uebersee/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("overseas")
        for price in prices:
            print(price.strip())   
    def organic():
        rel_url = url + "Wein-Spirituosen/Rotwein/Bio//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("organic")
        for price in prices:
            print(price.strip())  
    def portugal():
        rel_url = url + "Wein-Spirituosen/Rotwein/Portugal/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("portugal")
        for price in prices:
            print(price.strip()) 
    def whitevine():
        rel_url = url + "Wein-Spirituosen/Weisswein/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("whitevine")
        for price in prices:
            print(price.strip()) 
    def germanyw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_germany_")
        for price in prices:
            print(price.strip())  
    def italyw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_italy_")
        for price in prices:
            print(price.strip()) 
    def francew():
        rel_url = url + "Wein-Spirituosen//Weisswein/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("france")
        for price in prices:
            print(price.strip())   
    def spainw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("spain")
        for price in prices:
            print(price.strip())  
    def austriaw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Oesterreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("austria")
        for price in prices:
            print(price.strip()) 
    def overseasw():
        rel_url = url + "Wein-Spirituosen//Weisswein/Uebersee/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("overseas")
        for price in prices:
            print(price.strip())   
    def organicw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Bio//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("organic")
        for price in prices:
            print(price.strip())  
    def portugalw():
        rel_url = url + "Wein-Spirituosen/Weisswein/Portugal/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("portugal")
        for price in prices:
            print(price.strip())   
    def rosewine():
        rel_url = url + "Wein-Spirituosen/Ros-weine/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("roseine")
        for price in prices:
            print(price.strip()) 
    def germanyr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_germany_")
        for price in prices:
            print(price.strip())  
    def italyr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_italy_")
        for price in prices:
            print(price.strip()) 
    def francer():
        rel_url = url + "Wein-Spirituosen//Ros-weine/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("france")
        for price in prices:
            print(price.strip())   
    def spainr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("spain")
        for price in prices:
            print(price.strip())  
    def austriar():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Oesterreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("austria")
        for price in prices:
            print(price.strip()) 
    def overseasr():
        rel_url = url + "Wein-Spirituosen//Ros-weine/Uebersee/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("overseas")
        for price in prices:
            print(price.strip())   
    def organicr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Bio//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("organic")
        for price in prices:
            print(price.strip())  
    def portugalr():
        rel_url = url + "Wein-Spirituosen/Ros-weine/Portugal/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("portugal")
        for price in prices:
            print(price.strip())   
    def sparkling():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("sparkling")
        for price in prices:
            print(price.strip())  
    def nonalcoholic():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/ALKOHOLFREI/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("nonalcoholic")
        for price in prices:
            print(price.strip())  
    def germanysp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Deutschland/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_germany_")
        for price in prices:
            print(price.strip())  
    def italysp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Italien/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("_italy_")
        for price in prices:
            print(price.strip()) 
    def francesp():
        rel_url = url + "Wein-Spirituosen//Sekt-Prosecco/Frankreich/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("france")
        for price in prices:
            print(price.strip())   
    def spainsp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Spanien//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("spain")
        for price in prices:
            print(price.strip())
    def organisp():
        rel_url = url + "Wein-Spirituosen/Sekt-Prosecco/Bio/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("organic")
        for price in prices:
            print(price.strip())                
    def spirit():
        rel_url = url + "Wein-Spirituosen/Spirituosen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("spirit")
        for price in prices:
            print(price.strip())  
    def fires():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Braende/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("fires")
        for price in prices:
            print(price.strip())                
    def brandy():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Brandy-Weinbrand/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("spirit")
        for price in prices:
            print(price.strip()) 
    def cognac():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Cognac/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("cognac")
        for price in prices:
            print(price.strip())                
    def gin():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Gin/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("gin")
        for price in prices:
            print(price.strip()) 
    def grappa():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Grappa/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("grappa")
        for price in prices:
            print(price.strip())                
    def liquire():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Likoere-Bitter//"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("liquire")
        for price in prices:
            print(price.strip()) 
    def mead():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Met/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("mead")
        for price in prices:
            print(price.strip()) 
    def canmix():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Mixgetraenke-in-Dosen/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("canmix")
        for price in prices:
            print(price.strip())                
    def party():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Party-Schnaps/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("party")
        for price in prices:
            print(price.strip()) 
    def port():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Portwein-Sherry-Likoerwein/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("port")
        for price in prices:
            print(price.strip()) 
    def rum():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Rum/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("rum")
        for price in prices:
            print(price.strip())                
    def tequila():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Tequila/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("tequila")
        for price in prices:
            print(price.strip()) 
    def vodka():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Vodka/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("vodka")
        for price in prices:
            print(price.strip()) 
    def vermouth():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Wermut/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("vermouth")
        for price in prices:
            print(price.strip())                
    def whisky():
        rel_url = url + "Wein-Spirituosen/Spirituosen/Whisky/"
        response = requests.get(rel_url, headers=headers)
        selector = Selector(response.text)
        prices = selector.xpath('//div[@class="price"]/text()').extract()
        print("whisky")
        for price in prices:
            print(price.strip()) 







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
# mainlist()
grocery()
organic_products()
