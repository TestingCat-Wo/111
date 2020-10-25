from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/login.html")
#driver.find_element_by_css_selector("#username").send_keys("test123")
driver.find_element_by_xpath("//*[contains(@id,'username')]").send_keys("12314")
