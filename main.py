from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

#create a dataframe with name specialite tel tel1 adresse 
data = pd.DataFrame(columns=['name','specialite','tel','tel1','adresse'])
driver = webdriver.Chrome()
driver.get("https://tunisie-medicale.com/index.php/docteur")
time.sleep(5)
page=0
while(page<3000):
    page=page+20
    driver.get("https://tunisie-medicale.com/index.php/docteur/index/"+str(page))
    #find divs with class="col-lg-6 col-md-6 col-sm-6 col-xs-12"
    divs = driver.find_elements(By.CLASS_NAME,"col-lg-6.col-md-6.col-sm-6.col-xs-12")
    print(divs)
    links=[]
    #get first links of each div
    for div in divs:
        links.append(div.find_element(By.TAG_NAME,"a").get_attribute("href"))
    time.sleep(2)
    for link in links:
        #got to link
        driver.get(link)
        time.sleep(5)
        #get element by itemprop="name"
        name = driver.find_element(By.XPATH,"//*[@itemprop='name']")
        print(name.text)
        time.sleep(2)




#save data to excel
data.to_excel("docteur.xlsx")
driver.quit()