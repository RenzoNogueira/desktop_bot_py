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
        return tl.decodeJson('files/desktop.json', "file")

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
                self.verifyFolder("Desktop/Textos")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Textos/"+file)
            elif file.endswith(".pdf"):
                self.verifyFolder("Desktop/Pdfs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Pdfs/"+file)
            elif file.endswith(".docx"):
                self.verifyFolder("Desktop/Docs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Docs/"+file)
            elif file.endswith(".xlsx"):
                self.verifyFolder("Desktop/Xls")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Xls/"+file)
            elif file.endswith(".pptx"):
                self.verifyFolder("Desktop/Pptx")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Pptx/"+file)
            elif file.endswith(".jpg"):
                self.verifyFolder("Desktop/Imgs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Imgs/"+file)
            elif file.endswith(".png"):
                self.verifyFolder("Desktop/Imgs")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Imgs/"+file)
            elif file.endswith(".mp3"):
                self.verifyFolder("Desktop/Musicas")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Musicas/"+file)
            elif file.endswith(".mp4"):
                self.verifyFolder("Desktop/Videos")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Videos/"+file)
            elif file.endswith(".zip"):
                self.verifyFolder("Desktop/Zip")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Zip/"+file)
            elif file.endswith(".rar"):
                self.verifyFolder("Desktop/Rar")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Rar/"+file)
            elif file.endswith(".7z"):
                self.verifyFolder("Desktop/7z")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/7z/"+file)
            elif file.endswith(".iso"):
                self.verifyFolder("Desktop/Iso")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Iso/"+file)
            elif file.endswith(".exe"):
                self.verifyFolder("Desktop/Exe")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Exe/"+file)
            elif file.endswith(".apk"):
                self.verifyFolder("Desktop/Apk")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Apk/"+file)
            elif file.endswith(".bat"):
                self.verifyFolder("Desktop/Bat")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Bat/"+file)
            elif file.endswith(".sh"):
                self.verifyFolder("Desktop/Sh")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Sh/"+file)
            elif file.endswith(".py"):
                self.verifyFolder("Desktop/Py")
                os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Py/"+file)
            else:
                # verifica se arquivo é uma pasta
                if os.path.isdir(vars.rootPc+"Desktop/"+file):
                    self.verifyFolder("Desktop/OutrasPastas")
                    os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/OutrasPastas/"+file)
                else: 
                    self.verifyFolder("Desktop/Outros")
                    os.rename(vars.rootPc+"Desktop/"+file, vars.rootPc+"Desktop/Outros/"+file)
        return True

    # Verifica se pasta existe, se não existir, cria
    def verifyFolder(self, folder):
        if not os.path.exists(vars.rootPc+folder):
            os.makedirs(vars.rootPc+folder)
        return True
                



    

    
        
