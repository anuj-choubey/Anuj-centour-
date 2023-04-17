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
driver.maximize_window()

driver.find_element_by_link_text("Check-in Report").click()

cust_fun.find_element_by_tag_name(driver,[{"field":'select',"value":'Utkarsh'}])

# Get today's date
# presentday = datetime.now()  # or presentday = datetime.today()
# # Get Yesterday
# yesterday = presentday - timedelta(1)
# # tomorrow = presentday + timedelta(1)
# Yesterday =  yesterday.strftime('%d-%m-%Y')
# Today = presentday.strftime('%d-%m-%Y')
#
# cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': Yesterday}])
# cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': Today}])

driver.find_element_by_class_name("buttons-excel").click()
# cust_fun.find_element_by_link_text(driver,"Click here",2)
driver.find_element_by_link_text("Click here").click()