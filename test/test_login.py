from Pages.LandingPage import LandingPage
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage

# noinspection PyDeprecation
class LoginTest(BasePage):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        ACCOUNT_CAPTION = 'Moje konto'
        # creating Login page object, passing driver instance
        login = LandingPage(driver)
        login.accept_cookies()
        login.click_login_button()
        login.type_username()
        login.type_password()
        home = HomePage(driver)
        assert ACCOUNT_CAPTION == home.login_header()

    def test_logout_valid(self):
        driver = self.driver
        driver.get("https://shop.mango.com/pl")
        LOGIN_CAPTION = 'Zaloguj się'
        # creating Login page object, passing driver instance
        login = LandingPage(driver)
        login.accept_cookies()
        login.click_login_button()
        login.type_username()
        login.type_password()
        home = HomePage(driver)
        home.hit_logout_menu()
        logout = LandingPage(driver)
        assert LOGIN_CAPTION == logout.logout_header()

    def tearDown(self):
        super().setUp()
        print("RUNNING AFTER EACH TEST")

# python -m unittest login.py