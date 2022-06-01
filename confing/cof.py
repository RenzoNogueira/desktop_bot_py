import json
#   Lê o arquivo json de configurações
confing = None
file = open("confing.json", "r")
confing = json.loads(file.read())
file.close()
