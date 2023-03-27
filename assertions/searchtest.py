import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')

        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()
    
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')

        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements(By.XPATH, "//a[text()='Stone Salt and Pepper Shakers']")
        assert 1 == len(products), 'OK - Equals'

    @classmethod
    def tearsDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)