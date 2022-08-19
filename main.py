from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

#create a dataframe with name specialite tel tel1 adresse 
data = pd.DataFrame(columns=['name','specialite','tel','adresse','google_map'])
driver = webdriver.Chrome()
driver.get("https://tunisie-medicale.com/index.php/docteur")
time.sleep(5)
page=0
while(page<3000):
    try:
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
            name = driver.find_element(By.XPATH,"//*[@itemprop='name']").text
            print(name)
            #get element by itemprop="streetAddress"
            StreetAdresse = driver.find_element(By.XPATH,"//*[@itemprop='streetAddress']")
            #get href from StreetAdresse
            google_map = StreetAdresse.get_attribute("href")
            #get element by itemprop="addressLocality"
            addressLocality = driver.find_element(By.XPATH,"//*[@itemprop='addressLocality']")
            #concat text from StreetAdresse and addressLocality
            adresse = StreetAdresse.text+" "+addressLocality.text
            #get element by itemprop="telephone" if exist
            telephone = driver.find_element(By.XPATH,"//*[@itemprop='telephone']").text
            #get element by itemprop="medicalSpecialty"
            specialite = driver.find_element(By.XPATH,"//*[@itemprop='medicalSpecialty']").text
            #add data to dataframe
            data = data.append({'name':name,'specialite':specialite,'tel':telephone,'adresse':adresse,'google_map':google_map},ignore_index=True)

            time.sleep(2)
            #print last row of dataframe
            print(data.tail(1))
    except:
        print("error while getting page")
        print("saving data before continuing...")
        data.to_excel("data.xlsx")
        print("page number: "+str(page))
        print("skip to next page")

        continue




#save data to excel
data.to_excel("docteur.xlsx")
driver.quit()