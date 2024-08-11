import configparser #it reads ini files

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig_Class:
    @staticmethod
    def getUsername():
        Username=config.get("login data","username")
        return Username

    @staticmethod
    def getPassword():
        Password = config.get("login data", "password")
        return Password