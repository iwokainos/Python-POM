from selenium.webdriver.common.keys import Keys

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
        self.search_button_id ="searchIconButton"
        self.search_bar_class_name = "LqcsN"

    def accept_cookies(self):
        self.driver.find_element_by_id(self.cookies_button_id).click()

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def type_username(self):
        self.driver.find_element_by_id(self.login_field_id).send_keys(username)

    def type_password(self):
        self.driver.find_element_by_id(self.password_field_id).send_keys(password + Keys.RETURN)

    def click_search_button(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def search_type_in(self):
        self.driver.find_element_by_class_name(self.search_bar_class_name).send_keys(search_term + Keys.RETURN)

    def logout_header(self):
        span_elem2 = self.driver.find_element_by_xpath("/html/body/header/micro-frontend/div/div[2]/div[2]/div[2]/span[2]")
        new2 = span_elem2.text
        return new2


