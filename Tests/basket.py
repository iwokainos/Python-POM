import time
import unittest
from selenium import webdriver
from Pages.LandingPage import LandingPage
from Pages.ResultsPage import ResultsPage
from Pages.ProductPage import ProductPage
from selenium.webdriver.chrome.options import Options

class BasketTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--window-position=2000,0")
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe", chrome_options=cls.chrome_options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_basket_validation(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        basket = LandingPage(driver)
        basket.accept_cookies()
        basket.click_search_button()
        basket.search_type_in()
        time.sleep(3)
        basket = ResultsPage(driver)
        basket.hit_item()
        time.sleep(5)
        basket = ProductPage(driver)
        basket.add_to_basket()
        time.sleep(5)
        basket.basket_item_validation()
        assert True

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
