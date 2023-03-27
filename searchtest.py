import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class searchTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com')
        driver.maximize_window()
        driver.implicitly_wait(5)

    # @classmethod
    # def test_search_test_by_id(cls):
    #     search_field = cls.driver.find_element(By.ID, 'search')

    # @classmethod
    # def test_search_test_by_xpath(cls):
    #     search_field = cls.driver.find_element(By.XPATH, "//input[@id='search']")


    # @classmethod
    # def test_search_test_by_class(cls):
    #     search_field = cls.driver.find_element(By.CLASS_NAME, "input-text")

    
    # @classmethod
    # def test_search_test_by_name(cls):
    #     search_field = cls.driver.find_element(By.NAME, "q")
    

    # @classmethod
    # def test_search_button_enable(cls):
    #     button = cls.driver.find_element(By.XPATH, "//button[@title='Search']")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banner = banner_list.find_elements(By.TAG_NAME, "img")
        try:
            assert 3 == len(banner), 'Equals'
        except:
            raise Exception("Not Equals")
            raise TypeError("Not Equals")


    @classmethod
    def tearsDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='search-test-report'))