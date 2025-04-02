from selenium import webdriver
from selenium.webdriver.common.by import By

items_dict = {}

#Keep website open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

items = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")
counter = 0
for item in items:
    element_dict = {}
    time_element = item.find_element(By.CSS_SELECTOR, value="time")
    element_dict["time"] = time_element.text
    anchor_element = item.find_element(By.CSS_SELECTOR, value="a")
    element_dict["name"] = anchor_element.text
    items_dict[counter] = element_dict
    counter += 1
print(items_dict)

driver.quit()