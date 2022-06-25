import configparser

class ConfigManager(object):

    def __init__(self) -> None:
        self.config = configparser.SafeConfigParser()
        self.config.read('config/config.ini')
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigManager, cls).__new__(cls)
        return cls.instance

    def get(self,section):
        return self.config[section]