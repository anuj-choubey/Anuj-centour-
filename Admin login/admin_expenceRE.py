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
driver.find_element_by_link_text("Expense Report").click()

cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': "04/10/2013"}])
cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': "02/11/2023"}])

cust_fun. find_elements_by_class(driver, "exp_approve", 6)
cust_fun. find_elements_by_class(driver,"fa-download ", 6)

#Error - Your Absoluthe Path is: C:\xampp\htdocs\centaur  - click on download button