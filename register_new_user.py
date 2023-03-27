import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_new_user(self):
        driver = self.driver
        account = driver.find_element(By.XPATH, "//a[contains(@class,'skip-link skip-account')]")
        account.click()
        log_in = driver.find_element(By.XPATH, "//a[text()='Log In']")
        log_in.click()
        create_user_button = driver.find_element(By.XPATH, "//a[@title='Create an Account']")
        create_user_button.click()

    @classmethod
    def tearsDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='search-test-report'))