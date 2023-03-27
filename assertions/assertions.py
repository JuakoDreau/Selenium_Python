import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AssertionTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_header_cart(self):
        self.assertTrue(self.is_element_present(By.ID, 'header-cart'))

    @classmethod
    def tearsDown(cls):
        cls.driver.quit()
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
             return False
        return True
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)