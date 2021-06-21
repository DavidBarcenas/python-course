import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('http://demo.onestepcheckout.com/')

    
    def test_new_user(self):
        driver = self.driver
        # Busca el boton 'Account' y le da click
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        # Dentro del menu selecciona la opcion 'Log In'
        driver.find_element_by_link_text('Log In').click()

        # Dentro de la panta 'Log In', busca el boton para crear una cuenta nueva
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        # Validá que el boton este visible y habilitado para hacer click
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        # Validá que e titulo de la pestaña sea: Create New Customer Account
        self.assertEqual('Create New Customer Account', driver.title)

        # Identificar los elementos del formulario
        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        # Validá que los campos etsen habilitados
        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@mail.com')
        password.send_keys('T123456')
        confirm_password.send_keys('T123456')
        submit_button.click()

    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)