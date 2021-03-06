from asyncore import read
from operator import index
import asyncio
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
    fileExtensions = []
    arquivosIgonorados = []
    inLooping = False
    timeInterval = 0

    def __init__(self, folders, inLooping):
        self.foldersToVerify = folders
        self.inLooping = inLooping
        # Carrega os arquivos aceitos
        self.filesFoldersAccept = self.readFile(self.foldersToVerify)
        
        # Lê arquivo txt contendo as extensões
        self.fileExtensions = open("extensions.txt", "r", encoding="utf-8")
        self.fileExtensions = self.fileExtensions.read().split("\n")
        
    async def __call__(self):
        print("InLooping Files")
        # Lista os arquivos do computador
        self.filesInFolders = self.listFiles(self.foldersToVerify)
        # Verifica os arquivos do computador
        self.verifyFiles(self.foldersToVerify)
        if self.inLooping:
            await asyncio.sleep(4)
            await self.__call__()


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
        pastaspredefinidas = ["Outros", "Pastas"]
        self.arquivosIgonorados = self.recoverLogFile()

        # Retiras os . dos itens do array self.fileExtensions
        for folder in folders:
            for file in self.filesInFolders[folder]:
                # Verifica a [key] é válida
                if folder in self.filesFoldersAccept:
                    # Verifica se o arquivo está na lista de arquivos aceitos
                    if file not in self.filesFoldersAccept[folder] and file not in [x[1:] for x in self.fileExtensions] and file not in pastaspredefinidas and file not in [x[1:] for x in self.arquivosIgonorados]:
                        # Se não estiver, adiciona na lista de arquivos desconhecidos
                        if folder not in arquivosDesconhecidos:
                            arquivosDesconhecidos[folder] = []
                        arquivosDesconhecidos[folder].append(file)
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
        

    # Deletar arquivos passados por parametro
    def deleteFiles(self, files):
        for file in files:
            os.remove(vars.rootPc+file)
        return True

    # Criar arquivo de lote de arquivos não listados na área de trabalho
    def createLogFile(self, files):
        logFile = open(vars.rootPc+"Desktop/arquivosNaoListados.txt", "w", encoding="utf-8")
        for file in files:
            print(file)
            logFile.write(files[file] + ": " + file + "\n")
        logFile.close()
        return True

    # Recupera o arquivo de log
    def recoverLogFile(self):
        # Verifica se o arquivo existe
        if os.path.exists(vars.rootPc+"Desktop/arquivosNaoListados.txt"):
            logFile = open(vars.rootPc+"Desktop/arquivosNaoListados.txt", "r", encoding="utf-8")
            logFile = logFile.read()
            # Converte o arquivo de log em um array separado por chave : valor
            logFile = logFile.split("\n")
            logFile = [x.split(": ") for x in logFile]
            return logFile
        else:
            return []

    # Organizar os arquivos recebidos por parametro em pastas com suas determinadas extensões
    def organizeFiles(self, folder, file):
        tarefaCompleta = False
        # Verifica se o caminho não está lisado no  arquivo de log
        # Veridica se a extensão do arquivo é conhecida
        for ext in self.fileExtensions:
            if file.endswith(ext):
                # Remove o . da extensão
                ext = ext[1:]
                # Verifica se pasta existe, se não existir, cria
                self.verifyFolder(folder+"/"+ext)
                # Move o arquivo para a pasta
                try:
                    os.rename(vars.rootPc+folder+"/"+file, vars.rootPc+folder+"/"+ext+"/"+file)
                    print("Arquivo movido: "+folder+"/"+file)
                    tarefaCompleta = True
                except:
                    print("Erro ao mover arquivo: "+folder+"/"+file)
                    return False
                return True
        # Senão, mover para pasta Pasta
        if not tarefaCompleta:
            # verifica se o arquivo é uma pasta
            if os.path.isdir(vars.rootPc+folder+"/"+file):
                # Verifica se pasta existe, se não existir, cria
                self.verifyFolder(folder+"/Pastas/")
                # Move a pasta para Pastas
                try:
                    os.rename(vars.rootPc+folder+"/"+file, vars.rootPc+folder+"/Pastas/"+file)
                    print("Pasta movida: "+folder+"/Pastas/"+file)
                    tarefaCompleta = True
                except:
                    print("Erro ao mover pasta: "+folder+"/Pastas/"+file)
                    return False
                return True
            else:
                # Verifica se pasta existe, se não existir, cria
                self.verifyFolder(folder+"/Outros")
                # Move o arquivo para a Outros
                try:
                    os.rename(vars.rootPc+folder+"/"+file, vars.rootPc+folder+"/Outros/"+file)
                    print("Arquivo movido: "+folder+"/Outros/"+file)
                    tarefaCompleta = True
                except:
                    print("Erro ao mover arquivo: "+folder+"/Outros/"+file)
                    return False
                return True
        return tarefaCompleta

    # Verifica se pasta existe, se não existir, cria
    def verifyFolder(self, folder):
        if not os.path.exists(vars.rootPc+folder):
            os.makedirs(vars.rootPc+folder)
        return True
                



    

    
        
