#-----------------------------------------------------------------------------------------
from selenium import webdriver
import time
import pandas as pd
import re
from selenium.webdriver.firefox.options import Options #For headless browser

#-----------------------------------------------------------------------------------------
#Strength Shop White
print("Strength Shop White")
#-----------------------------------------------------------------------------------------
# specify the url
urlpage = 'https://www.strengthshop.co.uk/nike-romaleos-4-white-black.html'
print(urlpage)
#-----------------------------------------------------------------------------------------
#Headless browser option

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(urlpage)
print ("Headless Firefox Initialized")
#driver.quit()
#-----------------------------------------------------------------------------------------
#Button not required
#-----------------------------------------------------------------------------------------
#results = driver.find_element_by_xpath("//*[@value='247']").is_enabled()
time.sleep(2)

shoe_code = list(range(247, 267))
data_ss_white = []

for i in shoe_code:
    xpath = "//*[@value='" + str(i) + "']"
    result = driver.find_element_by_xpath(xpath)
    size_text = result.text
    size = re.search(r'(\d+\.?\d*)', size_text).group()

    stock_boo = result.is_enabled()
    data_ss_white.append({"size" : size, "status" : stock_boo})

df_ss_white = pd.DataFrame(data_ss_white)


#-----------------------------------------------------------------------------------------
driver.quit()
#-----------------------------------------------------------------------------------------
#Add column that gives colour and column that gives website
df_ss_white['site'] = 'Strength Shop'
df_ss_white['colour'] = 'White'
#-----------------------------------------------------------------------------------------
print("Strength Shop White Finished Check")
#-----------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------
#Strength Shop Black
print("Strength Shop black")
#-----------------------------------------------------------------------------------------
# specify the url
urlpage = 'https://www.strengthshop.co.uk/nike-romaleos-4-black-white.html'
print(urlpage)
#-----------------------------------------------------------------------------------------
#Headless browser option

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(urlpage)
print ("Headless Firefox Initialized")
#driver.quit()
#-----------------------------------------------------------------------------------------
#Button not required
time.sleep(2)

#-----------------------------------------------------------------------------------------
#results = driver.find_element_by_xpath("//*[@value='247']").is_enabled()
shoe_code = list(range(247, 267))
data_ss_black = []

for i in shoe_code:
    xpath = "//*[@value='" + str(i) + "']"
    result = driver.find_element_by_xpath(xpath)
    size_text = result.text
    size = re.search(r'(\d+\.?\d*)', size_text).group()

    stock_boo = result.is_enabled()
    data_ss_black.append({"size" : size, "status" : stock_boo})

df_ss_black = pd.DataFrame(data_ss_black)

#-----------------------------------------------------------------------------------------
driver.quit()
#-----------------------------------------------------------------------------------------
#Add column that gives colour and column that gives website
df_ss_black['site'] = 'Strength Shop'
df_ss_black['colour'] = 'Black'
#-----------------------------------------------------------------------------------------
print("Strength Shop Black Finished Check")
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
#Append all rows of the 2 dataframes together

frames = [df_ss_white, df_ss_black]
df_ultimate = pd.concat(frames)

#-----------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------
#Stock Checking Alert Function
#-----------------------------------------------------------------------------------------
#Can change this to user input
user_input = '5.5'
# Boolean series TRUE on selected user size
size_select = df_ultimate['size'].isin([user_input])
# Subset original dataframe to only include sizes of interest
subset_df = df_ultimate.loc[size_select]
# Loop through rows of subset dataframe. idx isn't used but must be included when using .iterrows() method
for idx, row in subset_df.iterrows():
    if row['status'] == True: #Max help
        print(row['size'] + " " + row['colour'] + " " + row['site'] + " In Stock GOGOGO")
    else:
        print(row['size'] + " " + row['colour'] + " " + row['site'] + " Not in Stock") #print not this time

#-----------------------------------------------------------------------------------------