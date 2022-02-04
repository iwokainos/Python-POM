from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ResultsPage():

    def __init__(self, driver):
        self.driver = driver
        self.results_css_selector = "[alt='Czapka z daszkiem - Plan średni']"

    def hit_item(self):
        # wait = WebDriverWait(self.driver, 10)
        # result = wait.until(EC.element_to_be_clickable(self.driver.find_element_by_css_selector("[alt='Czapka z daszkiem - Plan średni']")))
        # result.click()
        result = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.results_css_selector)))
        result.click()

