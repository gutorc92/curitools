import os
import time
import codecs
import re
import getpass

class MissingFileSettings(Exception):
    pass

class Settings(object):
    
    def __init__(self, file_path  = None):
        self.file_path = file_path if file_path is not None else self.find_settings_file()

    def find_settings_file(self):
        uritools_dir = os.path.expanduser("~")
        file_settings = os.path.join(uritools_dir, ".uri.settings")
        if os.path.isfile(file_settings):
            return file_settings
        uritools_dir = os.path.dirname(os.path.realpath(__file__))
        file_settings = os.path.join(uritools_dir, ".uri.settings")
        if os.path.isfile(file_settings):
            return file_settings
        file_settings = os.path.join(uritools_dir,"..", ".uri.settings")
        if os.path.isfile(file_settings):
            return file_settings
        file_settings = os.path.join(os.getcwd(),".uri.settings")
        if os.path.isfile(file_settings):
            return file_settings
        file_settings = os.path.join(os.getcwd(),"..", ".uri.settings")
        if os.path.isfile(file_settings):
            return file_settings
        else:
            print("Nao foi encontrado um arquivo de configuracoes")
            if self.create_file_settings():
                uritools_dir = os.path.expanduser("~")
                file_settings = os.path.join(uritools_dir, ".uri.settings")
                return file_settings
            return None

    def create_file_settings(self):
        var = input("Voce deseja criar o arquivo de configuracao:[S/N] ")
        if "S" in var:    
            user = input("Digite o seu email: ")
            password = getpass.getpass("Digite a sua senha: ")
            uritools_dir = os.path.expanduser("~")
            file_settings = os.path.join(uritools_dir, ".uri.settings")
            if user and password:
                user = "user: " + user + "\n"
                password = "password: " + password
                with open(file_settings, "w") as handle:
                    handle.write(user)
                    handle.write(password)
                return True
        else:
            print("O arquivo de configuracao e necessario")
            return False
            
    def get_user(self,line):
        m = re.search("user: (.*)", line)
        if m is not None:
            return m.group(1)
        return m

    def get_password(self, line):
        m = re.search("password: (.*)", line)
        if m is not None:
            return m.group(1)
        return m

    def read_settings(self):
        user = ""
        password = ""
        if self.file_path is None:
             raise MissingFileSettings("O arquivo de configuracão nao foi encontrado")
        with open(self.file_path, "r") as handle:
            for line in handle:
                if self.get_user(line) is not None:
                    user = self.get_user(line)
                if self.get_password(line) is not None:
                    password = self.get_password(line)
        self.user = user
        self.passwrod = password
        return user,password

    def get_settings(self):
        if hasattr(self, 'user') and hasattr(self, 'password') and self.user and self.password:
            return self.user, self.password
        else:
            return self.read_settings()


