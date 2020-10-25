from selenium import webdriver
import unittest
import time
class Test_log(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://erp.lemfix.com/login.html")
    def tearDown(self):
        time.sleep(5)

    # def test_title(self):
    #     driver = self.driver

    def test_login(self):
        driver = self.driver
        #验证title
        if driver.title == "柠檬ERP":
            print("标题一致,该页面标题为:",driver.title)
        else:
            print("标题不一致，该页面标题为：", driver.title)
        #登录操作
        driver.find_element_by_css_selector("#username").send_keys("test123")
        driver.find_element_by_css_selector("#password").send_keys("123456")
        driver.find_element_by_css_selector('[title="公共场所慎用,下次不需要再填写帐号"] .iCheck-helper').click()
        driver.find_element_by_css_selector("#btnSubmit").click()
        print("登录成功")
        time.sleep(1)
        #验证用户名
        text = driver.find_element_by_css_selector(".user-panel p").text
        if "测试用户" == text:
            print("当前用户与预期一致，用户为:",text)
        else:
            print("当前用户与预期不一致，当前用户为:",text)
        time.sleep(1)
        #验证 零售出库 菜单能正常打开
        #driver.find_element_by_css_selector('[title="零售管理"]').click()

        driver.find_element_by_css_selector('[title="零售出库"]').click()
        print("零售出库正常打开")
        time.sleep(1)
        #elel = driver.find_element_by_css_selector("[src='/pages/materials/retail_out_list.html']")

        driver.switch_to.frame(1)
        time.sleep(5)
        driver.find_element_by_css_selector("#searchNumber").send_keys("1234")
        time.sleep(5)
      #  driver.find_element_by_id("searchBeginTime").click()
        driver.find_element_by_css_selector("#searchBtn").click()
   #     driver.find_element_by_css_selector('[value="214"]')
   #     driver.find_element_by_css_selector("#addDepotHead .l-btn-left span")
        print("搜索成功")




