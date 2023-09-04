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



maxclaim = int(input('nhập ví trên 1 Lần claim: '))
day_claim = int(input('nhập số ngày claim: '))

#tạo người dugnf chrome
options = Options()
options.add_argument('--user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 2')
options.debugger_address="127.0.0.1:2222"
driver = webdriver.Chrome(options=options)



#login metamask khi moi mo len
driver.switch_to.window(driver.window_handles[0])
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
wait = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "password")))
driver.find_element("xpath",'//*[@id="password"]').send_keys("123123123")
driver.find_element("xpath",'//*[@id="app-content"]/div/div[2]/div/div/button').click()
time.sleep(1)

#driver.switch_to.new_window()
driver.switch_to.window(driver.window_handles[1])
driver.get('https://cointool.app/batchMint/xen')

#bật other
wait2 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core').click()

#chỉnh dayclaim
wait2 = WebDriverWait(driver, 1000).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.resultBox > div.formBox > div:nth-child(3) > div:nth-child(2) > button')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.resultBox > div.formBox > div:nth-child(3) > div:nth-child(2) > button').click()
time.sleep(1)
	
dayclaim_element = driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > form > div > div > div > div > input')
WebDriverWait(driver, 60).until(ec.visibility_of(dayclaim_element))
dayclaim_element.clear()
dayclaim_element.send_keys(day_claim)
time.sleep(1)
wait2 = WebDriverWait(driver, 1000).until(ec.presence_of_element_located((By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__header > button')))
driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__header > button').click()
time.sleep(1)


#chỉnh maxclaim
maxclaim_element = driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(4) > div > div > div > div > input')
WebDriverWait(driver, 10).until(ec.visibility_of(maxclaim_element))
maxclaim_element.clear()
maxclaim_element.send_keys(maxclaim)


input(' chờ load ví + chinh dclaim, enter để tiếp tục')


for i in range(1,1000):
	print(i)
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(4)

	if i % 5 == 0:
		
		actions = ActionChains(driver) 
		actions.send_keys(Keys.ESCAPE) # XOÁ maxclaim number
		actions.perform()
		time.sleep(1)

	else: 
		pass

	#ấn claim
	wait2 = WebDriverWait(driver, 1000).until(ec.presence_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.resultBox > div.formBox > div:nth-child(3) > div:nth-child(2) > button')))
	driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.resultBox > div.formBox > div:nth-child(3) > div:nth-child(2) > button').click()
	time.sleep(2)
	
	#ấn confirm
	wait2 = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.dialog-footer > button.el-button.el-button--success.el-button--medium')))
	driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div.dialog-footer > button.el-button.el-button--success.el-button--medium').click()

	
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
	time.sleep(3)
	wait2 = WebDriverWait(driver, 1000).until(ec.visibility_of_element_located((By.CLASS_NAME,'mm-box.transaction-list__pending-transactions')))
	print('chờ xác nhận lệnh')
	time.sleep(1)
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

input('done')

