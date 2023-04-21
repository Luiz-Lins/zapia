from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(chrome_options=chrome_options2)
driver.get('https://web.whatsapp.com')


#######API DO EDITACODIGO##########################################

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/gyGAjVhzbR9CYbdXcKY1mFdeDvW2CHfj",  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
elem_notif = api[3].strip()
contact_client = api[4].strip()
box_msg = api[5].strip()
msg_client = api[6].strip()

##########################################
time.sleep(10)


def bot():
    try:
        notif = driver.find_element(By.CLASS_NAME, elem_notif)
        notif = driver.find_elements(By.CLASS_NAME, elem_notif)
        click_notif = notif[-1]
        act_notif = webdriver.common.action_chains.ActionChains(driver)
        act_notif.move_to_element_with_offset(click_notif, 0, -20)
        act_notif.click()
        act_notif.perform()





    except:
        print('buscando novas notificações')

while True:
    bot()
