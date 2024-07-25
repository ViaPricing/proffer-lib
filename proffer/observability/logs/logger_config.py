import os

class LoggerConfig:
    def __init__(self):
        self.host = os.getenv("LOGGER_HOST", "localhost")
        self.port = os.getenv("LOGGER_PORT", 50000)
    