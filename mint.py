import subprocess
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





# Tạo thông báo nhập dữ liệu theo network
check_network = "Nhập số để chọn mạng: "
network = open('network.txt', mode='r')
all_file = network.readlines()
line_number = 0

for line in all_file:
    tach_hang = line.strip().split(',')
    path = tach_hang[0]
    input_string = f"{line_number}({path}), "
    check_network += input_string
    line_number += 1

network.close()

print(check_network)


#tạo ô dể nhập network
while True:
    try:
        ob = int(input("Nhập mạng: "))
        network = open('network.txt', mode='r')
        all_file = network.readlines()

        if 0 <= ob < len(all_file):
            line = all_file[ob]
            tach_hang = line.strip().split(',')
            path, mint, claim = tach_hang[0], tach_hang[1], tach_hang[2]
            print("Path:", path)
            print("Mint:", mint)
            print("Claim:", claim)
            break
        else:
            print("Nhập mạng không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
        print("Nhập mạng không hợp lệ. Vui lòng nhập lại.")
network.close()


if ob < 10:
	ob = "0" + str(ob)
	print(ob)
else:
	ob = str(ob)
	print(ob)

#tạo người dugnf chrome
options = Options()
options.debugger_address=fr"127.0.0.1:92{ob}"
driver = webdriver.Chrome(options=options)



acc_now = int(input('nhập số Lần cần mint: '))


for i in range(1,1000):

	if i == 1:
		driver.switch_to.window(driver.window_handles[0])
		driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
	else:
		pass


	print(i)
	if i > acc_now:
		i = 1
		hoi = input('đã xong 68 lần, có muốn tiếp tục không?')
	else: 
		print('nhỏ hơn 35')

	driver.switch_to.window(driver.window_handles[1])

	if i % 4 == 0:
		
		actions = ActionChains(driver) 
		actions.send_keys(Keys.ESCAPE) # XOÁ maxclaim number
		actions.perform()
		time.sleep(1)

	else: 
		pass

	time.sleep(2)
	#ấn mint
	wait2 = WebDriverWait(driver, 1000).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#app-main > div > div.card > div:nth-child(5) > button')))
	driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div:nth-child(5) > button').click()
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

	time.sleep(3)
	try:
		wait2 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME,'mm-box.transaction-list__pending-transactions')))
		print('chờ xác nhận lệnh')
	except:
		pass

	wait2 = WebDriverWait(driver, 100000).until(ec.invisibility_of_element_located((By.CLASS_NAME,'mm-box.transaction-list__pending-transactions')))
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