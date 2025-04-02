from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#Keep website open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

#By.LINK_TEXT finds elements by the text in th anchor tag. .click method clicks the link.
#all_portals = driver.find_element(By.LINK_TEXT, value="Content Portals")
#all_portals.click()

#send_keys types in the input places.
f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("a")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("b")

email = driver.find_element(By.NAME, value="email")
email.send_keys("a@b")

button = driver.find_element(By.CSS_SELECTOR, value="button")
button.click()


#price = driver.find_element(By.CLASS_NAME, value="price-item.price-item--sale.price-item--last")
#print(price.text)
#We can also find elements with ID, name, css selectors, and XPATH.
#driver.find_element(By.XPATH, '/html/body/div/div[1]/div/main/div/p[3]')

driver.quit()