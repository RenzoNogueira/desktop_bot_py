import pyautogui as pg
import time
import json

class safety:
    toVerify = {}
    inLooping = False
    timeInterval = 0

    def __init__(self, inLooping = False, timeInterval = 1):
        self.inLooping = inLooping
        self.timeInterval = timeInterval
        self.toVerify = open("safety/toVerify.json")
        self.toVerify = json.load(self.toVerify)

    # Se chamado como método
    def __call__(self):
        self.print("InLooping")
        # Verificar se está em um site Privado
        self.checkPrivacity(self.toVerify)
        # Se inLooping for True, se rechamar o método
        if self.inLooping:
            time.sleep(self.timeInterval)
            self.__call__()

    # Localiza o objeto na tela
    def locateImg(self, img):
        try:
            # Localiza a imagem
            x, y = pg.locateCenterOnScreen(img)
            return [x, y]
        except:
            return False

    # Alerta
    def alert(self, title, msg, condition = False):
        if condition:
            pg.alert(title, msg)

    # Move o mouse para o objeto
    def moveToPositionImage(self, x, y, wait = 0):
        try:
            pg.moveTo(x, y, duration = wait)
            return True
        except:
            return False

    # Clicar em um objeto
    def clickImage(self, img, wait = 0):
        try:
            pg.click(img, duration = wait)
            return True
        except:
            return False
    
    # Verificar se está em um site Privado
    def checkPrivacity(self, obj = toVerify):
        breaking = False
        for sc in obj:
            if breaking:
                break
            for img in obj[sc]:
                self.print("[Checando por]: safety/images/"+img)
                if self.locateImg("safety/images/"+img) != False:
                    pg.alert("Você está em um site privado.", "Aviso")
                    breaking = True
                    break

    # Imprimir no console
    def print(self, msg):
        date = time.strftime("%d/%m/%Y %H:%M:%S")
        print("[" + date + "]" + " - " + msg)