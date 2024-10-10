from selenium import webdriver
import os
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.parse
from random import randrange
from difflib import SequenceMatcher
import random
import base64
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains

workbook = openpyxl.Workbook()
sheet = workbook.active
# Cấu hình đường dẫn hồ sơ Chrome
profile_directory = '/Users/nguyennhat/Desktop/taivideo/chrome_profiles' 
profile_name = 'linkedin_account_1'  
profile_path = os.path.join(profile_directory, profile_name)
if not os.path.exists(profile_path):
    raise Exception(f"Hồ sơ {profile_name} không tồn tại. Vui lòng kiểm tra đường dẫn.")

# Cấu hình Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={profile_path}")
# Thêm User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")


df1 = pd.read_excel('/Users/nguyennhat/Desktop/taivideo/fb_groupurls2xlsx.xlsx') 
FB_groupurls = df1.iloc[:, 0].tolist()
driver = webdriver.Chrome(options=chrome_options)

for FB_groupurl in FB_groupurls:

    driver.get(FB_groupurl)
    # Cuộn xuống ngẫu nhiên từ 10-15 lần
    scroll_times = randrange(10, 16)

    for _ in range(scroll_times):
        page_height = driver.execute_script("return document.body.scrollHeight")

        scroll_height = randrange(800, 1000)
        scroll_height2 = randrange(40, 200)

        # Cuộn xuống với chiều cao ngẫu nhiên
        driver.execute_script(f"window.scrollBy(0, {page_height});")
        sleep(randrange(2, 5))

        driver.execute_script(f"window.scrollBy(0, -{scroll_height2});")
        # Dừng lại trong một khoảng thời gian ngẫu nhiên
        sleep(randrange(2, 5))
        
        groupurls = driver.find_elements(By.CLASS_NAME,'x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1sur9pj.xkrqix3.xzsf02u.x1pd3egz')
        for groupurl in groupurls:
            link = groupurl.get_attribute('href')
            if link:
                sheet.append([link])
    workbook.save('links.xlsx')
