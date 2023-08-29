from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random


acc_now = int(input('nhập số Lần cần mint: '))
daymint = int(input('nhập số Ngày cần mint: '))
mint_number = int(input('nhập số ví trên 1 lần mint: '))


#tạo người dugnf chrome
options = Options()
options.add_argument('--user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 30')
options.debugger_address="127.0.0.1:3000"
driver = webdriver.Chrome(options=options)



#login metamask khi moi mo len
driver.switch_to.window(driver.window_handles[0])
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
wait = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "password")))
driver.find_element("xpath",'//*[@id="password"]').send_keys("123123123")
driver.find_element("xpath",'//*[@id="app-content"]/div/div[2]/div/div/button').click()
time.sleep(2)

#driver.switch_to.new_window()
driver.switch_to.window(driver.window_handles[1])
driver.get('https://cointool.app/batchMint/xen')


#bật other
wait2 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core').click()

time.sleep(1)
actions = ActionChains(driver) 
actions.send_keys(Keys.TAB * 1 + Keys.BACKSPACE) # XOÁ MINT
time.sleep(1)
actions.send_keys(Keys.TAB * 1 + Keys.BACKSPACE) # XOÁ dmint
time.sleep(1)
actions.send_keys(Keys.TAB * 2 + Keys.BACKSPACE) # XOÁ MAXMINT
actions.perform()
time.sleep(1)


#chỉnh maxmint
wait2 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(3) > div > div > div > div > input')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(3) > div > div > div > div > input').send_keys("999")
time.sleep(1)
#chỉnh mint
wait2 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(1) > div > div > div > div > input')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(1) > div > div > div > div > input').send_keys(mint_number)
time.sleep(1)
#chỉnh dmint
wait2 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(2) > div > div > div > div > input')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(2) > div > div > div > div > input').send_keys(daymint)
input(' chờ load ví, enter để tiếp tục')


file_count = open('count.txt', mode = 'r')

count = int(file_count.read())

file_count.close()


for i in range(1,1000):
	print(count)
	if count > acc_now:
		count = 1
		file_count = open('count.txt', mode = 'w')
		file_count.write(str(count))
		file_count.close()
		hoi = input('đã xong 68 lần, có muốn tiếp tục không?')
	else: 
		print('nhỏ hơn 35')

	driver.switch_to.window(driver.window_handles[1])

	if i % 5 == 0:
		
		actions = ActionChains(driver) 
		actions.send_keys(Keys.ESCAPE) # XOÁ maxclaim number
		actions.perform()
		time.sleep(1)

	else: 
		pass

	#ấn mint
	wait2 = WebDriverWait(driver, 1000).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#app-main > div > div.card > div:nth-child(5) > button')))
	driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div:nth-child(5) > button').click()
	time.sleep(1)


	driver.switch_to.window(driver.window_handles[0])
	time.sleep(1)
	#chuyển sang activity
	wait2 = WebDriverWait(driver, 60).until(ec.presence_of_element_located(("xpath",'//*[@id="app-content"]/div/div[3]/div/div/div/div[2]/div/ul/li[3]/button')))
	driver.find_element("xpath",'//*[@id="app-content"]/div/div[3]/div/div/div/div[2]/div/ul/li[3]/button').click()

	time.sleep(1)

	#ấn contrackt
	wait2 = WebDriverWait(driver, 1000).until(ec.visibility_of_element_located((By.CLASS_NAME,'transaction-list__pending-transactions')))
	driver.find_element(By.CLASS_NAME,'list-item.transaction-list-item.transaction-list-item--unconfirmed').click()

	time.sleep(3)

	wait2 = WebDriverWait(driver, 20).until(ec.presence_of_element_located(("xpath",'//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]')))
	driver.find_element("xpath",'//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]').click() #confirm
	count = count + 1

	wait2 = WebDriverWait(driver, 1000).until(ec.invisibility_of_element_located(("xpath",'//*[@id="app-content"]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[4]/div/button[1]')))
	time.sleep(1)
	


	if i % 10 == 0:
		driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/advanced')
		time.sleep(1)
		wait2 = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(("xpath",'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button')))
		driver.find_element("xpath",'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button').click() #clear active
		time.sleep(1)
		wait2 = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(("xpath",'//*[@id="app-content"]/div/span/div[1]/div/div/div[2]/button[2]')))
		driver.find_element("xpath",'//*[@id="app-content"]/div/span/div[1]/div/div/div[2]/button[2]').click() #clear
		time.sleep(3)	
		wait2 = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(("xpath",'//*[@id="app-content"]/div/div[3]/div/div[1]/div/button')))
		driver.find_element("xpath",'//*[@id="app-content"]/div/div[3]/div/div[1]/div/button').click() #x

	else: 
		pass

	 

	file_count = open('count.txt', mode = 'w')
	file_count.write(str(count))
	file_count.close()
	
input('done')

