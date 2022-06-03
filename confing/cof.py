import json
import os
#   Lê o arquivo json de configurações
confing = None
file = open("confing.json", "r")
confing = json.loads(file.read())
file.close()
# Pega o nome de usuário do sistema
nameUser = os.getlogin()
