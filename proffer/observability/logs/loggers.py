import logging

from proffer.observability.logs import JsonFormatter
from typing import Optional

class ProfferLogger:
    PROJECT_NAME = "proffer"
    handler: Optional[logging.Handler]

    def __init__(self, id: str, name: str, **kwargs):
        name = f"{self.PROJECT_NAME}.{name}.{id}"

        self.remove_logger_handlers(name)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = kwargs.get("formatter", None)
        self.formatter = formatter if formatter else JsonFormatter()

        handler = kwargs.get("handler", None)
        self.handler = handler if handler else logging.StreamHandler()
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

    def __init__(self, identifier: str, formatter: JsonFormatter = None, handler: Optional[logging.Handler] = None):
        name = "web_scraper"
        super().__init__(identifier, name, formatter=formatter, handler=handler)