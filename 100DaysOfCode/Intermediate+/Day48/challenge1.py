from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")

events = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last li")

upcoming_events = {}

for i in range(0,len(events)):
    event = events[i].text.split("\n")
    upcoming_events[i] = {"time":event[0] , 'name':event[1]}

print(upcoming_events)

driver.quit()