import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class OrderBy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('http://demo.onestepcheckout.com/vip.html')


    def test_select_order_by(self):
        exposed_options = ['Position', 'Name', 'Price']
        active_options = []

        # Buscamos que el select se ecneuntre dentro de la ventana
        select = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div/select')
        select_option = Select(select)

        # Validamos que tenga tres opciones
        self.assertEqual(3, len(select_option.options))

        for option in select_option.options:
            active_options.append(option.text)

        # Validamos que sean las mismas opciones que tenemos quemadas
        self.assertListEqual(exposed_options, active_options)    

        # Validamos que la opcion seleccionada por defecto sea 'Position'
        self.assertEqual('Position', select_option.first_selected_option.text)

        # Seleccionamos otra opcion para validar el cambio
        select_option.select_by_visible_text('Price')

        # Cuando se selecciona otra opcion la url cambia, validamos que sea correcta
        self.assertTrue('http://demo.onestepcheckout.com/vip.html?dir=asc&order=price' in self.driver.current_url)

        # Reseteamos el select
        select_option = Select(self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div/select'))
        select_option.select_by_index(0)

    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)