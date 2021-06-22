import unittest 
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()
    
    def test_search_salt_shaker(self):
        search_field = self.driver.find_element_by_id('search')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = self.driver.find_elements_by_expath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))


    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name('button')


    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul/li[2]/a/img')

    
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

   
    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reports', 
            report_name='serach-report'
        )
    )