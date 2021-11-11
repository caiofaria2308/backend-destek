from utils import Crypt, Setting

"""
GERAR SECRET_KEY:
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())

LISTA DE ENGINES

    django.db.backends.postgresql (recomendado)
    django.db.backends.mysql
    django.db.backends.sqlite3
    django.db.backends.oracle
"""


crypt = Crypt()
database_engine = crypt.encrypt(input("Digite a engine do banco de dados: "))
database_name = crypt.encrypt(input("Digite o nome do banco de dados: "))
database_user = crypt.encrypt(input("Digite o usuário do banco de dados: "))
database_password = crypt.encrypt(input("Digite a senha do usuário do banco de dados: "))
database_host = crypt.encrypt(input("Digite o endereço do banco de dados(ex: localhost): "))
database_port = crypt.encrypt(input("Digite a porta do banco de dados(default postgres: 5432): "))

sett = Setting()
sett.load_setting()

dados_formatado = f'''secret_key = {sett.secret_key.decode()}
database_engine = {database_engine}
database_name = {database_name}
database_user = {database_user}
database_password = {database_password}
database_host = {database_host}
database_port = {database_port}'''
print("Dados criptografados".center(50, '-'))
print(dados_formatado)
try:
    deseja_salvar = input("Deseja salvar os dados? (Digite 'sim' para salvar): ")
    if deseja_salvar.upper() == "SIM":
        name = input("Qual vai ser o nome do arquivo ?(preencha .env caso queria substituir o arquivo): ")
        with open(name, 'w+') as file:
            file.write(dados_formatado)
except TypeError as e:
    print("Erro ao salvar dados !")
