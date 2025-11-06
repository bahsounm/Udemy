from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_optons = webdriver.ChromeOptions()
chrome_optons.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_optons)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# this can also be achived by using find_elements and taking hte secodn one, or by doing x path i was just trying to be exact lol
number_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-of-type(2) a:nth-of-type(1)")

print(number_of_articles.text)

# this is how we can click
# number_of_articles.click()

# lets say there is a linkwe want to lcik we can just pass the link text and then clcik it
# sieges_of_berwick = driver.find_element(By.LINK_TEXT, value="sieges of Berwick")
# sieges_of_berwick.click()

# we can also find "Search" bar inputs, and send what we want to search
search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search.send_keys("Prophet Muhammad", Keys.ENTER)
# now in order to search or click enter we do the following see keys import above, and key word in search in line above 

# driver.quit()