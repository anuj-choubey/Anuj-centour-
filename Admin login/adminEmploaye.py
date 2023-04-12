import selenium
from selenium import webdriver
from helpersUsers import cust_fun
driver= selenium.webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()

driver.find_element_by_link_text("Employee List").click()
# date
from datetime import datetime, timedelta
# Get today's date
presentday = datetime.now()  # or presentday = datetime.today()
# Get Yesterday
yesterday = presentday - timedelta(1)
# tomorrow = presentday + timedelta(1)
Yesterday =  yesterday.strftime('%d-%m-%Y')
Today = presentday.strftime('%d-%m-%Y')
# Tomorrow = tomorrow.strftime('%d-%m-%Y')
cust_fun.find_element_by_name(driver, [{'field': 'min', 'value': Yesterday}])
cust_fun.find_element_by_name(driver, [{'field': 'max', 'value': Today}])

# driver.find_element_by_link_text("Click").click()
cust_fun.find_elements_by_link_text(driver, [{'field': 'Click', 'value': "5"}])