from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import openai

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(options=chrome_options2)
driver.get('https://web.whatsapp.com')

#######API DO EDITACODIGO##########################################

agent = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 '
                  'Safari/537.36'}
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/gyGAjVhzbR9CYbdXcKY1mFdeDvW2CHfj", headers=agent)
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
        #        ######PEGAR A MENSAGEM E CLICAR NELA######
        notif = driver.find_element(By.CLASS_NAME, elem_notif)
        notif = driver.find_elements(By.CLASS_NAME, elem_notif)
        click_notif = notif[-1]
        act_notif = webdriver.common.action_chains.ActionChains(driver)
        act_notif.move_to_element_with_offset(click_notif, 0, -20)
        act_notif.click()
        act_notif.perform()

        ################LER A NOVA MENSAGEM _21Ahp
        todas_as_msg = driver.find_elements(By.CLASS_NAME, msg_client)
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)
        time.sleep(5)

        ################PROCESSA A MENSAGEM NA API ia

        openai.api_key = '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'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=msg,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        resposta = response['choices'][0]['text']
        print(resposta)
        time.sleep(3)

        # RESPONDE A MSG
        campo_de_texto = driver.find_element(By.XPATH,box_msg)
        campo_de_texto.click()
        time.sleep(3)
        campo_de_texto.send_keys(resposta, Keys.ENTER)
        time.sleep(2)

        # FECHA O CONTATO






    except:
        print('buscando novas notificações')


while True:
    bot()
