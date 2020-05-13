from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

# turn on selenium
driver = webdriver.Chrome(r'\Users\aviia\desktop\chromedriver.exe')

# this is where i would stick the url file so that we can iterate through it and pull out the data below.
# maybe set the driver.get to the urls to the ones in the csv

f = open('bdgeekurlsleft.csv', 'r')
lines = f.readlines()

csv_file = open('bdgeek1.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

for i in lines:
    driver.get(i)
    try:
        print('\n')
        print("Scraping Page number ")
        print("+"*40)

        wait_rating = WebDriverWait(driver, 10)
        ratings = wait_rating.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="game ng-scope"]')))

        for rating in ratings:
            game_rating_dict = {}
            time.sleep(0)

                        # print out the rank of the game
            try: 
                rank = rating.find_element_by_xpath('.//*[contains(@class, "rank-number")]').text
                print(rank)
            except:
                continue

                        # get the weight of the game
            try:
                weight = rating.find_element_by_xpath('.//span[contains(@class, "ng-binding gameplay-weight-")]').text
                print(weight) 
            except:
                continue


                        # prints type of game
            try:
                type_of_game = rating.find_element_by_xpath('.//div[contains(@class, "feature-description")]').text
                print(type_of_game) 
            except:
                continue

            game_rating_dict['rank'] = rank
            game_rating_dict['weight'] = weight
            game_rating_dict['type_of_game'] = type_of_game
            writer.writerow(game_rating_dict.values())




     
    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break