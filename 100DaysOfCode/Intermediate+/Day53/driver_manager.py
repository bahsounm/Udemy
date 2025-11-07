from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DriverManager:
    def __init__(self):
        self.driver = self.set_up_driver()
        self.form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdKuIDUJRtz6udrL8NNaiaL0PQX3LSEJu4MlNB8t6e-02wF_g/viewform?usp=header'
        self.zillow_url = 'https://appbrewery.github.io/Zillow-Clone'


    def set_up_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    
    def get_properties(self):
        driver = self.driver
        driver.get(self.zillow_url)

        responses = []

        properties = driver.find_elements(By.CLASS_NAME, value='ListItem-c11n-8-84-3-StyledListCardWrapper')

        for property_obj in properties:
            property = {}
            property['Address'] = property_obj.find_element(By.CSS_SELECTOR, value='address').text
            property['Price'] = property_obj.find_element(By.CLASS_NAME, value='PropertyCardWrapper__StyledPriceLine').text
            property['Link'] = property_obj.find_element(By.CSS_SELECTOR, value='a').get_attribute("href")
            
            responses.append(property)
        
        return responses



    def fill_form(self, responses = []):
        driver = self.driver
        driver.get(self.form_url)
        time.sleep(1)

        for response in responses:

            # get the entries since they all have the same class name
            entries = driver.find_elements(By.CLASS_NAME, value='whsOnd.zHQkBf')
            
            # Address entry
            address_entry = entries[0]
            address_entry.send_keys(response['Address'])
            # Price entry
            price_entry = entries[1]
            price_entry.send_keys(response['Price'])
            # Link entry
            link_entry = entries[2]
            link_entry.send_keys(response['Link'])

            # submit the response 
            submit_button = driver.find_element(By.CLASS_NAME, value='l4V7wb.Fxmcue')
            submit_button.click()

            # Submit Another response
            submit_another = driver.find_element(By.CSS_SELECTOR, value='.c2gzEf a')
            submit_another.click()

        driver.quit()

