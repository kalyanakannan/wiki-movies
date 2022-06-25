import logging

class Log:

    def __init__(self) -> None:
        logging.basicConfig(filename="debug.log",
                    format='%(asctime)s-%(levelname)s:%(message)s',
                    filemode='w')
            # Creating an object
        self.logger = logging.getLogger()
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
        return cls.instance
    
    def logger(self, message, mode):
        if mode == 'debug':
            self.logger.debug(message)
        elif mode == 'info':
            self.logger.info(message)
        elif mode == 'warning':
            self.logger.warning(message)
        elif mode == 'error':
            self.logger.error(message)
        elif mode == 'critical':
            self.logger.critical(message)