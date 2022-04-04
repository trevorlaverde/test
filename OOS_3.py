  
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
  
#url of the page we want to scrape
url = "https://store.ui.com/collections/unifi-protect/products/unifi-video-g3-flex-camera?variant=16425747447897"
  
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(5) 
  
html = driver.page_source
  
# this renders the JS code and stores all
# of the information in static HTML code.
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find("div", {"class": "relatedProducts__item__data__title"})
inventory = all_divs.find_all('Sold Out')
  
# printing top ten job profiles
count = 0
for inventory in inventory :
    print(jinventory.text)
    count = count + 1
    if(count == 1) :
        print("Out of Stock")
        break
  
driver.close() # closing the webdriver