#-----------------------------------------------------------------------------------------
# Clean Script
#-----------------------------------------------------------------------------------------
from selenium import webdriver
import time
import pandas as pd
import re
from selenium.webdriver.firefox.options import Options #For headless browser
#-----------------------------------------------------------------------------------------
print("Zalando White Romaleos")
#-----------------------------------------------------------------------------------------

# specify the url
urlpage = 'https://www.zalando.co.uk/nike-performance-romaleos-4-sports-shoes-n1244a0en-a11.html'
#print(urlpage)
#-----------------------------------------------------------------------------------------
#Headless browser option

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(urlpage)
print ("Headless Firefox Initialized")
#driver.quit()
#-----------------------------------------------------------------------------------------
#Click button for more html/interactive component

drop_down_button = driver.find_element_by_xpath("//button[@id='picker-trigger' and @class='J1Rmt- _6-WsK3 Md_Vex Nk_Omi _MmCDa _0xLoFW FCIprz NN8L-8 _7Cm1F9 ka2E9k uMhVZi FxZV-M ovwSlD LyRfpJ K82if3 heWLCX mo6ZnF pVrzNP']")
time.sleep(2)
drop_down_button.click()
#-----------------------------------------------------------------------------------------
#https://stackoverflow.com/questions/7867537/how-to-select-a-drop-down-menu-value-with-selenium-using-python
results = driver.find_elements_by_xpath("//*[@class='iJxDek JT3_zV _0xLoFW _78xIQ- EJ4MLB']")
print('Number of results', len(results))
#-----------------------------------------------------------------------------------------
#Loop to get data of interest
# create empty array to store data
data_z_white = []
# loop over results
for result in results: #results is all my text and paths and things that have come out
    shoe_text = result.text
    #shoe_text = shoe_text.encode('ascii', 'ignore') #Note not needed for Python 3
    size_status = re.search(r'(^\d+\.?\d*)\n(.*)', shoe_text)
    size = size_status.group(1)
    status = size_status.group(2)
    # append dict to array
    data_z_white.append({"size" : size, "status1" : status})

    df_z_white = pd.DataFrame(data_z_white)
    #print(df_z_white)

driver.quit()

#-----------------------------------------------------------------------------------------
#Alternative
df_z_white['status'] = (df_z_white['status1'] != "Notify Me")
del df_z_white['status1']
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#Add column that gives colour and column that gives website
df_z_white['site'] = 'Zalando'
df_z_white['colour'] = 'White'
#-----------------------------------------------------------------------------------------
#df_z_white['status'] = df_z_white['status'].replace(to_replace='Notify Me', value=False)
#df_z_white['status'] = df_z_white['status'].replace(to_replace=r"^£", value=True,regex=True)
#Then write code that converts that column from str to boolean
#-----------------------------------------------------------------------------------------
print("Zalando White Finished Check")
#-----------------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------------
#Zalando Black
print("Zalando Black Romaleos")
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
# specify the url
urlpage = 'https://www.zalando.co.uk/nike-performance-romaleos-4-sports-shoes-blackwhite-n1244a0en-q11.html'
#print(urlpage)
#-----------------------------------------------------------------------------------------
#Headless browser option

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(urlpage)
print("Headless Firefox Initialized")
#driver.quit()
#-----------------------------------------------------------------------------------------
#Click button for more html/interactive component

drop_down_button = driver.find_element_by_xpath("//button[@id='picker-trigger' and @class='J1Rmt- _6-WsK3 Md_Vex Nk_Omi _MmCDa _0xLoFW FCIprz NN8L-8 _7Cm1F9 ka2E9k uMhVZi FxZV-M ovwSlD LyRfpJ K82if3 heWLCX mo6ZnF pVrzNP']")
time.sleep(2)
driver.execute_script("arguments[0].click();", drop_down_button)
#selenium.common.exceptions.ElementClickInterceptedException: Message: Element <button id="picker-trigger" class="J1Rmt- _6-WsK3 Md_Vex Nk_Omi _MmCDa _0xLoFW FCIprz NN8L-8 _7Cm1F9 ka2E9k uMhVZi FxZV-M ovwSlD LyRfpJ K82if3 heWLCX mo6ZnF pVrzNP" type="button"> is not clickable at point (1037,508) because another element <b> obscures it
#-----------------------------------------------------------------------------------------
results = driver.find_elements_by_xpath("//*[@class='iJxDek JT3_zV _0xLoFW _78xIQ- EJ4MLB']")
print('Number of results', len(results))

shoe_text = results[9].text
size_status = re.search(r'(^\d+\.?\d*)', shoe_text).group()
size_status = "Notify Me" not in shoe_text
#-----------------------------------------------------------------------------------------
#Loop to get data of interest
# create empty array to store data
data_z_black = []
# loop over results
for result in results: #results is all my text and paths and things that have come out
    shoe_text = result.text
    #shoe_text = shoe_text.encode('ascii', 'ignore')
    size = re.search(r'(^\d+\.?\d*)', shoe_text).group()
    status = "Notify Me" not in shoe_text
    # append dict to array
    data_z_black.append({"size" : size, "status" : status})

    df_z_black = pd.DataFrame(data_z_black)
    #print(df_z_black)

driver.quit()
#-----------------------------------------------------------
#Add column that gives colour and column that gives website
df_z_black['site'] = 'Zalando'
df_z_black['colour'] = 'Black'
#-----------------------------------------------------------------------------------------
print("Zalando Black Finished Check")
#-----------------------------------------------------------------------------------------
#Concat both dataframes together
frames = [df_z_white, df_z_black]
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
    if row['status'] == True:
        print(row['size'] + " " + row['colour'] + " " + row['site'] + " In Stock GOGOGO")
    else:
        print(row['size'] + " " + row['colour'] + " " + row['site'] + " Not in Stock") #print not this time

#-----------------------------------------------------------------------------------------
