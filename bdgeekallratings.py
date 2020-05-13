from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

# turn on selenium
driver = webdriver.Chrome(r'\Users\aviia\desktop\chromedriver.exe')

# go to the ranking area of the site
driver.get("https://boardgamegeek.com/browse/boardgame")

csv_file = open('bdgeekallratings.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# it takes 56 seconds to do 2 pages
# it takes 107 seconds to do 4 pages
# 185 pages should take about 1 hours 23 minutes if everthing is somewhat consistent.
# index*100 is the amount of games rank you are going to find

index = 1
while index < 186:
    try:
        print('\n')
        print("Scraping Page number " + str(index))
        print("+"*40)
        index += 1

        wait_rating = WebDriverWait(driver, 10)
        ratings = wait_rating.until(EC.presence_of_all_elements_located((By.XPATH,'//div/table[@class="collection_table"]//tr')))

        for rating in ratings:
            game_rating_dict = {}
            time.sleep(0)

            # print out the rank of the game
            try: 
                rank = rating.find_element_by_xpath('.//*[contains(@class, "collection_rank")]').text
                print(rank)
            except:
                continue

            # # print out the title of the game
            try: 
                title = rating.find_element_by_xpath('.//div[contains(@id, "results_objectname")]//a').text
                print(title)
            except:
                continue

            # # print out the geek rating of the game
            try: 
                geek_rating = rating.find_element_by_xpath('.//td[4][contains(@class, "collection_bggrating")]').text
                print(geek_rating)
            except:
                continue

            # # print out the average rating of the game
            try: 
                avg_rating = rating.find_element_by_xpath('.//td[5][contains(@class, "collection_bggrating")]').text
                print(avg_rating)
            except:
                continue

            # # print out the number of ratings of the game
            try: 
                num_of_rating = rating.find_element_by_xpath('.//td[6][contains(@class, "collection_bggrating")]').text
                print(num_of_rating)
            except:
                continue


            game_rating_dict['rank'] = rank
            game_rating_dict['title'] = title
            game_rating_dict['geek_rating'] = geek_rating
            game_rating_dict['avg_rating'] = avg_rating
            game_rating_dict['num_of_rating'] = num_of_rating
            writer.writerow(game_rating_dict.values())
 
        
        first_next_page = driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[1]/div/div/p/a[5]')
        first_next_page.click()

    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break