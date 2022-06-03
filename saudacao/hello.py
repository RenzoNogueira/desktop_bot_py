# Saudação
import time
import pyautogui as pg
import confing.cof as conf

def saudacao():
    saudacao = None
    #  verifica a hora do dia para dar "Bom dia", "Boa tarde" ou "Boa noite"
    if time.strftime("%H") >= "06" and time.strftime("%H") <= "12":
        saudacao = "Bom dia"
    elif time.strftime("%H") >= "13" and time.strftime("%H") <= "18":
        saudacao = "Boa tarde"
    elif time.strftime("%H") >= "19" and time.strftime("%H") <= "23":
        saudacao = "Boa noite"

    confirm = pg.confirm("\tOlá, seja bem vindo!\n\n\t\t😁\n\nDeseja que eu execute em segundo plano?", "Olá, "+saudacao+ " "+ conf.nameUser,  ["Executar", "Não obrigado"])
    if confirm == "Executar":
        confirm = True
    elif confirm == "Não obrigado":
        pg.alert("Obrigado, nós veremos depois!", "Olá, "+saudacao+ " "+ conf.nameUser)
        confirm = False
    return confirm