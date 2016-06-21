from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
# assert "Python" not in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
print "send"
elem.send_keys(Keys.RETURN)
print "RETURN"
# assert "No results found." not in driver.page_source
# driver.close()