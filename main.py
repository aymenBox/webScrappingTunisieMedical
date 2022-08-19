from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://tunisie-medicale.com/index.php/docteur")
time.sleep(5)
page=0
while(page<3000):
    page=page+20
    driver.get("https://tunisie-medicale.com/index.php/docteur/index/"+str(page))
    time.sleep(5)
driver.close()