from gsheetReader import gsheet_reader
import configparser
from selenium import webdriver                             #to open the browser
config = configparser.ConfigParser()
config.readfp(open(r'config.ini'))
download_folder = config.get('download','folder')


#create the xpaths dataframe by reading googlesheet , 
## The automation process will be completed from here
config = configparser.ConfigParser()
config.readfp(open(r'config.ini'))
df_xpath = gsheet_reader(config.get('gsheet','url'))
###########################################################################################################################
## Open the webpage :
    

#change download folder
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\mohit\\Desktop\\TorkMotors\\Vahan\\TorkMotorsProject\\download_vahan\\","directory_upgrade": True}   
#extra \ in the download folder directory address, and 'upgrade' option is very imp

options.add_experimental_option("prefs",prefs)

#open chrome instance
driver = webdriver.Chrome(executable_path='./chromedriver',options=options)