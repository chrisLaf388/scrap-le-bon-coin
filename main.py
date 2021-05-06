import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime

tels= []


# Ouverture de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')

#navigation privé
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver.maximize_window()
# Lien de la page formulaire
pageContinue = True
compt = 0
erreurFinDeProg = 0

while pageContinue:
    compt+=1
    driver.get('https://www.leboncoin.fr/recherche?text=wii&shippable=1&locations=Marseille_13008__43.22665_5.36869_6492&page='+str(compt))
    time.sleep(10)
    #cookie
    driver.find_element_by_xpath('//*[@id="didomi-notice-agree-button"]').click()
    time.sleep(5)

    # affiche numero de page
    numeroPageActuel = driver.find_element(By.CSS_SELECTOR, ".\\_21IEe").text
    print('numeroPageActuel' + numeroPageActuel)


    for i in range (1,42):
        try:
            #click sur la card de l'annonce
            driver.find_element(By.CSS_SELECTOR, '.styles_adCard__2YFTi:nth-child('+str(i)+')').click()
            time.sleep(3)

            try:
                #Verifie si le bouton numéro est présent
                if (driver.find_element_by_xpath('//*[@id="aside"]/div[1]/section/div/div[3]/div[2]/div[1]/button').text == "Voir le numéro"):
                    driver.find_element_by_xpath('//*[@id="aside"]/div[1]/section/div/div[3]/div[2]/div[1]/button').click()
                    time.sleep(5)
                    print(driver.find_element_by_xpath('//*[@id="aside"]/div[1]/section/div/div[3]/div[2]/div[1]/a').text)
                    tel = driver.find_element_by_xpath('//*[@id="aside"]/div[1]/section/div/div[3]/div[2]/div[1]/a').text

                    telExistant = False
                    for j in tels:
                        if tel == j :
                            telExistant=True

                    if telExistant != True :
                        tels.append(tel)

                else:
                    print("pas de num")
            except:
                driver.back()
                time.sleep(5)


            driver.back()
            time.sleep(5)
        except:
            erreurFinDeProg +=1
            pass

        if erreurFinDeProg == 10:
            pageContinue = False
            break

    driver.quit()










