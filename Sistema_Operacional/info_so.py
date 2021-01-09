import platform
import getpass
from datetime import datetime

print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())

print("******************************************")
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)

print("******************************************")
usuario =(getpass.getuser())
senha = (getpass.getpass("Digite sua senha:..."))

if usuario == "isisc" and senha == "hello_python":
    print("Bem-vindo")
else:
    print("Você não tem acesso!")

