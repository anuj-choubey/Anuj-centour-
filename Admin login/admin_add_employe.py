import selenium
from selenium import webdriver
from helpersAdmin import cust_fun
driver= selenium.webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()
driver.find_element_by_class_name("dropdown-toggle").click()
driver.find_element_by_link_text("Add Employee").click()

cust_fun.find_element_by_name(driver, [{'field': 'name', 'value': "ANUJ CHOUBEY"}])
cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "cs000111"}])
cust_fun.find_element_by_name(driver, [{'field': 'phone', 'value': "8374734474387"}])
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "dddsk@gmail.com"}])
cust_fun.find_element_by_name(driver, [{'field': 'access_group', 'value': "Indore "}])
cust_fun.find_element_by_name(driver, [{'field': 'role', 'value': "Manager 3 "}])
cust_fun.find_element_by_name(driver, [{'field': 'password', 'value': "Anujchopubey22 "}])
cust_fun.find_element_by_name(driver, [{'field': 'image_path', 'value': "D://Users//Anuj Choubey//Selenium testing//src.png.png"}])
driver.find_element_by_class_name("btn-primary").click()