# Script uses selenium to automatcally launch a browser and go to python.org and then uses python.org search functionality to search for "pycon"


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get('http://www.python.org')
assert "Python" in driver.title

elem=driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
