from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_optons = webdriver.ChromeOptions()
chrome_optons.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_optons)
driver.get('https://ozh.github.io/cookieclicker')
# need to give a delay to allow for the language options to appear
time.sleep(1)

english_language = driver.find_element(By.CLASS_NAME, "langSelectButton.title")
english_language.click()

# needed to reloacte due to stale element, so wait 1 sec before looking for the big cookie 
time.sleep(1)
cookie_to_click = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")

start_time = time.time()
check_timer = start_time 

grandma_count = 0
farm_count = 0

while True:
    cookie_to_click.click()
    # the extra cursor appear to have class name 'product locked disabled', then after getting enough cookies the class name is 'product unlocked enabled'
    # it also has an id of 'productName0'
    # grandma appears to have class name 'product locked disabled', then after getting enough cookies the class name is 'product unlocked enabled'
    # it also has an id of 'productName1'
    if time.time() - check_timer >= 5:
        try:
            store_options = driver.find_elements(By.CLASS_NAME, value='product.unlocked.enabled')
            if len(store_options) > 1:
                if grandma_count < 20:
                    store_options[1].click()
                    grandma_count+=1
                elif farm_count < 10:
                    store_options[2].click()
                    farm_count += 1
            check_timer = time.time()
        except:
            continue
    
    if time.time() - start_time >= 300:
        break









