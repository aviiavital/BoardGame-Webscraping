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
driver.get("https://boardgamegeek.com/browse/boardgame/page/167?sort=rank")

csv_file = open('bdgeekurls.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)


index = 1
while index < 25:
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

            # find the url of each game that I want to study            
            try: 
                url = rating.find_element_by_xpath('.//div[contains(@id, "results_objectname")]//a').get_attribute('href')
                print(url)
            except:
                continue

            game_rating_dict['url'] = url
            writer.writerow(game_rating_dict.values())
 
        
        first_next_page = driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[1]/div/div/p/a[5]')
        first_next_page.click()

    except Exception as e:
        print(e)
        csv_file.close()
        driver.close()
        break











# driver.find_element_by_xpath('//div/table[@class="collection_table"]')

# # scrape the row for  Rank, Title, Geek Rating, Avg Rating, Num of Voters for games on the page

# driver.find_element_by_xpath('.//td[@class="collection_rank"]').text()

# # Clicks that url game on the page to enter the row site
# driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[2]/td[2]/a/img').click()

# # # Collect Weight,Num of players, type of game from that page

# # # backs out of the page on to the list again
# # driver.find_element_by_xpath('//*[@id="mainbody"]/div/div[1]/div[1]/div[2]/ng-include/div/ng-include/div/div/div[2]/div[1]/flags-module/div/div/div/ul[1]/li/span[2]/a').click()

# # # click on the next page on the list
# # # need to find the new xpath for the current next game
# # # table/tbody/tr[this number goes up by 1 every time]



# # until the final game on the list
# # driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[1]/div/div/div[2]/div[3]/table/tbody/tr[101]/td[2]/a/img').click()



# # Click next button to go to the next page after 100 games are looked at
# # this one may work but doesnt usually
# # driver.find_element_by_xpath('//*[@id="maincontent"]/form/div/div[1]/a[5]').click()   

# driver.find_element_by_xpath('//*[@id="maincontent"]/p/a[7]/b').click()

# Have this repeat for like 

# # print all those elements to a csv






# reviews = driver.find_elements_by_xpath('//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')

# while True:
#   for review in reviews
#       try:
#           title = review.find_element_by_xpath('//div[@class="NHaasDS75Bd fontSize_12 wrapText"]').text
#           print(title)
#       except:
#           continue


# # Page index used to keep track of where we are.
# index = 1
# # We want to start the first two pages.
# # If everything works, we will change it to while True
# while index <=2:
#   try:
#       print("Scraping Page number " + str(index))
#       index = index + 1
#       # Find all the reviews. The find_elements function will return a list of selenium select elements.
#       # Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
#       reviews = driver.find_elements_by_xpath('//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')
#       # Iterate through the list and find the details of each review.
#       for review in reviews:
#           # Initialize an empty dictionary for each review
#           review_dict = {}
#           # Use try and except to skip the review elements that are empty. 
#           # Use relative xpath to locate the title.
#           # Once you locate the element, you can use 'element.text' to return its string.
#           # To get the attribute instead of the text of each element, use 'element.get_attribute()'
#           try:
#               title = review.find_element_by_xpath('.//div[@class="NHaasDS75Bd fontSize_12 wrapText"]').text
#           except:
#               continue

#           print('Title = {}'.format(title))

#           # OPTIONAL: How can we deal with the "read more" button?
            
#           # Use relative xpath to locate text, username, date_published, rating.
#           # Your code here

#           # Uncomment the following lines once you verified the xpath of different fields
            
#           # review_dict['title'] = title
#           # review_dict['text'] = text
#           # review_dict['username'] = username
#           # review_dict['date_published'] = date_published
#           # review_dict['rating'] = rating

#       # We need to scroll to the bottom of the page because the button is not in the current view yet.
#       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#       # Locate the next button element on the page and then call `button.click()` to click it.
#       button = driver.find_element_by_xpath('//li[@class="nextClick displayInlineBlock padLeft5 "]')
#       button.click()
#       time.sleep(2)

    # except Exception as e:
    #     print(e)
    #     driver.close()
    #     break
