import logging

from logstash_async.handler import SynchronousLogstashHandler

from proffer.observability.logs.formatter import JsonFormatter
from proffer.observability.logs.logger_config import LoggerConfig


class ProfferLogger:
    PROJECT_NAME = "proffer"

    def __init__(self, config: LoggerConfig, **kwargs):
        self.host = config.host
        self.port = config.port

        name = f"{self.PROJECT_NAME}.{config.resource['name']}.{config.resource['id']}"

        self.remove_logger_handlers(name)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        if kwargs.get("formatter", None):
            self.formatter = kwargs.get("formatter")
        else:
            self.formatter = JsonFormatter()

        self.handler = SynchronousLogstashHandler(
            self.host, self.port, database_path=None
        )
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def log(self, message, extra=None):
        self.logger.info(message, extra=extra)

    def error(self, message, extra=None):
        self.logger.error(message, extra=extra)

    def warning(self, message, extra=None):
        self.logger.warning(message, extra=extra)

    def debug(self, message, extra=None):
        self.logger.debug(message, extra=extra)

    def remove_logger_handlers(self, logger_name):
        logger = logging.getLogger(logger_name)
        handlers = logger.handlers[:]
        for handler in handlers:
            handler.close()
            logger.removeHandler(handler)


class WebScraperLogger(ProfferLogger):
    name = "web_scraper"

    def __init__(self, id: str, config: LoggerConfig, formatter: JsonFormatter = None):
        config.resource = {
            "name": self.name,
            "id": id,
        }

        super().__init__(config, formatter=formatter)
