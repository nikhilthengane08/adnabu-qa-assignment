from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def add_to_cart(self):

        # Wait for page load
        time.sleep(5)

        # Try multiple Shopify button locators
        locators = [
            (By.NAME, "add"),
            (By.XPATH, "//button[@name='add']"),
            (By.XPATH, "//button[contains(.,'Add to cart')]"),
            (By.XPATH, "//input[@value='Add to cart']"),
            (By.CSS_SELECTOR, "button.product-form__submit"),
        ]

        add_button = None

        for locator in locators:
            try:
                add_button = self.wait.until(
                    EC.presence_of_element_located(locator)
                )

                if add_button.is_displayed():
                    break

            except:
                continue

        if not add_button:
            raise Exception("Add to cart button not found")

        # Scroll to button
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_button
        )

        time.sleep(2)

        # Click using JavaScript
        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        time.sleep(5)