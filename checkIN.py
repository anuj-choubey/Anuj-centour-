from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
# login page
cust_fun.find_element_by_name(driver, [{"field": "empid", "value": "mis1011"}, {"field": "password", "value": "Q!W@e3r4t5"}])
driver.find_element_by_name('login').click()
# enter a check in page
driver .get("http://localhost/centaur/user/clientp")
# click in check in button
driver.find_element_by_class_name("nav-link").click()

cust_fun.find_element_by_name(driver, [{"field": "clientname","value":"anuj"}])
cust_fun.find_element_by_name(driver, [{"field":"premise_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
cust_fun.find_element_by_name(driver, [{"field":"discussion","value":"Anuj choubey samanpur seth"}])
driver.find_element_by_name("submit").click()
# # check out process
# cust_fun.find_element_by_name(driver, [{"field":"expense_detail","value":"Anuj choubey samanpur seth"}])
# cust_fun.find_element_by_name(driver, [{"field":"exp_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
# # click on check out button
# driver.find_element_by_name("submit").click()


driver.quit()