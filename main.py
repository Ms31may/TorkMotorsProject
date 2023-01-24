from websiteOpen import openWebpage
from driver import df_xpath
from step2 import clickstep2
from step3 import clickstep3
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By

#open the webpage
driver_open_time, driver = openWebpage(df_xpath)
driver = clickstep2(driver,df_xpath)
for state_loop_counter in range(1,34):
    clickstep3(driver,df_xpath,state_loop_counter)


