from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

username = "spisanenastraty@gmail.com"
password = "omikron66"
search_term = "czapka"

class LandingPage():
# constructor
    def __init__(self, driver):
        self.driver = driver
        self.cookies_button_id = "onetrust-accept-btn-handler"
        self.login_button_id = "login_any"
        self.login_field_id = "SVLoginCheck:FRegLogChk:userMail"
        self.password_field_id = "SVLoginCheck:FRegLogChk:chkPwd"
        self.search_button_id = "searchIconButton"
        self.search_bar_class_name = "LqcsN"
        self.logout_header_xpath = "/html/body/header/micro-frontend/div/div[2]/div[2]/div[2]/span[2]"

    def accept_cookies(self):
        cookies_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.cookies_button_id)))
        cookies_button.click()

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.login_button_id)))
        login_button.click()

    def type_username(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.login_field_id)))
        username_field.clear()
        username_field.send_keys(username)

    def type_password(self):
        password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.password_field_id)))
        password_field.clear()
        password_field.send_keys(password + Keys.RETURN)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.search_button_id)))
        search_button.click()

    def search_type_in(self):
        search_bar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.search_bar_class_name)))
        search_bar.clear()
        search_bar.send_keys(search_term + Keys.RETURN)

    def logout_header(self):
        logout_header = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.logout_header_xpath)))
        # span_elem2 = self.driver.find_element_by_xpath("/html/body/header/micro-frontend/div/div[2]/div[2]/div[2]/span[2]")
        new2 = logout_header.text
        return new2


