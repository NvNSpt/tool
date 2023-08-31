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



maxclaim = 1
day_claim = 1

#tạo người dugnf chrome
options = Options()
options.debugger_address="127.0.0.1:2222"
driver = webdriver.Chrome(options=options)

driver.get('https://cointool.app/batchMint/xen')

metamask_window = WebDriverWait(driver, 60).until(ec.number_of_windows_to_be(2))
time.sleep(1)
# Switch sang cửa sổ MetaMask
driver.switch_to.window(driver.window_handles[metamask_window])
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
wait = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.ID, "password")))
driver.find_element("xpath",'//*[@id="password"]').send_keys("123123123")
driver.find_element("xpath",'//*[@id="app-content"]/div/div[2]/div/div/button').click()
time.sleep(1)

#chuyen ve cointoool
driver.switch_to.window(driver.window_handles[0])

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

#bật other
wait2 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core').click()

#chỉnh maxclaim
maxclaim_element = driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(4) > div > div > div > div > input')
WebDriverWait(driver, 10).until(ec.visibility_of(maxclaim_element))
maxclaim_element.clear()
maxclaim_element.send_keys(maxclaim)
