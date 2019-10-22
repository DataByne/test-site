from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

browser = None

class SearchBox_TestCase( unittest.TestCase ):
    def test_000_no_result( self ):
        browser = webdriver.Chrome()
        browser.get( "http://www.python.org" )
        assert "Python" in browser.title

    
    pass


if __name__ == "__main__":
    unittest.main( verbosity=2 )