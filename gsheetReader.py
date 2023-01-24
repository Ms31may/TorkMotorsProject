import pandas as pd
###*** function to read URL, and xpaths of all elements of the parivahan website from gsheet maintained separately
#this info is stored in a dataframe and returned to calling code
def gsheet_reader(url_passed):
    sheet_url = url_passed
    url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df_xpath=pd.read_csv(url_1,index_col=0)
    return (df_xpath)