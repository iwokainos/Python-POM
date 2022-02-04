from Pages.LandingPage import LandingPage
from Pages.BasePage import BasePage

class SearchTests(BasePage):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")


    def test_search_valid(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        search = LandingPage(driver)
        search.accept_cookies()
        search.click_search_button()
        search.search_type_in()
        assert 'czapka' in driver.title

    def tearDown(self):
        super().setUp()
        print("RUNNING AFTER EACH TEST")