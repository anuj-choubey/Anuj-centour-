from selenium import webdriver
from helpersUsers import cust_fun
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
# login page
cust_fun.find_element_by_name(driver, [{"field": "empid", "value": "mis1011"}, {"field": "password", "value": "Q!W@e3r4t5"}])
driver.find_element_by_name('login').click()
driver .get("http://localhost/centaur/user/clientp")

# driver .get("http://localhost/centaur/user/clientp")
cust_fun.find_element_by_name(driver, [{"field":"expense_detail","value":"Anuj choubey"}])
cust_fun.find_element_by_name(driver, [{"field":"exp_image","value":"C://Users//Admin//Pictures//Screenshots//Src.png.png"}])
# click on check out button
driver.find_element_by_name("submit").click()


driver.quit()

# Do not open maps