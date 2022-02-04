from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_button_xpath = "/html/body/div[5]/div/form/div[2]/div[1]/main/div/div[3]/div[3]/form/div[2]/button"
        self.item_added_selector = "[span='UxJ2P']"

    def add_to_basket(self):
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_button_xpath)))
        add_button.click()

    def basket_item_validation(self):
        try:
            self.driver.find_element_by_css_selector(self.item_added_selector)
        except NoSuchElementException:
            return False
        return True

