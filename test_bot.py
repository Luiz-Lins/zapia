from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import openai
from dotenv import load_dotenv




# Configurações do Chrome

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(chrome_options=chrome_options2)
driver.get('https://web.whatsapp.com')

# API do Editacodigo

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/59.0.3071.115 Safari/537.36'}
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/gyGAjVhzbR9CYbdXcKY1mFdeDvW2CHfj",  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()

##########################################
time.sleep(10)
##########################################


def bot():
    try:
        # Clica na última notificação recebida
        bolinha = driver.find_element(By.CLASS_NAME, bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME, bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()



        # Obtém a mensagem do cliente
        todas_as_msg = driver.find_elements(By.CLASS_NAME, msg_cliente)
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)

        # Processa a mensagem na API da OpenAI

        cliente = 'mensagem do cliente:'
        texto2 = 'Responda a mensagem do cliente com base no proximo texto.'
        texto = 'explique tudo sobre hotel Copacabana Palace Endereço: Av. Atlântica, 1111 - ' \
                'Copacabana, Rio de Janeiro -RJ, 22021-111 Telefone: (21) 2548-1111, resevas por email ' \
                ' reserva@email.com, aceitamos todas as formas de pagamentos'
        questao = cliente + msg + texto2 + texto

        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_ACCESS_KEY_ID')

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=questao,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        resposta = response['choices'][0]['text']
        print(resposta)
        time.sleep(2)

        # Responde a mensagem
        campo_de_texto = driver.find_element(By.XPATH, caixa_msg)
        campo_de_texto.click()
        time.sleep(3)
        campo_de_texto.send_keys(resposta,Keys.ENTER)
        time.sleep(2)

        # Fecha a janela de conversa
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except:
        print('buscando novas notificações')
        time.sleep(3)

# Executa o bot indefinidamente

while True:
    bot()
