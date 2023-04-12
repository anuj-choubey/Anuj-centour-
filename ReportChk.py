from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
# login page
cust_fun.find_element_by_name(driver, [{"field": "empid", "value": "mis1011"}, {"field": "password", "value": "Q!W@e3r4t5"}])
driver.find_element_by_name('login').click()

driver.find_element_by_class_name("dropdown-toggle").click()
# drp_item = driver.find_elements_by_class_name("dropdown-item")


# drp_item[1].click()
cust_fun.find_elements_by_class(driver, 'dropdown-item', 0)
driver.find_element_by_class_name("dropdown-toggle").click()
driver.find_element_by_partial_link_text("Click here").click()
cust_fun.find_element_by_name(driver, [{"field": "expense_amount", "value": "22222"}])
# driver.find_element_by_name("discussion").clear()
cust_fun.find_element_by_name(driver, [{"field": "discussion", "value": "Aman gupta "}])
driver.find_element_by_class_name("btn-primary").click()


driver.quit()

