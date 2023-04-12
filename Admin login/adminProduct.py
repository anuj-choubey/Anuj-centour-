from selenium import webdriver
from helpersUsers import cust_fun
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()
driver.find_element_by_link_text("Products").click()
driver.find_element_by_class_name("btn-outline-primary").click()
# select wattage
driver.find_element_by_class_name("form-select ").click()
cust_fun.find_elements_by_class(driver, 'form-control', 4)
# select shape
driver.find_element_by_class_name("form-group ").click()
cust_fun.find_elements_by_class(driver, 'form-control', 4)
# Enter Quantity
cust_fun.find_element_by_class_name(driver, [{'field': 'amnt', 'value': "400"}])
# Discounted
cust_fun.find_element_by_id(driver,[{'field': 'price5', 'value': "66"}])
