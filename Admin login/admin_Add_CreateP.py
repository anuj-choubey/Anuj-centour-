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
driver.find_element_by_class_name("dropdown-item").click()
cust_fun.find_element_by_name(driver, [{'field': 'product_file', 'value': "D://Users//Anuj Choubey//Selenium testing//Check-in Report.xlsx"}])
driver.find_element_by_class_name( "btn-primary").click()