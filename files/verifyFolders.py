from asyncore import read
from operator import index
import os
import vars
import tools.tools as tl
import pyautogui as pg

# set charset utf-8
pg.FAILSAFE = True


class VerifyFolders:
    filesFoldersAccept = []
    filesInFolders = []
    foldersToVerify = []

    def __init__(self, folders):
        self.foldersToVerify = folders
        self.filesFoldersAccept = self.readFile(self.foldersToVerify)
        self.filesInFolders = self.listFiles(self.foldersToVerify)
        self.verifyFiles(self.foldersToVerify)

    # Lê o arquivo json de arquivos aceitos
    def readFile(self, folders = foldersToVerify):
        files = {}
        fileJson = open("acceptedFiles.json")
        fileJson = tl.decodeJson(fileJson)
        for folder in fileJson:
            if folder in folders:
                files[folder] = fileJson[folder]
        # print("Arquivos aceitos: \n"+str(files))
        return files

    # Lista os arquivos do desktop
    def listFiles(self, folders = foldersToVerify):
        files = {}
        for folder in folders:
            files[folder] = os.listdir(vars.rootPc+folder)
        return files

    # Verifica se os arquivos do desktop estão corretos
    def verifyFiles(self, folders = filesInFolders):
        arquivosDesconhecidos = {}
        for folder in folders:
            for file in self.filesInFolders[folder]:
                # Verifica a [key] é válida
                if folder in self.filesFoldersAccept:
                    # Verifica se o arquivo está na lista de arquivos aceitos
                    if file not in self.filesFoldersAccept[folder]:
                        print("Arq desc: ["+folder+"] "+file)
                        # adiciona ao objeto arquivosDesconhecidos
                        arquivosDesconhecidos[file] = folder
        if len(arquivosDesconhecidos) > 0:
            prompt = pg.confirm("O que deseja fazer?", "Arquivos não listados encontrados", ["Oganizar", "Ignorar"])
            if prompt == "Oganizar":
                for file in arquivosDesconhecidos:
                    print("Arquivo: "+arquivosDesconhecidos[file]+" - "+file)
                    self.organizeFiles(arquivosDesconhecidos[file], str(file))
            elif prompt == "Ignorar":
                self.createLogFile(arquivosDesconhecidos)
                pg.alert("Os arquivos não listados foram ignorados e estão listados em um arquivo txt na área de trabalho.","Você optou por ignorar os arquivos não listados.")
        return len(arquivosDesconhecidos) == 0

    # Deletar arquivos passados por parametro
    def deleteFiles(self, files):
        for file in files:
            os.remove(vars.rootPc+file)
        return True

    # Criar arquivo de lote de arquivos não listados na área de trabalho
    def createLogFile(self, files):
        logFile = open(vars.rootPc+"Desktop/arquivosNaoListados.txt", "w", encoding="utf-8")
        for file in files:
            logFile.write(files[file] + ": " + file + "\n")
        logFile.close()
        return True

    # Organizar os arquivos recebidos por parametro em pastas com suas determinadas extensões
    def organizeFiles(self, folder, file):
        # Lê arquivo txt contendo as extensões
        fileExtensions = open("extensions.txt", "r", encoding="utf-8")
        fileExtensions = fileExtensions.read().split("\n")
        tarefaCompleta = False
        # Veridica se a extensão do arquivo é conhecida
        for ext in fileExtensions:
            if file.endswith(ext):
                # Retira o ponto da primeira posição da string
                ext = ext[1:]
                # Verifica se pasta existe, se não existir, cria
                self.verifyFolder(folder+"/"+ext)
                # Move o arquivo para a pasta
                os.rename(vars.rootPc+folder+"/"+file, vars.rootPc+folder+"/"+ext+"/"+file)
                print("Arquivo movido: "+folder+"/"+file)
                tarefaCompleta = True
                return True
        # Senão mover para pasta Outros
        if not tarefaCompleta:
            # verifica se o arquivo é uma pasta
            if os.path.isdir(vars.rootPc+folder+"/"+file):
                # Verifica se pasta existe, se não existir, cria
                self.verifyFolder(folder+"/Pastas/")
                # Move a pasta para Pastas
                os.rename(vars.rootPc+folder+"/"+file, vars.rootPc+folder+"/Pastas/"+file)
                print("Pasta movida: "+folder+"/Pastas/"+file)
                tarefaCompleta = True
                return True
            else:
                # Verifica se pasta existe, se não existir, cria
                self.verifyFolder(folder+"/Outros")
                # Move o arquivo para a Outros
                os.rename(vars.rootPc+folder+"/"+file, vars.rootPc+folder+"/Outros/"+file)
                print("Arquivo movido: "+folder+"/Outros/"+file)
                return True
        return tarefaCompleta

    # Verifica se pasta existe, se não existir, cria
    def verifyFolder(self, folder):
        if not os.path.exists(vars.rootPc+folder):
            os.makedirs(vars.rootPc+folder)
        return True
                



    

    
        
