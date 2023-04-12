# import driver as driver
from selenium import webdriver

# my custom import
from helpersUsers import cust_fun

driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver .get("http://localhost/centaur/")
driver.implicitly_wait(5)

# Enter incorrect password
cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "Q!W@e3r4t"}], 'login')

driver.back()

driver .get("http://localhost/centaur/")

# Enter correct password
cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')

# Click on log out button
driver.find_element_by_class_name('fa-user').click()

# Enter incorrect id
cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis101"}, {'field': 'password', 'value': "Q!W@e3r4t"}], 'login')

# Enter correct id
cust_fun.find_element_by_name(driver, [{'field': 'empid', 'value': "mis1011"}, {'field': 'password', 'value': "Q!W@e3r4t5"}], 'login')

# Meassage are showing on screen "in correct id and password "

driver.quit()