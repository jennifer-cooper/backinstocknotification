# Back in Stock Notification for Nike Romaleos 4
### Author: Jennifer Cooper
## Rationale
Nike Romaleo 4 shoes are extremely low stock for smaller female sizes in the UK (i.e. UK 5.5 and lower) - this script checks for stock using a user inputted size and sends automatic email notifications.
21st December 2021

![image](images.jpg)

| .py                                  | Description                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------|
| main.py                              | The complete script for Strength Shop which will send an email notification when an item comes back into stock |
| strengthshop_romaleo_notification.py | Strength Shop - Code which checks stock in one instance and prints whether in stock or not                     |
| Zalando_romaleo_notification.py      | Zalando - Code which checks stock in one instance and prints whether in stock or not                           |

## Summary
This project uses Strength Shop as the main website but also includes code for Zalando.

*Note Strength Shop lists the Male Sizes so UK size 5.5 is actually a regular female UK size 5.

The user enters their shoe size, email address and password (which is hidden). The script then uses web scraping to obtain the data of interest using Selenium, Firefox and GeckoDriver.
A function then checks the data for a True statement for a particular size and will email the user with a back in stock notification. If the data is false then the script will initiate a while loop printing 'Not in stock' and checking every 5 minutes continually until a true statement is met which will exit the loop.

Both the black and white versions of the shoes are checked.

Mac OS has been used for this project (Python 3.10 run through PyCharm 2021.2.1 Community Edition) but the setup is the same for Windows OS.

## More detailed summary of coding steps

1. Look at underlying html code on a webpage to determine what elements could be used
for a back in stock notification.
(e.g. You can use 'More tools'> 'developer tools' on a chrome browser or you can right click and inspect source)
Look for stock inventory words or sold out or enabled and disabled elements etc and compare code to those
not sold out. 
2. Online retailers often have dynamic web pages that load content using javascript
First port of call would be to use BeautifulSoup to extract information e.g.
```
results = soup.find_all('div', attrs={'class': 'xxxxx'})
print('Number of results', len(results)) 
```
3. This wont return results if there are dynamic features on the web page like Zalando. Not all the HTML will load until a button is pressed or you interact with the webpage in a certain way. 
This would suggest that javascript is being used.
4. We can use Python package Selenium and a web-driver (Geckodriver) to access the webpage and interact with it for the underlying html code. 
5. Download GeckoDriver and put it in PATH or specify driver path in Python code:
https://github.com/mozilla/geckodriver/releases
The project used the following version: geckodriver-v0.30.0-macos.tar.gz
6. Firefox (95.0.2)  was downloaded and used with GeckoDriver
https://www.mozilla.org/en-GB/firefox/new/
7. Within the Python code you can initialise a headless Firefox session 
8. For Strength Shop sold out shoe sizes are identified through a disabled element 
9. The following functions were produced in Python and orchestrated using the following at the end of the script:
```
if __name__ == "__main__":
```
9. A function for webscraping from Strength Shop for different colours of Romaleos
10. A function to email yourself a notification using smtplib and Outlook on Office 365 online
11. A function to concatenate the dataframes for both white and black urls 
12. A function to slice the dataframe using user input of size
13. A listener which implements a while loop if the shoes are not in stock in the user defined size and exits the loop if the shoes become in stock sending an email
14. If shoes arent in stock then the script will wait 5 minutes before checking the webpage again

## Next Steps
* Use Tkinter for interactive popups
* Make a version which will work on all operating systems without additional setup like Gecko Driver and Firefox (only for Strength Shop, BeautifulSoup)
* Allow a user to input multiple sizes, maybe even colour
* Create an asset from .exe (using travis?)
* Include an option to run for 'x' number of hours
* Incorporate Unit testing (pytest)
* Program Raspberry Pi as server instead of running on PC continually
* User defined time.sleep

## URLs
* https://www.zalando.co.uk/nike-performance-romaleos-4-sports-shoes-n1244a0en-a11.html
* https://www.zalando.co.uk/nike-performance-romaleos-4-sports-shoes-blackwhite-n1244a0en-q11.html
* https://www.strengthshop.co.uk/nike-romaleos-4-white-black.html
* https://www.strengthshop.co.uk/nike-romaleos-4-black-white

## Resources used
Sending emails Outlook Office 365:
https://pretagteam.com/question/how-to-send-smtp-email-for-office365-with-python-using-tlsssl

Dynamic webpage/Javascript Web Scraping:
https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

https://stackoverflow.com/questions/6332577/send-outlook-email-via-python
https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353
https://stackoverflow.com/questions/46160886/how-to-send-smtp-email-for-office365-with-python-using-tls-ssl

Click a button:
https://stackoverflow.com/questions/7867537/how-to-select-a-drop-down-menu-value-with-selenium-using-python

Regular Expression Tutorial:
https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial

Masking Password for User Input:
https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered

## Trouble Shooting and Useful Code

Workaround GeckoDriver Mac Permissions:
https://github.com/mozilla/geckodriver/issues/1629

Methodology:
https://stackoverflow.com/questions/48095700/web-scraping-back-in-stock-notification/48096692

Non clickable element:
https://stackoverflow.com/questions/49252880/element-is-not-clickable-at-point-x-y-5-because-another-element-obscures-it/49261182