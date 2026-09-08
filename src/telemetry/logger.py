import logging.config

logger = logging.getLogger("Test Logging")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(message)s"}},
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "logs/logs.log",
            "maxBytes": 10000000,
            "backupCount": 3,
        }
    },
    "loggers": {"root": {"level": "INFO", "handlers": ["file"]}},
}


def setup_logging():
    logging.config.dictConfig(logging_config)
    return logger
