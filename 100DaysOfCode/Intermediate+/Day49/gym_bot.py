from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class GymBot:
    def __init__(self, email, password, url):
        self.email = email
        self.password = password
        self.url = url
        self.driver = self._setup_driver()

    def _setup_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(2)
        return driver

    def login(self):
        driver = self.driver
        driver.get(self.url)

        # Click login button
        driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        # Enter credentials
        driver.find_element(By.CSS_SELECTOR, '#email-input').send_keys(self.email)
        driver.find_element(By.CSS_SELECTOR, '#password-input').send_keys(self.password)

        # Submit
        driver.find_element(By.CSS_SELECTOR, '#submit-button').click()

        # Wait for dashboard to load
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Schedule_scheduleTitle__zfZxg"))
            )
            print("✅ Logged in successfully!")
        except:
            print("❌ Login failed or class schedule not found.")
            driver.quit()