import time

from selenium import webdriver
from helpersUsers import cust_fun

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver .get("http://localhost/centaur/")
driver.find_element_by_link_text("Click here").click()

# Wrong password Enter
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@32"}])
driver.find_element_by_class_name("btn-block").click()
time .sleep(4)
# admin login
cust_fun.find_element_by_name(driver, [{'field': 'email', 'value': "centura001"}, {'field': 'password', 'value': "centura@321"}])
driver.find_element_by_class_name("btn-block").click()

# Document vault
driver.find_element_by_link_text("Document Vault").click()
cust_fun.find_element_by_name(driver, [{'field': 'title', 'value': "Solar light"}])
cust_fun.find_element_by_name(driver, [{'field': 'document_address', 'value': "D:\\Users\\Anuj Choubey\\Selenium testing\\src.png.png"}])
driver.find_element_by_name("submit").click()

driver.find_element_by_id("35").click()
time.sleep(3)
alert = driver.switch_to.alert #This .alert will work For Python
try:
   alert.accept() #If you want to Accept the Alert
except:
   alert.dismiss()
time.sleep(3)
driver.find_element_by_class_name("fa-download").click()
time.sleep(2)