from datetime import datetime
import time


#this process is done twice. hence the name filter_selector_2x2times
#xpaths of the dropdown click and the option to be selected are given by calling function
#if this function is successful the option selected in filter is returned
#need to implement return(0) if there is error in this function

def filter_selector_2x2times(driver, dropdown_xpath, option_xpath):
    driver.find_element("xpath", dropdown_xpath).click()      # click on the dropdown to expand it
    driver.find_element("xpath", option_xpath).click()          # click on the desired option name

    time.sleep(1)                                                                      # wait 1 sec before repeat click
    driver.find_element("xpath", option_xpath).click()          # click on the desired option name

    #repeating the process due to weird website behaviour
    driver.find_element("xpath", dropdown_xpath).click()      # click on the dropdown to expand it
    driver.find_element("xpath", option_xpath).click()          # click on the desired option name

    time.sleep(1)                                                                      # wait 1 sec before repeat click
    driver.find_element("xpath", option_xpath).click()          # click on the desired option name
    
    #get the name of the option selected
    filter_display = driver.find_element("xpath", dropdown_xpath).text
    
    return(filter_display)    
### function to click on the 'Year' drop down, click on 2022-23 in dropdown
def filter_selector_1x1times(driver, dropdown_xpath, option_xpath):
    driver.find_element("xpath", dropdown_xpath).click()         # click on the dropdown to expand it
    driver.find_element("xpath", option_xpath).click()             # click on the desired xaxis name
    time.sleep(1)                                                                       #wait 1 sec in case anything is running
    
    filter_display = driver.find_element("xpath", dropdown_xpath).text
    
    return(filter_display)
#function to get the display name of the filter on website
def filtered_selection(driver,dropdown_xpath):
    filter_display = driver.find_element("xpath", dropdown_xpath).text
    return(filter_display)
