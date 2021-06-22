from logging import exception
import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    
    def test_sort_tables(self):
        driver = self.driver

        total_columns = 5
        total_rows = 4

        table_data = [[] for i in range(total_columns)]

        for i in range(total_columns):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(total_rows):
                try:
                    row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                    table_data[i].append(row_data.text)
                except:
                    break


        for i in table_data:
            print(i)

    
    def tearDown(self): 
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)