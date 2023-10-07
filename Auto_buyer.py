# Best buy autonomous purchaser test
# Nicholas Whitman
# 14 April 2021

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time 

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 600)
count = 0

#confirmation = False

#while confirmation != True:
#do i loop this whole thing or do I refresh at add to cart

#driver.get("https://www.bestbuy.com/site/skullcandy-sesh-evo-true-wireless-in-ear-headphones-true-black/6412863.p?skuId=6412863")
driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")
end = False
while end == False:
	try:
		btn = driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block.btn-leading-ficon.add-to-cart-button")
		btn.click()

		explicitWait = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-secondary.btn-sm.btn-block")))
		btn = driver.find_element_by_class_name("btn.btn-secondary.btn-sm.btn-block")
		btn.click()

		btn = driver.find_element_by_class_name("btn.btn-lg.btn-block.btn-primary").click()
		explicitWait = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-secondary.btn-lg.cia-guest-content__continue.guest")))
		btn = driver.find_element_by_class_name("btn.btn-secondary.btn-lg.cia-guest-content__continue.guest").click()

#if class "ispu-card__switch" is avaiable then click
		explicitWait = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ispu-card__switch")))
		try:
	#	if bool(driver.find_element_by_class_name("ispu-curbside-new__option__content")) == True:
			driver.find_element_by_class_name("ispu-curbside-new__option__content") 
			driver.find_element_by_class_name("ispu-card__switch").click()
			explicitWait = wait.until(EC.visibility_of_element_located((By.ID, "consolidatedAddresses.ui_address_5.firstName")))
			firstName = driver.find_element_by_id("consolidatedAddresses.ui_address_5.firstName").send_keys("firstname")
			lastName = driver.find_element_by_id("consolidatedAddresses.ui_address_5.lastName").send_keys("lastname")
			address = driver.find_element_by_id("consolidatedAddresses.ui_address_5.street").send_keys("address")
			city = driver.find_element_by_id("consolidatedAddresses.ui_address_5.city").send_keys("city")
			state = driver.find_element_by_id("consolidatedAddresses.ui_address_5.state").send_keys("state")
			zipcode = driver.find_element_by_id("consolidatedAddresses.ui_address_5.zipcode").send_keys("zip")
			email = driver.find_element_by_id("user.emailAddress").send_keys("email")
			phone = driver.find_element_by_id("user.phone").send_keys("phone number")
			checkbox = driver.find_element_by_id("text-updates").click()
			btn = driver.find_element_by_class_name("button--continue").click()
			explicitWait = wait.until(EC.visibility_of_element_located((By.ID, "optimized-cc-card-number")))
			debitCard = driver.find_element_by_id("optimized-cc-card-number").send_keys("card number")
#code for dropdown box 
			explicitWait = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "c-dropdown.v-medium.c-dropdown.v-medium.smart-select")))
			expirationMonth = driver.find_element_by_class_name("c-dropdown.v-medium.c-dropdown.v-medium.smart-select") #month02
			selectObject = Select(expirationMonth)
			selectObject.select_by_value('02')
			expirationYear = driver.find_element_by_name("expiration-year")#year
			selectObject = Select(expirationYear)
			selectObject.select_by_value('2022')
			cvv = driver.find_element_by_id("credit-card-cvv").send_keys("111")#cvv
			btn = driver.find_element_by_class_name("btn.btn-lg.btn-block.btn-primary").click()
			end = True
		except NoSuchElementException:
#enter billing information if shipping was selected first
			explicitWait = wait.until(EC.visibility_of_element_located((By.ID, "consolidatedAddresses.ui_address_2.firstName")))
			firstName = driver.find_element_by_id("consolidatedAddresses.ui_address_2.firstName").send_keys("Bob")
			lastName = driver.find_element_by_id("consolidatedAddresses.ui_address_2.lastName").send_keys("Smith")
			address = driver.find_element_by_id("consolidatedAddresses.ui_address_2.street").send_keys("anonymous")
			city = driver.find_element_by_id("consolidatedAddresses.ui_address_2.city").send_keys("anonymous")
			state = driver.find_element_by_id("consolidatedAddresses.ui_address_2.state").send_keys("anonymous")
			zipcode = driver.find_element_by_id("consolidatedAddresses.ui_address_2.zipcode").send_keys("anonymous")
			email = driver.find_element_by_id("user.emailAddress").send_keys("anonymous")
			phone = driver.find_element_by_id("user.phone").send_keys("anonymous")
			checkbox = driver.find_element_by_id("text-updates").click()
			btn = driver.find_element_by_class_name("button--continue").click()
			explicitWait = wait.until(EC.visibility_of_element_located((By.ID, "optimized-cc-card-number")))
#inserts information for credit card
			debitCard = driver.find_element_by_id("optimized-cc-card-number").send_keys("anonymous")
#code for dropdown box 
			expirationMonth = driver.find_element_by_class_name("c-dropdown.v-medium.c-dropdown.v-medium.smart-select") #month
			selectObject = Select(expirationMonth)
			selectObject.select_by_value('02')
			expirationYear = driver.find_element_by_name("expiration-year")#year
			selectObject = Select(expirationYear)
			selectObject.select_by_value('2022')
			cvv = driver.find_element_by_id("credit-card-cvv").send_keys("anonymous")#cvv
			btn = driver.find_element_by_class_name("btn.btn-lg.btn-block.btn-primary").click()
			end = True
	except NoSuchElementException:
		driver.refresh()
		count += 1
		print("refresh", count)
		
		end = False

#confirmation = EC.url_contains("https://www.bestbuy.com/checkout/r/thank-you")

#end program syntax
