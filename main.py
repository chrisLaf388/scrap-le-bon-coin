import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime


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

#click de page suivante
driver.find_element(By.CSS_SELECTOR, ".\\_2WNWW:nth-child(5) .sc-bdvvaa").click()
time.sleep(5)

#affiche numero de page
numeroPageActuel = driver.find_element(By.CSS_SELECTOR, ".\\_21IEe").text

for i in range (10,20):
    try:
    #click sur la card de l'annonce
        driver.find_element(By.CSS_SELECTOR, '.styles_adCard__2YFTi:nth-child('+str(i)+') .AdCardTitle-e546g7-0').click()
        time.sleep(5)

        #Clique sur affiche le numéro
        driver.find_element(By.CSS_SELECTOR, '.tiOck > .\_2qvLx').click()
        time.sleep(1)
        #Affiche le numéro
        print(driver.find_element(By.CSS_SELECTOR, '.tiOck > .\_2qvLx').text)
    except:
        pass

    driver.back()
    time.sleep(5)


