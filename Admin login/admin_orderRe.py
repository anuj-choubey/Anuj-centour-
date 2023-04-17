import selenium
import time
from datetime import datetime, timedelta
from selenium import webdriver
from helpersAdmin import cust_fun
driver= selenium.webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()
driver.find_element_by_link_text("Report").click()

driver.find_element_by_link_text("Orders Report").click()
driver.maximize_window()
# cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': "05/01/2013"}])
# cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': "01/01/2023"}])

driver.find_element_by_xpath("//body/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/input[1]").send_keys("LED BULB")

cust_fun.find_elements_by_class(driver,"fs-3",6)
time.sleep(3)
driver.find_element_by_class_name("fa-user").click()