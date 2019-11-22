from selenium.webdriver.common.by import By
from selenium import webdriver

class game_page():


    #Selectors
    GATHER_CATNIP_BUTTON = (By.XPATH, "")
    REFINE_CATNIP_BUTTON = (By.XPATH, "")




    def __init__(self, driver):
        self.driver = driver

    def click_gather_catnip(self):
        self.driver.find_element(*self.GATHER_CATNIP_BUTTON).click()


    def refine_catnip(self):
        self.driver.find_element(*self.REFINE_CATNIP_BUTTON).click()



