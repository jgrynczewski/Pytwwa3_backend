import os
import pathlib
import unittest


from selenium import webdriver

driver = webdriver.Chrome()

def get_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

FILE_URI = get_uri("counter.html")

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(FILE_URI)
        self.assertEqual(driver.title, "Licznik")

    def test_increase(self):
        driver.get(FILE_URI)
        increase = driver.find_element_by_id('increase')
        increase.click()
        header_text = driver.find_element_by_tag_name("h1").text
        self.assertEqual(int(header_text), 1)

    def test_multiple_decrease(self):
        driver.get(FILE_URI)
        decrease = driver.find_element_by_id('decrease')
        for item in range(20):
            decrease.click()
        header_text = driver.find_element_by_tag_name('h1').text
        self.assertEqual(int(header_text), -20)


if __name__ == "__main__":
    unittest.main()