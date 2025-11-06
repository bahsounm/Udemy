from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_optons = webdriver.ChromeOptions()
chrome_optons.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_optons)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# this can also be achived by using find_elements and taking hte secodn one, or by doing x path i was just trying to be exact lol
number_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-of-type(2) a:nth-of-type(1)")

print(number_of_articles.text)



