from asyncore import read
import json

# Decodifica um arquivo ou texto json
def decodeJson(text, type = "text"):
    if type == "text": # Se for texto
        return json.load(text)
    elif type == "file": # Arquivo
        file = open(text, 'r')
        return json.load(file) # Decodifica o arquivo
