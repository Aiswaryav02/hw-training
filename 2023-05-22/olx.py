from playwright.sync_api import sync_playwright

url = "https://www.olx.in/item/brand-new-3-bhk-flat-for-sale-at-calicut-city-iid-1729965653"


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    descriptions = page.wait_for_selector('xpath=//div[@data-aut-id="itemDescriptionContent"]',timeout=30000).text_content()
    price = page.wait_for_selector('xpath=//span[@data-aut-id="itemPrice"]',timeout=30000).text_content()
    property_title = page.wait_for_selector('xpath=//h1[@data-aut-id="itemTitle"]',timeout=30000).text_content()
    bathrooms = page.wait_for_selector('xpath=//span[@data-aut-id="value_bathrooms"]',timeout=30000).text_content()
    bedrooms = page.wait_for_selector('xpath=//span[@data-aut-id="value_rooms"]',timeout=30000).text_content()
    property_type = page.wait_for_selector('xpath=//span[@data-aut-id="value_type"]',timeout=30000).text_content()
    breadcrumbs = page.wait_for_selector('xpath=//div[@data-aut-id="breadcrumb"]',timeout=30000).text_content()
    location = page.wait_for_selector('xpath=//div[@data-aut-id="itemLocation"]',timeout=30000).text_content()
    
    print("Descriptions:", descriptions)
    print("Price:", price)
    print("Property Title:", property_title)
    print("Bathrooms:", bathrooms)
    print("Bedrooms:", bedrooms)
    print("Property Type:", property_type)
    print("Breadcrumbs:", breadcrumbs)
    print("Location:", location)

    
    

