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

# Lấy đường dẫn tới tệp Python hiện tại (script đang thực thi)
current_script_path = os.path.abspath(__file__)
current_file_name = os.path.basename(current_script_path)
#đổi thành đường dẫn tới chrome đã tạo
chrome_path = current_script_path.replace(current_file_name, "chrome\\")
#khơi chạy chrome theo port
chrome_run = fr"{chrome_path}{path}\App\Chrome-bin\chrome.exe "
chrome_options = [
    "--user-data-dir=" + chrome_path + path +"\\Data\\profile",
    "--profile-directory=Default",
    "--remote-debugging-port=922" + str(ob)
]
cmd = [chrome_run] + chrome_options
subprocess.Popen(cmd)





day_claim = int(input('nhập số ngày claim: '))
maxclaim = claim

#tạo người dugnf chrome
options = Options()
options.debugger_address=fr"127.0.0.1:922{ob}"
driver = webdriver.Chrome(options=options)



driver.switch_to.window(driver.window_handles[0])
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
wait = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "password")))
driver.find_element(By.ID, "password").send_keys("123123123")
driver.find_element(By.CSS_SELECTOR, '#app-content > div > div:nth-child(2) > div > div > button').click()



time.sleep(10000)
