import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.python.org")

about = driver.find_element_by_xpath('//*[@id="about"]/a')
print("xpath done")
hover = ActionChains(driver).move_to_element(about)

print("performing hover actions")
hover.perform()
time.sleep(10)
print("perform time sleep")
cam = driver.find_element_by_xpath('//*[@id="about"]/ul/li[4]/a')
print "clicking cam"
cam.click()