import os
import vars
import tools.tools as tl
import pyautogui as pg

class deskTopVerify:
    filesDeskTop = []
    filesInDeskTop = []

    def __init__(self):
        self.filesDeskTop = self.readFile()["files"]
        self.filesInDeskTop = self.listFiles()
        self.verifyFiles()

    # Lê o arquivo json
    def readFile(self):
        return tl.decodeJson(vars.rootProject+'files/desktop.json', "file")

    # Lista os arquivos do desktop
    def listFiles(self):
        return os.listdir(vars.rootPc+"Desktop")

    # Verifica se os arquivos do desktop estão corretos
    def verifyFiles(self):
        arquivosDesconhecidos = []
        for file in self.filesInDeskTop:
            if file not in self.filesDeskTop:
                arquivosDesconhecidos.append(file)
                print("Arquivo: "+file+" é um arquivo desconhecido")
        if len(arquivosDesconhecidos) > 0:
            action = pg.confirm("Os arquivos abaixo não são desconhecidos no Desktop:\n"+str(arquivosDesconhecidos), "Arquivos não encontrados no desktop", ["Deletar", "Organizar", "Cancelar"])
            if action == "Deletar":
                self.deleteFiles(arquivosDesconhecidos)
            elif action == "Organizar":
                self.organizeFiles(arquivosDesconhecidos)
            elif action == "Cancelar":
                return False
        return len(arquivosDesconhecidos) == 0

    # Deletar arquivos passados por parametro
    def deleteFiles(self, files):
        for file in files:
            os.remove(vars.rootPc+"Desktop/"+file)
        return True

    # Organizar os arquivos recebidos por parametro em pastas com suas determinadas extensões
    def organizeFiles(self, files):
        for file in files:
            if file.endswith(".txt"):
                self.verifyFolder("Desktop/textos")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/textos/"+file)
            elif file.endswith(".pdf"):
                self.verifyFolder("Desktop/pdfs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/pdfs/"+file)
            elif file.endswith(".docx"):
                self.verifyFolder("Desktop/docs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/docs/"+file)
            elif file.endswith(".xlsx"):
                self.verifyFolder("Desktop/xls")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/xls/"+file)
            elif file.endswith(".pptx"):
                self.verifyFolder("Desktop/pptx")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/pptx/"+file)
            elif file.endswith(".jpg"):
                self.verifyFolder("Desktop/imgs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/imgs/"+file)
            elif file.endswith(".png"):
                self.verifyFolder("Desktop/imgs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/imgs/"+file)
            elif file.endswith(".mp3"):
                self.verifyFolder("Desktop/musicas")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/musicas/"+file)
            elif file.endswith(".mp4"):
                self.verifyFolder("Desktop/videos")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/videos/"+file)
            elif file.endswith(".zip"):
                self.verifyFolder("Desktop/zip")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/zip/"+file)
            elif file.endswith(".rar"):
                self.verifyFolder("Desktop/rar")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/rar/"+file)
            elif file.endswith(".7z"):
                self.verifyFolder("Desktop/7z")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/7z/"+file)
            elif file.endswith(".iso"):
                self.verifyFolder("Desktop/iso")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/iso/"+file)
            elif file.endswith(".exe"):
                self.verifyFolder("Desktop/exe")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/exe/"+file)
            elif file.endswith(".apk"):
                self.verifyFolder("Desktop/apk")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/apk/"+file)
            elif file.endswith(".bat"):
                self.verifyFolder("Desktop/bat")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/bat/"+file)
            elif file.endswith(".sh"):
                self.verifyFolder("Desktop/sh")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/sh/"+file)
            elif file.endswith(".py"):
                self.verifyFolder("Desktop/py")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/py/"+file)
            else:
                # verifica se arquivo é uma pasta
                if os.path.isdir(vars.rootPc+"Desktop/"+file):
                    self.verifyFolder("Desktop/outrasPastas")
                    os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/outrasPastas/"+file)
                else: 
                    self.verifyFolder("Desktop/outros")
                    os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/outros/"+file)
        return True

    # Verifica se pasta existe, se não existir, cria
    def verifyFolder(self, folder):
        if not os.path.exists(vars.rootPc+folder):
            os.makedirs(vars.rootPc+folder)
        return True
                



    

    
        
