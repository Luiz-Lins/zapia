from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import openai
import PySimpleGUI as Sg


agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/59.0.3071.115 Safari/537.36'}
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/gyGAjVhzbR9CYbdXcKY1mFdeDvW2CHfj" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
token1 = api[0].strip()
token2 = api[1].strip()
token3 = api[2].strip()
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()


tela1 = [
    [Sg.Text('SENHA')],
    [Sg.Input(key='senha', password_char='*')],
    [Sg.Button('ENTRAR')],



]


tela2 = [
    [Sg.Text('BEM VINDO A SEGUNDA TELA')],




]

windows1 = Sg.Window('ZAPIA', layout=tela1)
windows2 = Sg.Window('ZAPIA', layout=tela2)


while True:
    event, values = windows1.read()
    if event == Sg.WIN_CLOSED:
        break
    if event == 'ENTRAR':
        senha = values['senha']
        if senha == token1 :
            windows1.close()
            event2, values2 = windows2.read()







