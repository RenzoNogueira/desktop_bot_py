import os

# Pasta do usuário atual do sistema
rootPc = os.path.expanduser('~').replace('\\', '/')
# Pasta atual do projeto
rootProject = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
# Usuário do sistema
user = os.getlogin()