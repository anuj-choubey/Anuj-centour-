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

driver.find_element_by_id("basorelal_uu").click()
cust_fun.find_element_by_name(driver, [{"field": "exp_amount", "value": "888888"}])

cust_fun.find_element_by_name(driver, [{"field": "exp_date", "value": "12/02/2023"}])

cust_fun.find_element_by_name(driver, [{"field": "exp_category", "value": "FOOD"}])

cust_fun.find_element_by_name(driver, [{"field": "comment", "value": "anuj choubey "}])

cust_fun.find_element_by_name(driver, [{"field": "exp_image", "value": "C://Users//Admin//Pictures//Screenshots//Src.png.png "}])
driver.find_element_by_name("submit").click()