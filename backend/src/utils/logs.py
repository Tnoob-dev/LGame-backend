from logging import getLogger

class Logger:
    def __init__(self) -> None:
        self.logger = getLogger("uvicorn")
    
    def info(self, message: str):
        self.logger.info(message)
    
    def warning(self, message: str):
        self.logger.warning(message)
        
    def error(self, message: str):
        self.logger.error(message)