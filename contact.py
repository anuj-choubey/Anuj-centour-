from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
# login page
driver.maximize_window()
cust_fun.find_element_by_name(driver, [{"field": "empid", "value": "mis1011"}, {"field": "password", "value": "Q!W@e3r4t5"}])
driver.find_element_by_name('login').click()

driver.find_element_by_link_text("Contact US").click()