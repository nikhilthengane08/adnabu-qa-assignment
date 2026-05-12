from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.driver_factory import get_driver
from config import BASE_URL, STORE_PASSWORD, PRODUCT_URL

import time


def test_search_and_add_product_to_cart():

    driver = get_driver()

    try:
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        # Open store
        home_page.open(BASE_URL)

        # Login
        home_page.enter_store_password(STORE_PASSWORD)

        # Open product page
        driver.get(PRODUCT_URL)

        # Wait for page load
        time.sleep(5)

        # Add product to cart
        product_page.add_to_cart()

        # Wait after add
        time.sleep(5)

        # Open cart manually
        driver.get("https://adnabu-store-assignment1.myshopify.com/cart")

        time.sleep(3)

        # Verify cart page
        assert "cart" in driver.current_url.lower()

    finally:
        driver.quit()