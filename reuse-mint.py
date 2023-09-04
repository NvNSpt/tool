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



#tạo người dugnf chrome
options = Options()
options.add_argument('--user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 30')
options.debugger_address="127.0.0.1:2222"
driver = webdriver.Chrome(options=options)


file_count = open('count.txt', mode = 'r')

count = int(file_count.read())

file_count.close()


for i in range(1,1000):

	if i == 1:
		driver.switch_to.window(driver.window_handles[0])
		driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
	else:
		pass


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

	
	#ấn remint
	wait2 = WebDriverWait(driver, 1000).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')))
	driver.find_element(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary').click()
	time.sleep(1)


	driver.switch_to.window(driver.window_handles[0])
	#chuyển sang activity
	wait2 = WebDriverWait(driver, 60).until(ec.visibility_of_element_located(("xpath",'//*[@id="app-content"]/div/div[3]/div/div/div[1]/div[2]/div/ul/li[3]/button')))
	driver.find_element("xpath",'//*[@id="app-content"]/div/div[3]/div/div/div[1]/div[2]/div/ul/li[3]/button').click()
	time.sleep(1)


	#ấn contrackt
	wait2 = WebDriverWait(driver, 1000).until(ec.visibility_of_element_located((By.CLASS_NAME,'mm-box.transaction-list__pending-transactions')))
	driver.find_element(By.CLASS_NAME,'mm-box.transaction-list__pending-transactions').click()
	time.sleep(2)

	wait2 = WebDriverWait(driver, 20).until(ec.element_to_be_clickable(("xpath",'//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]')))
	driver.find_element("xpath",'//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]').click() #confirm
	count = count + 1
	time.sleep(3)
	try:
		wait2 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME,'mm-box.transaction-list__pending-transactions')))
		print('chờ xác nhận lệnh')
	except:
		pass

	wait2 = WebDriverWait(driver, 1000).until(ec.invisibility_of_element_located((By.CLASS_NAME,'mm-box.transaction-list__pending-transactions')))
	print('hoàn thành lệnh')
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
