import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class helloWorld(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = cls.driver
        driver.implicitly_wait(5)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://platzi.com')

    def test_visit_youtube(self):
        driver = self.driver
        driver.get('https://www.youtube.com')

    @classmethod
    def tearsDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))