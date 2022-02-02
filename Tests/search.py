import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.LandingPage import LandingPage
from Pages.HomePage import HomePage

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--window-position=2000,0")
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe", chrome_options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_search_valid(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        search = LandingPage(driver)
        search.accept_cookies()
        time.sleep(5)
        search.click_search_button()
        search.search_type_in()
        assert 'sukienka' in driver.title

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test completed")