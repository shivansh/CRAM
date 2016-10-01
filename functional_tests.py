from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_start(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
                )
        # self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
