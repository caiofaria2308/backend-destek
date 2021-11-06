from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import jwt


class Setting:
    """
    Classe que trata o arquivo .env
    """
    def __init__(self) -> None:
        load_dotenv()
        self.__secret_key = None
        self.__database_engine = None
        self.__database_name = None
        self.__database_user = None
        self.__database_password = None
        self.__database_host = None
        self.__database_port = None
        return


    def load_setting(self) -> None:
        self.__secret_key = os.getenv('secret_key').encode()
        self.__database_engine = os.getenv('database_engine')
        self.__database_name = os.getenv('database_name')
        self.__database_user = os.getenv('database_user')
        self.__database_password = os.getenv('database_password')
        self.__database_host = os.getenv('database_host')
        self.__database_port = os.getenv('database_port')
        return


    def decrypy_setting(self) -> None:
        crypt = Crypt()
        self.__database_engine = crypt.decrypt(self.__database_engine)
        self.__database_name = crypt.decrypt(self.__database_name)
        self.__database_user = crypt.decrypt(self.__database_user)
        self.__database_password = crypt.decrypt(self.__database_password)
        self.__database_host = crypt.decrypt(self.__database_host)
        self.__database_port = crypt.decrypt(self.__database_port)
        return


    @property
    def secret_key(self) -> bytes:
        return self.__secret_key

    @property
    def database_engine(self) -> str:
        return self.__database_engine

    @property
    def database_name(self) -> str:
        return self.__database_name

    @property
    def database_user(self) -> str:
        return self.__database_user

    @property
    def database_password(self) -> str:
        return self.__database_password

    @property
    def database_host(self) -> str:
        return self.__database_host

    @property
    def database_port(self) -> str:
        return self.__database_port


class Crypt:
    """
    Classe de criptografia/descriptografia        
    """
    def __init__(self) -> None:
        sett = Setting()
        sett.load_setting()
        self.__key = sett.secret_key
        self.__fernet = Fernet(self.__key)
        return


    def encrypt(self, message: str) -> str:
        enc_message = self.__fernet.encrypt(message.encode())
        return enc_message.decode()


    def decrypt(self, enc_message: str) -> str:
        message = self.__fernet.decrypt(enc_message.encode()).decode()
        return str(message)
