import sys

from selenium import webdriver
import unittest

import util

class Test(unittest.TestCase):
    """ Demonstration: Get Chrome to generate fullscreen screenshot """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/usr/lib/enox/chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        ''' Generate document-height screenshot '''
        url = "https://www.principlesofaccounting.com/?page_id=98"
        self.driver.get(url)
        util.fullpage_screenshot(self.driver, "4.png")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])