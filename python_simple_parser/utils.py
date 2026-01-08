from playwright.sync_api import Page

def getProducts(page: Page, iterations: int = 0):
    # Function is scrolling page down and waiting cards for download
    # to get more cards

    # Arguments
    # page: playwright.sync_api.Page - your page object
    # iterations: int - amount of iterations. The more iterations the more cards
    # you will get

    for i in range(iterations):
        page.mouse.wheel(0, 2200)
        page.wait_for_timeout(5000)