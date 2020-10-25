import time
def login_page(username,password,driver):
    driver.find_element_by_css_selector("#username").send_keys("test123")
    driver.find_element_by_css_selector("#password").send_keys("123456")
    driver.find_element_by_css_selector('[title="公共场所慎用,下次不需要再填写帐号"] .iCheck-helper').click()
    driver.find_element_by_css_selector("#btnSubmit").click()
def open_url(url,driver):
    driver.get(url)


def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    time.sleep(2)
    driver.find_element_by_css_selector('[title="零售出库"]').click()
    print("零售出库正常打开")
    time.sleep(1)
    # elel = driver.find_element_by_css_selector("[src='/pages/materials/retail_out_list.html']")

    driver.switch_to.frame(1)
    time.sleep(5)
    driver.find_element_by_css_selector("#searchNumber").send_keys(s_key)
    time.sleep(5)
    #  driver.find_element_by_id("searchBeginTime").click()
    driver.find_element_by_css_selector("#searchBtn").click()
#     driver.find_element_by_css_selector('[value="214"]')
#     driver.find_element_by_css_selector("#addDepotHea