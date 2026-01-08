from playwright.sync_api import sync_playwright
from utils import getProducts

OZON_URL = "https://www.ozon.ru"
PROFILE_DIR = "ozon_profile"

with sync_playwright() as p:
    browser = p.chromium

    context = browser.launch( # Settings to imitate human
        args=[
            "--disable-blink-features=AutomationControlled",
        ],
        headless=False,
    )

    page = context.new_page()

    page.goto(OZON_URL)
    page.wait_for_timeout(5000) # Waiting page to load
    getProducts(page, iterations=1)

    cards = page.query_selector_all('.tile-root') # Getting all cards by class name

    print(len(cards))

    for item in cards:
        price = item.query_selector('.c35_3_12-a1')
        name = item.query_selector('.tsBody500Medium')
        link = item.query_selector('.q4b1_3_1-a').get_attribute('href')

        print(f'PRICE: {price.inner_text()}')
        print(f'NAME: {name.inner_text()}')
        print(f'LINK: https://www.ozon.ru{link}\n\n')

    context.close()
