import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest
from Pages.LandingPage import LandingPage
from Pages.HomePage import HomePage

# noinspection PyDeprecation
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--window-position=2000,0")
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe", chrome_options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        PHRASE1 = 'Moje konto'
        # creating Login page object, passing driver instance
        login = LandingPage(driver)
        login.accept_cookies()
        login.click_login_button()
        login.type_username()
        login.type_password()
        home = HomePage(driver)
        assert PHRASE1 == home.login_header()

    def test_logout_valid(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        PHRASE2 = 'Zaloguj się'
        # creating Login page object, passing driver instance
        login = LandingPage(driver)
        login.accept_cookies()
        login.click_login_button()
        login.type_username()
        login.type_password()
        home = HomePage(driver)
        time.sleep(5)
        home.hit_logout_menu()
        logout = LandingPage(driver)
        assert PHRASE2 == logout.logout_header()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

# python -m unittest login.py