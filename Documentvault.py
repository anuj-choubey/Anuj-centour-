from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
driver .get("http://localhost/centaur/")
# login page
cust_fun.find_element_by_name(driver, [{"field": "empid", "value": "mis1011"}, {"field": "password", "value": "Q!W@e3r4t5"}])
driver.find_element_by_name('login').click()
driver.find_element_by_id("syamlal_uu").click()
# driver.find_element_by_class_name("fs-3").click()
doc_vout=driver.find_elements_by_class_name("fa-download")
doc_vout[5].click()
driver.quit()