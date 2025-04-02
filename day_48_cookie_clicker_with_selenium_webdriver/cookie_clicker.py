from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Keep website open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


timeout = time.time() + 5
while True:
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()
    if time.time() > timeout:
        timeout = time.time() + 5
        #Every 5 seconds, buy the most expensive upgrade.
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
        prices = prices[:-1]
        money = driver.find_element(By.ID, value="money")
        possible_purchases = []
        for price in prices:
            a = price.text.strip().split("-")[1]
            a = a.replace(",", "")
            if int(money.text) > int(a):
                possible_purchases.append(price)
        possible_purchases[-1].click()




