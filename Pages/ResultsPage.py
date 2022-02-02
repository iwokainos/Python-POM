from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ResultsPage():

    def __init__(self, driver):
        self.driver = driver
        # self.item_xpath = "/html/body/div[5]/div/form/div[2]/div/div/div[4]/div[1]/div[1]/div/ul/li[2]/a/div[1]/div/div[1]/div[2]/img"

    def hit_item(self):
        # self.driver.find_element_by_xpath("img[contains(@src'https://st.mngbcn.com/rcs/pics/static/T1/fotos/S20/17075752_99.jpg')]").click()
        # self.driver.find_element_by_css_selector("#g17075752 > div > div.swiper-wrapper > div.swiper-slide.swiper-no-swiping.swiper-slide-active > img").click()
        self.driver.find_element_by_css_selector("[alt='Czapka z daszkiem - Plan średni']").click()
