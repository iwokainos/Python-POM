import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-position=2000,0")
        self.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe", chrome_options=self.chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")