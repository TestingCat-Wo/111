from selenium import webdriver
#from login import login_page
from day01 import lesson_06
from data import test_data

driver = webdriver.Firefox()
url = test_data.url["url"]
username = test_data.login_data["username"]
password = test_data.login_data["password"]
s_key = test_data.s_key["s_key"]
print(url,password,username,s_key)
lesson_06.search_key(driver=driver,url=url,username=username,password=password,s_key=s_key)