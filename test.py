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


day_claim = 5

#tạo người dugnf chrome
options = Options()
options.debugger_address="localhost:2222"
driver = webdriver.Chrome(options=options)


driver.get('https://cointool.app/batchMint/xen')

wait = WebDriverWait(driver, 60)
metamask_window = wait.until(ec.number_of_windows_to_be(2))

time.sleep(1)

# Switch sang cửa sổ MetaMask
driver.switch_to.window(driver.window_handles[metamask_window])


driver.get('https://cointool.app/batchMint/xen')

wait = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "password")))
driver.find_element(By.ID, "password").send_keys("123123123")
#driver.find_element("xpath",'//*[@id="app-content"]/div/div[2]/div/div/button').click()
time.sleep(1)



input('tam dừng')