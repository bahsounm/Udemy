import scrapy
import os
from dotenv import load_dotenv
load_dotenv()
import smtplib

TARGET_PRICE = 150
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASS = os.environ.get("MY_PASS")

class AmazonPriceTracker(scrapy.Spider):
    name = "amazon"
    start_urls = ['https://www.amazon.ca/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1']
    
    def parse(self, response):
        price_text = response.css('span.aok-offscreen::text').get()
        if not price_text:
            self.logger.error("Price element not found!")
            return

        price = float(price_text.replace("$", "").strip())
        print("THIS IS THE PRICE {}".format(price))
        yield {"price": price} # not needed in our case as we dont need to store or use it elsewhere

        if price < TARGET_PRICE:
            self.send_email(price)

    def send_email(self, price):
        subject = "Price Drop Alert!"
        body = f"The Instant Pot cooker dropped to ${price:.2f} — below your target price of ${TARGET_PRICE:.2f}."
        msg = f"Subject:{subject}\n\n{body}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=msg.encode('utf-8')
                )
            self.logger.info("Email sent successfully.")
        except Exception as e:
            self.logger.error(f"Error sending email: {e}")