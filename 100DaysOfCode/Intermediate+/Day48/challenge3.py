from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com')

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("hassan")
lName = driver.find_element(By.NAME, value="lName")
lName.send_keys("bazun")
email = driver.find_element(By.NAME, value="email")
email.send_keys("abcd@gmail.com")

signUp = driver.find_element(By.CLASS_NAME, value='btn.btn-lg.btn-primary.btn-block')
signUp.click()

# driver.quit()