import time

import selenium
from selenium import webdriver
from helpersAdmin import cust_fun
driver= selenium.webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()

driver.find_element_by_link_text("Employee List").click()

# driver.find_element_by_link_text("Click").click()
cust_fun.find_element_by_link_text(driver, "Click",5)

driver.find_element_by_name("name").clear()
cust_fun.find_element_by_name(driver, [{'field': 'name', 'value': "Anuj choubey"}])

driver.find_element_by_name("empid").clear()
cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value':"mis1111"}])

driver.find_element_by_name("phone").clear()
cust_fun.find_element_by_name(driver, [{'field': 'phone', 'value':"6363636363"}])
time.sleep(3)
driver.find_element_by_name("email").clear()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "anuj@gmail.com"}])
time.sleep(2)
# location
cust_fun.find_element_by_name(driver, [{'field': 'access_group', 'value': "Bhopal"}])
time.sleep(2)
# role
cust_fun.find_element_by_name(driver, [{'field': 'role', 'value': "Executive"}])
time.sleep(2)
driver.find_element_by_name("password").clear()
cust_fun.find_element_by_name(driver, [{'field': 'password', 'value': "Anuj@123"}])

driver.find_element_by_name("image_path").clear()
cust_fun.find_element_by_name(driver, [{'field': 'image_path', 'value': "D://Users//Anuj Choubey//Selenium testing//src.png.png"}])

# submit button
driver.find_element_by_name("submit").click()