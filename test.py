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



day_claim = 1


#tạo người dugnf chrome
options = Options()
options.debugger_address="localhost:2222"
driver = webdriver.Chrome(options=options)


driver.get('https://cointool.app/batchMint/xen')

#bật other
wait2 = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core')))
driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(1) > div:nth-child(2) > div > div > div > div > span.el-switch__core').click()


#chỉnh maxclaim
maxclaim_element = driver.find_element(By.CSS_SELECTOR,'#app-main > div > div.card > div.panal > form > div:nth-child(2) > div:nth-child(4) > div > div > div > div > input')

WebDriverWait(driver, 10).until(ec.visibility_of(input_element))

maxclaim_elemen.clear()

maxclaim_elemen.send_keys(day_claim)


input('tam dừng')