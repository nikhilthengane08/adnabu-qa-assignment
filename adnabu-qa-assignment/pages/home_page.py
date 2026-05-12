from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)

    def enter_store_password(self, password):

        password_box = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "password")
            )
        )

        password_box.clear()
        password_box.send_keys(password)

        enter_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Enter')]")
            )
        )

        enter_button.click()