import time
from driver import driver
def openWebpage(df_xpath):

 
    # open the target URL given in xpaths dataframe
    driver.get(df_xpath['relXpath']['website link'])
    
    # Wait for 2 seconds to load the webpage completely
    time.sleep(2)
    
    # to check time when webdriver was opened.If website refreshes every 30mins, new driver will have to be opened before refresh
    driver_open_time = time.time()
    return driver_open_time, driver
