import requests
import json
from parsel import Selector

headers={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	            "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	            "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
	            
	              }
url="https://www.edeka24.de/"

def mainlist():
	

	response = requests.get(url,headers=headers)
	print(response.status_code)


	selector= Selector(response.text)
	prices= selector.xpath(' //div[@class="price salesprice"]//text()').extract()

	for price in prices:
	    print(price.strip()) 
	pricenote=selector.xpath(' //p[@class="price-note"]//text()').extract()

	for price in pricenote:
	    print(price.strip()) 


	titles =selector.xpath('//div[@class="product-details"]/a[@class="title"]/h2/text()').extract()
	for title in titles:
		print(title.strip())

	img =selector.xpath('//div[@class="product-image"]/a/img/@src').extract()
	for image in img:
		print(image.strip())


def grocery():
	def coffeetea():
	    
	    cof_url = url+"Lebensmittel/Kaffee-Tee/"

	    response = requests.get(cof_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("_________grocery_____")
	    for price in prices:
	        print(price.strip())

	def coffeewholebeans():

	    cofb_url = url+"Lebensmittel/Kaffee-Tee/Kaffee-ganze-Bohnen/"

	    response = requests.get(cofb_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
    	# print("_________coffee wholebean____")
	   	for price in prices:
	        print(price.strip())

	def grndcofinstant():

	    grndinst_url = url+"Lebensmittel/Kaffee-Tee/Kaffee-gemahlen-Instant/"


	    response = requests.get(grndinst_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("_________ground coffee_____")
	    for price in prices:
	        print(price.strip())

	def coffeepods():

	    cofpods_url = url+"Lebensmittel/Kaffee-Tee/Kaffeepads/"


	    response = requests.get(cofpods_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("____coffeepods______")
	    for price in prices:
	        print(price.strip())

	def coffeecapsules():

	    cofcaps_url = url+"Lebensmittel/Kaffee-Tee/Kaffeekapseln/"


	    response = requests.get(cofcaps_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___Coffee capsule_______")
	    for price in prices:
	        print(price.strip())
	       

	def cappuccino():

	    cofcaps_url = url+"Lebensmittel/Kaffee-Tee/Cappuccino-Kakao/"


	    response = requests.get(cofcaps_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("__Cappuccino___")
	    for price in prices:
	        print(price.strip())

	def cfilter():

	    filt_url = url+"Lebensmittel/Kaffee-Tee/Filter/"


	    response = requests.get(filt_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___Filter___")
	    for price in prices:
	        print(price.strip())

	def milkcraalter():

	    milk_url = url+"Lebensmittel/Kaffee-Tee/Milch-Sahne-Alternativen/"


	    response = requests.get(milk_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("__Milk cream___")
	    for price in prices:
	        print(price.strip())

	def tee():


	    tee_url = url+"Lebensmittel/Kaffee-Tee/tee/"


	    response = requests.get(tee_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___Tea__")
	    for price in prices:
	        print(price.strip())

	def beverages():

	    bev_url = url+"Lebensmittel/Getraenke/"


	    response = requests.get(bev_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("__Beverages__")
	    for price in prices:
	        print(price.strip())

	def energydrinks():

	    eng_url = url+"Lebensmittel/Getraenke/Energydrinks/"


	    response = requests.get(eng_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___Energy Drinks___")
	    for price in prices:
	        print(price.strip())

	def juices():

	    juice_url = url+"Lebensmittel/Getraenke/Saefte/"


	    response = requests.get(juice_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___Juices___")
	    for price in prices:
	        print(price.strip())
	def beer():

	    beer_url = url+"Wein-Spirituosen/Bier/"


	    response = requests.get(beer_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___beer____")
	    for price in prices:
	        print(price.strip())
	def cola():

	    cola_url = url+"Lebensmittel/Getraenke/Cola/"


	    response = requests.get(cola_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("__Cola__")
	    for price in prices:
	        print(price.strip())
	def icetea():

	    icetea_url = url+"Lebensmittel/Getraenke/Eistee/"


	    response = requests.get(icetea_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("__Icetea__")
	    for price in prices:
	        print(price.strip())


	def instdrinks():

	    inst_url = url+"Lebensmittel/Getraenke/Instant-Getraenke/"


	    response = requests.get(inst_url, headers=headers)
	    selector = Selector(response.text)
	    prices = selector.xpath('//div[@class="price"]/text()').extract()
	    print("___Instant drinks__")
	    for price in prices:
	        print(price.strip())


	def lemonade():

		    lemon_url = url+"Lebensmittel/Getraenke/Limonade/"


		    response = requests.get(lemon_url, headers=headers)
		    selector = Selector(response.text)
		    prices = selector.xpath('//div[@class="price"]/text()').extract()
		    print("___Lemonade__")
		    for price in prices:
		        print(price.strip())


	def syrup():

		    syrup_url = url+"Lebensmittel/Getraenke/Sirup/"


		    response = requests.get(syrup_url, headers=headers)
		    selector = Selector(response.text)
		    prices = selector.xpath('//div[@class="price"]/text()').extract()
		    print("___syrup__")
		    for price in prices:
		        print(price.strip())

	def water():

		    water_url = url+"Lebensmittel/Getraenke/Wasser/"


		    response = requests.get(water_url, headers=headers)
		    selector = Selector(response.text)
		    prices = selector.xpath('//div[@class="price"]/text()').extract()
		    print("___Water___")
		    for price in prices:
		        print(price.strip())
	def backingdessert():

		    backing_url = url+"/Lebensmittel/Backen-Desserts/"


		    response = requests.get(backing_url, headers=headers)
		    selector = Selector(response.text)
		    prices = selector.xpath('//div[@class="price"]/text()').extract()
		    print("__baking dessrt__")
		    for price in prices:
		        print(price.strip())
	def margarine():

			marg_url = url+"Lebensmittel/Backen-Desserts/Margarine-Butterschmalz/"


			response = requests.get(marg_url, headers=headers)
			selector = Selector(response.text)
			prices = selector.xpath('//div[@class="price"]/text()').extract()
			print("__Margarine___")
			for price in prices:
			    print(price.strip())
	def flavor():

			flavor_url = url+"Lebensmittel/Backen-Desserts/Aromen-Vanille/"


			response = requests.get(flavor_url, headers=headers)
			selector = Selector(response.text)
			prices = selector.xpath('//div[@class="price"]/text()').extract()
			print("___Flavors__")
			for price in prices:
				print(price.strip())
	def baking():

			baking_url = url+"Lebensmittel/Backen-Desserts/Backmischungen/"

			response = requests.get(baking_url, headers=headers)
			selector = Selector(response.text)
			prices = selector.xpath('//div[@class="price"]/text()').extract()
			print("___Baking___")
			for price in prices:
				print(price.strip())

	def bakingdecor():

				bakingd_url = url+"Lebensmittel/Backen-Desserts/Backzutaten-Dekor/"

				response = requests.get(bakingd_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___Baking decor___")
				for price in prices:
					print(price.strip())
	def gelingagent():

				gel_url = url+"Lebensmittel/Backen-Desserts/Geliermittel-Sahnefest/"

				response = requests.get(gel_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___gelling__")
				for price in prices:
					print(price.strip())


	def couvertur():

				cov_url = url+"Lebensmittel/Backen-Desserts/Kuvertuere-Glasur/"

				response = requests.get(cov_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___couverture glaze __")
				for price in prices:
					print(price.strip())
	def flour():

				flr_url = url+"Lebensmittel/Backen-Desserts/Mehl-Backpulver-Hefe/"

				response = requests.get(flr_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___flour __")
				for price in prices:
					print(price.strip())				
	def nuts():

				nuts_url = url+"Lebensmittel/Backen-Desserts/Nuesse-mehr/"

				response = requests.get(nuts_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___nuts __")
				for price in prices:
					print(price.strip())				

	def pudding():

				pud_url = url+"Lebensmittel/Backen-Desserts/Pudding-Dessert/"

				response = requests.get(pud_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___pudding__")
				for price in prices:
					print(price.strip())
	def sugar():

				sug_url = url+"Lebensmittel/Backen-Desserts/Zucker-Zuckerersatz/"

				response = requests.get(sug_url, headers=headers)
				selector = Selector(response.text)
				prices = selector.xpath('//div[@class="price"]/text()').extract()
				print("___sugar__")
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

mainlist()
grocery()
