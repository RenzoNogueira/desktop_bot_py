import json
# Lê o arquivo json de configurações
config = None
file = open("config.json", "r")
config = json.loads(file.read())
file.close()
