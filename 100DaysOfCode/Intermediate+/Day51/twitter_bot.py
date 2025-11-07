from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TwitterBot():
    def __init__(self, down, up):
        self.driver = self.set_up_driver()
        self.down = down 
        self.up = up
        self.speed_test_url = 'https://www.speedtest.net'
        self.twitter_url = 'https://www.x.com'


    def set_up_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def get_internet_speed(self):
        driver = self.driver
        driver.get(self.speed_test_url)
        
        # press go to start internet speed test
        go_button = driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()

        # wait for the speed test to finish before we look for the speeds
        time.sleep(40)
        up_speed = driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed")
        down_speed = driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed")

        # only care about sending a tweet if the speeds are not as promised
        speeds = {}
        if float(up_speed.text) < self.up:
            speeds["up"] = (up_speed.text)
        if float(down_speed.text) < self.down:
            speeds["down"] = (down_speed.text)
        return speeds


    def tweet_at_provider(self, found_speeds, email, password):
        driver = self.driver
        self.twitter_login(email, password)
        print("made it back")


    def twitter_login(self, email, password):
        driver = self.driver
        driver.get(self.twitter_url)

        sign_in_button = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a') # doing the classes by parts too long to do whole thing
        sign_in_button.click()

        driver.implicitly_wait(3)
        email_entry = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_entry.send_keys(email)
        
        # driver.implicitly_wait(3)
        # next_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        # next_button.click()

        # pswrd_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        # pswrd_button.send_keys(password)
        
        # login_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        # login_button.click()







