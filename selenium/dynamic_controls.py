import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class DynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    
    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()

        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')))
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        textbox = driver.find_element_by_css_selector('#input-example > input[type=text]')
        textbox.send_keys('Hello World')
        enable_disable_button.click()
    
    def tearDown(self): 
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)