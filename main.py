# -----------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.firefox.options import Options  # For headless browser
import pandas as pd
import time
import re
import smtplib
from datetime import datetime
import getpass

# -----------------------------------------------------------------------------------------

def web_scrape(url, colour):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(2)

    shoe_code = list(range(247, 267))
    data_ss = []

    for i in shoe_code:
        xpath = "//*[@value='" + str(i) + "']"
        result = driver.find_element_by_xpath(xpath)
        size_text = result.text
        size = re.search(r'(\d+\.?\d*)', size_text).group()

        stock_boo = result.is_enabled()
        data_ss.append({"size": size, "status": stock_boo})

        df_ss = pd.DataFrame(data_ss)
        df_ss['site'] = 'Strength Shop'
        df_ss['colour'] = colour

    return df_ss


# -----------------------------------------------------------------------------------------
def concate_frames(df1, df2):
    frames = [df1, df2]
    df_ultimate = pd.concat(frames)
    return df_ultimate

# -----------------------------------------------------------------------------------------
def size_slice(df_ultimate, user_input):
    size_select = df_ultimate['size'].isin([user_input])
    subset_df = df_ultimate.loc[size_select]
    return subset_df

# -----------------------------------------------------------------------------------------

def send_email(address, password, message):
    """Send an e-mail to yourself!"""
    mailserver = smtplib.SMTP("smtp.office365.com", 587)  # e-mail server
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(address, password)  # login

    SUBJECT = "In Stock Strength Shop!"
    TEXT = str(message)
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    #message = str(message)  # message to email yourself
    mailserver.sendmail(address, address, msg)  # send the email through dedicated server
    mailserver.quit()
    return


# -----------------------------------------------------------------------------------------

def stock_check_listener(url_white, url_black, address, password, user_size):
    """Periodically checks stock information."""
    listen = True  # listen boolean
    while (listen):  # while listen = True, run loop

        df_white = web_scrape(url_white, 'white')
        df_black = web_scrape(url_black, 'black')
        df_ultimate = concate_frames(df1=df_black, df2=df_white)
        df_subset = size_slice(df_ultimate= df_ultimate, user_input=user_size)

        for idx, row in df_subset.iterrows():
            now = datetime.now()
            if row['status'] == False:
                print(str(now) + " " + row['size'] + " " + row['colour'] + " " + row['site'] + ": Not in stock.")
            else:
                message = str(now) + " " + row['size'] + " " + row['colour'] + " " + row['site'] + ": NOW IN STOCK!"
                print(message)
                send_email(address, password, message)
                listen = False

        time.sleep(5*60)  # Wait N minutes to check again.

    return

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    user_size_input = input("Type Size e.g. 8 or 8.5:")
    user_email_input = input("Type Outlook Email address for notifications:")
    user_emailpassword_input = getpass.getpass(prompt="Type Outlook email password: ", stream= None)

    # Run listener to stream stock checks.
    stock_check_listener(url_white='https://www.strengthshop.co.uk/nike-romaleos-4-white-black.html',
                         url_black='https://www.strengthshop.co.uk/nike-romaleos-4-black-white.html',
                         #user_size='6.5',
                         user_size = user_size_input,
                         address = user_email_input,
                         password = user_emailpassword_input
                         )

# -----------------------------------------------------------------------------------------