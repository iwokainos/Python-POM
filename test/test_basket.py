from Pages.LandingPage import LandingPage
from Pages.ResultsPage import ResultsPage
from Pages.ProductPage import ProductPage
from Pages.BasePage import BasePage

class BasketTest(BasePage):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

    def test_basket_validation(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        basket = LandingPage(driver)
        basket.accept_cookies()
        basket.click_search_button()
        basket.search_type_in()
        basket = ResultsPage(driver)
        basket.hit_item()
        basket = ProductPage(driver)
        basket.add_to_basket()
        basket.basket_item_validation()
        assert True

    def tearDown(self):
        super().setUp()
        print("RUNNING AFTER EACH TEST")
