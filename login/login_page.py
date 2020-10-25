import time
def login_page(driver,username,password):
    driver.find_element_by_css_selector("#username").send_keys(username)
    driver.find_element_by_css_selector("#password").send_keys(password)
    driver.find_element_by_css_selector('[title="公共场所慎用,下次不需要再填写帐号"] .iCheck-helper').click()
    driver.find_element_by_css_selector("#btnSubmit").click()
def open_url(driver,url):
    driver.get(url)


def search_key(url,driver,username,password,s_key):
    open_url(driver,url)
    login_page(driver,username,password)
    time.sleep(2)
    driver.find_element_by_css_selector('[title="零售出库"]').click()
    driver.switch_to.frame(1)
    time.sleep(5)
    driver.find_element_by_css_selector("#searchNumber").send_keys(s_key)
    time.sleep(5)
    #  driver.find_element_by_id("searchBeginTime").click()
    driver.find_element_by_css_selector("#searchBtn").click()
