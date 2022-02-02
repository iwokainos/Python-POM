from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        # self.logout_menu_id = "login_any"
        # self.logout_sub_menu_class_name = "KI27k logout"

    # def verify_logged(self):
    #     return self.driver.find_element_by_xpath(".//span[@class = 'Moje konto']").get

    def hit_logout_menu(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_id("login")
        a.move_to_element(m).perform()
        n = self.driver.find_element_by_xpath("//*[@id='login']/div/div[2]/div[4]")
        a.move_to_element(n).click().perform()

    def login_header(self):
        span_element = self.driver.find_element_by_xpath("/html/body/header/micro-frontend/div/div[2]/div[2]/div[2]/span[2]")
        new = span_element.text
        return new
