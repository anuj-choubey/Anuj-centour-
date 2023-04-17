import selenium
import time
from datetime import datetime, timedelta
from selenium import webdriver
from helpersAdmin import cust_fun
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
driver= selenium.webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()
driver.find_element_by_link_text("Report").click()
driver.find_element_by_link_text("Attendance Report").click()

# cust_fun.find_element_by_name(driver, [{'field': 'min', 'value':"02/15/2023"}])
# cust_fun.find_element_by_name(driver, [{'field': 'max', 'value':"02/15/2023"}])


#  search  var properly working
cust_fun.find_element_by_class_name(driver, [{'field': 'form-control-sm', 'value':"	centura001"}])
