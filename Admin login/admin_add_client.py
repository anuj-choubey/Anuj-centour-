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
driver.find_element_by_link_text("Add Client").click()

cust_fun.find_element_by_name(driver, [{'field': 'clientname', 'value': "mistpl"}])
cust_fun.find_element_by_name(driver, [{'field': 'contactperson', 'value': "Anuj"}])
cust_fun.find_element_by_name(driver, [{'field': 'phone', 'value': "621660376111"}])
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "Ajdjhdj@gmaiik.com"}])
cust_fun.find_element_by_name(driver, [{'field': 'address', 'value': "Bhopal mp"}])
cust_fun.find_element_by_name(driver, [{'field': "image_path", 'value': "C://Users//Admin//Pictures//Screenshots//anuj.png.jpg"}])
cust_fun.find_element_by_name(driver, [{'field': 'access_groupt', 'value': "Indore"}])
driver.find_element_by_name("submit").click()