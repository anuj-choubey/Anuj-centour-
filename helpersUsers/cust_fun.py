
def find_element_by_name(driver, data_list, click_btn=None):
    for data in data_list:
        driver.find_element_by_name(data["field"]).send_keys(data["value"])
    if click_btn:
        driver.find_element_by_name(click_btn).click()




def find_element_by_class_name(driver , data_list ):
    for data in data_list:
        driver.find_element_by_class_name(data["field"]).send_keys(data["value"])

def find_element_by_id(driver,data_list,click_btn=None ):
    for data in data_list :
        driver.find_element_by_id(data["field"])


def find_element_by_xpath(driver, data_list):
    for data in data_list:
        driver.find_element_by_xpath(data ["field"]).send_key(data["value"])
def find_elements_by_class(driver, name, item_num):
       drp_item = driver.find_elements_by_class_name(name)
       drp_item[item_num].click()

