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
driver.get('https://www.leboncoin.fr/recherche?category=40&text=wii&shippable=1&locations=Marseille_13008__43.22665_5.36869_6492&page=1')
time.sleep(10)
#cookie
driver.find_element_by_xpath('//*[@id="didomi-notice-agree-button"]').click()
time.sleep(5)


#affiche numero de page
numeroPageActuel = ''
numeroPagePrecedent = '123'

while numeroPageActuel != numeroPagePrecedent:
    for i in range (1,42):
        try:
            #click sur la card de l'annonce
            driver.find_element(By.CSS_SELECTOR, '.styles_adCard__2YFTi:nth-child('+str(i)+')').click()
            time.sleep(3)

            try:
                #Verifie si le bouton numéro est présent
                if (driver.find_element_by_xpath('//*[@id="aside"]/div[1]/section/div/div[3]/div[2]/div[1]/button').text == "Voir le numéro"):
                    driver.find_element_by_xpath('//*[@id="aside"]/div[1]/section/div/div[3]/div[2]/div[1]/button').click()
                    time.sleep(2)
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
            pass

    # affiche numero de page avant de changer de page
    numeroPagePrecedent = driver.find_element(By.CSS_SELECTOR, ".\\_21IEe").text
    print('page précédente : '+numeroPagePrecedent)

    # click de page suivante
    driver.find_element(By.CSS_SELECTOR, ".\\_2WNWW:nth-child(5) .sc-bdvvaa").click()
    time.sleep(5)

    # affiche numero de page
    numeroPageActuel = driver.find_element(By.CSS_SELECTOR, ".\\_21IEe").text
    print('numeroPageActuel' + numeroPageActuel)







