from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        self.driver = webdriver.Chrome('/Users/christianfinn/Python Projects/wild_vanimals_instabot/chromedriver',
                                       chrome_options=self.options)
        self.driver.implicitly_wait(15)

    def get_page(self, web_page_link):
        self.driver.get(web_page_link)

    def type_in_box(self, method, identifier, text):
        if method == 'XPATH':
            element = self.driver.find_element(By.XPATH, identifier)
            element.send_keys(text)
        elif method == "SELECTOR":
            element = self.driver.find_element(By.CSS_SELECTOR, identifier)
            element.send_keys(text)
        elif method == "ID":
            element = self.driver.find_element(By.ID, identifier)
            element.send_keys(text)
        else:
            print("Method does not match")

    def click(self, method, identifier):
        if method == 'XPATH':
            self.driver.find_element(By.XPATH, identifier).click()
        elif method == "SELECTOR":
            self.driver.find_element(By.CSS_SELECTOR, identifier).click()
        elif method == "ID":
            self.driver.find_element(By.ID, identifier).click()
        else:
            print("Method does not match")
            
    def select_all(self, identifier):
        return self.driver.find_elements(By.CSS_SELECTOR, identifier)

    def source(self):
        time.sleep(3)
        return self.driver.page_source

    def close(self):
        self.driver.close()

    def refresh(self):
        self.driver.refresh()


# def get_page(driver, web_page_link):
#     driver.get(web_page_link)
#
#
# def type_in_box(driver, method, identifier, text):
#     if method == 'XPATH':
#         element = driver.find_element(By.XPATH, identifier)
#         element.send_keys(text)
#     elif method == "SELECTOR":
#         element = driver.find_element(By.CSS_SELECTOR, identifier)
#         element.send_keys(text)
#     elif method == "ID":
#         element = driver.find_element(By.ID, identifier)
#         element.send_keys(text)
#     else:
#         print("Method does not match")
#
#
# def click(driver, method, identifier):
#     if method == 'XPATH':
#         driver.find_element(By.XPATH, identifier).click()
#     elif method == "SELECTOR":
#         driver.find_element(By.CSS_SELECTOR, identifier).click()
#     elif method == "ID":
#         driver.find_element(By.ID, identifier).click()
#     else:
#         print("Method does not match")
#
#
# def source(driver):
#     time.sleep(3)
#     return driver.page_source
#
#
# def close(driver):
#     driver.close()
#
#
# def refresh(driver):
#     driver.refresh()
