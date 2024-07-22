import json
import logging
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "message": record.getMessage(),
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "extra": record.__dict__,
        }

        return json.dumps(log_record)
