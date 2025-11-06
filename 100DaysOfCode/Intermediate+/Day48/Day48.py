from selenium import webdriver # webdriver is driving the chorme browisng and going ot do all of our automated tasks
from selenium.webdriver.common.by import By
#------------------------------------------------------------------------------------------------------------------
# these are for getting passed a continue
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#------------------------------------------------------------------------------------------------------------------

# youll notice when we open the cite that it will automatically close to solve this
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# the driver tewlls selenium how to work witht he diferent browasers
driver = webdriver.Chrome(options=chrome_options)

# this will automatically open the cite we want
driver.get("https://www.amazon.ca/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

#------------------------------------------------------------------------------------------------------------------
# this is for if there is a click to continue button that we need to get past
continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "a-button-text"))
    )
continue_button.click()
#------------------------------------------------------------------------------------------------------------------
# can searchh by name, class, id, 
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print("The Price is {}.{}".format(price_dollar.text, price_cents.text))

# we can get a hold of elemetns that dont have any class name or id, by using a CSS selector
# can do this by doing ".<class name of the parent> <the selector we want>"

# if all else fails we can use the xPath, html/body
print(driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]').text)

# to find all the elements do "find_elements"


# # will quit a tab
# driver.close()
# # will quit the whole thing
# driver.quit()