from selenium.common.exceptions import NoSuchElementException
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_basket(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div/form/div[2]/div[1]/main/div/div[3]/div[3]/form/div[2]/button").click()

    def basket_item_validation(self):
        try:
            self.driver.find_element_by_css_selector("[span='UxJ2P']")
        except NoSuchElementException:
            return False
        return True


