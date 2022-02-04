from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.account_button_id = "login"
        self.driver.logout_subitem_xpath = "//*[@id='login']/div/div[2]/div[4]"
        self.driver.login_header_xpath = "/html/body/header/micro-frontend/div/div[2]/div[2]/div[2]/span[2]"

    def hit_logout_menu(self):
        a = ActionChains(self.driver)
        my_account_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.driver.account_button_id)))
        a.move_to_element(my_account_button).perform()
        logout_subitem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.driver.logout_subitem_xpath)))
        a.move_to_element(logout_subitem).click().perform()

    def login_header(self):
        login_header = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.driver.login_header_xpath)))
        new = login_header.text
        return new
