# Saudação
import time
import pyautogui as pg
import vars

def saudacao():
    saudacao = None
    #  verifica a hora do dia para dar "Bom dia", "Boa tarde" ou "Boa noite"
    if time.strftime("%H") >= "5" and time.strftime("%H") <= "12":
        saudacao = "Bom dia"
    elif time.strftime("%H") >= "13" and time.strftime("%H") <= "18":
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    confirm = pg.confirm("\tOlá, seja bem vindo!\n\n\t\t😁\n\nDeseja que eu execute alguns processos em segundo plano?", "Olá, "+saudacao+ " "+ vars.user,  ["Executar", "Não obrigado"])
    if confirm == "Executar":
        confirm = True
    elif confirm == "Não obrigado":
        pg.alert("Obrigado, nós veremos depois! Algumas operações de segurança continuarão executando em segundo plano.", "Olá, "+saudacao+ " "+ vars.user)
        confirm = False
    return confirm