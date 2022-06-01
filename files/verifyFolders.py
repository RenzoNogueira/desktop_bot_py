import os
import vars
import tools.tools as tl
import pyautogui as pg

class VerifyFolders:
    filesFolders = []
    filesInFolders = []
    foldersToVerify = []

    def __init__(self, folders):
        self.foldersToVerify = folders
        self.filesFolders = self.readFile(self.foldersToVerify)
        self.filesInFolders = self.listFiles(self.foldersToVerify)
        self.verifyFiles(self.foldersToVerify)

    # Lê o arquivo json
    def readFile(self, folders = foldersToVerify):
        files = []
        fileJson = open("acceptedFiles.json")
        fileJson = tl.decodeJson(fileJson)
        for folder in fileJson:
            if folder in folders:
                files.extend(fileJson[folder])
        return files

    # Lista os arquivos do desktop
    def listFiles(self, folders = foldersToVerify):
        files = {}
        for folder in folders:
            files[folder] = os.listdir(vars.rootPc+folder)
        return files
    # TODO Verificar se o arquivo existe, se não existir, deletar
    # Verifica se os arquivos do desktop estão corretos
    def verifyFiles(self, folders = filesInFolders):
        arquivosDesconhecidos = {}
        # for com indice "folder" e posição dentro de folders
        for folder in folders:
            for file in folders[folders.index(folder)]:
                print(file)
                # if file not in self.filesFolders
                    # arquivosDesconhecidos[file] = folder
        if len(arquivosDesconhecidos) > 0:
            strApresentacao = ""
            for arquivo in arquivosDesconhecidos:
                strApresentacao += arquivo+"\n"
            action = pg.confirm("Os arquivos abaixo não são desconhecidos no Downloads:\n"+strApresentacao, "Arquivos não encontrados no desktop", ["Deletar", "Organizar", "Cancelar"])
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
            os.remove(vars.rootPc+"Downloads/"+file)
        return True

    # Organizar os arquivos recebidos por parametro em pastas com suas determinadas extensões
    def organizeFiles(self, files):
        for file in files:
            if file.endswith(".txt"):
                self.verifyFolder("Downloads/Textos")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Textos/"+file)
            elif file.endswith(".pdf"):
                self.verifyFolder("Downloads/Pdfs")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Pdfs/"+file)
            elif file.endswith(".docx"):
                self.verifyFolder("Downloads/Docs")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Docs/"+file)
            elif file.endswith(".xlsx"):
                self.verifyFolder("Downloads/Xls")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Xls/"+file)
            elif file.endswith(".pptx"):
                self.verifyFolder("Downloads/Pptx")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Pptx/"+file)
            elif file.endswith(".jpg"):
                self.verifyFolder("Downloads/Imgs")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Imgs/"+file)
            elif file.endswith(".png"):
                self.verifyFolder("Downloads/Imgs")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Imgs/"+file)
            elif file.endswith(".mp3"):
                self.verifyFolder("Downloads/Musicas")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Musicas/"+file)
            elif file.endswith(".mp4"):
                self.verifyFolder("Downloads/Videos")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Videos/"+file)
            elif file.endswith(".zip"):
                self.verifyFolder("Downloads/Zip")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Zip/"+file)
            elif file.endswith(".rar"):
                self.verifyFolder("Downloads/Rar")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Rar/"+file)
            elif file.endswith(".7z"):
                self.verifyFolder("Downloads/7z")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/7z/"+file)
            elif file.endswith(".iso"):
                self.verifyFolder("Downloads/Iso")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Iso/"+file)
            elif file.endswith(".exe"):
                self.verifyFolder("Downloads/Exe")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Exe/"+file)
            elif file.endswith(".apk"):
                self.verifyFolder("Downloads/Apk")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Apk/"+file)
            elif file.endswith(".bat"):
                self.verifyFolder("Downloads/Bat")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Bat/"+file)
            elif file.endswith(".sh"):
                self.verifyFolder("Downloads/Sh")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Sh/"+file)
            elif file.endswith(".py"):
                self.verifyFolder("Downloads/Py")
                os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Py/"+file)
            else:
                # verifica se arquivo é uma pasta
                if os.path.isdir(vars.rootPc+"Downloads/"+file):
                    self.verifyFolder("Downloads/OutrasPastas")
                    os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/OutrasPastas/"+file)
                else: 
                    self.verifyFolder("Downloads/Outros")
                    os.rename(vars.rootPc+"Downloads/"+file, vars.rootPc+"Downloads/Outros/"+file)
        return True

    # Verifica se pasta existe, se não existir, cria
    def verifyFolder(self, folder):
        if not os.path.exists(vars.rootPc+folder):
            os.makedirs(vars.rootPc+folder)
        return True
                



    

    
        
