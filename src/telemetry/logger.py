import logging.config

logger = logging.getLogger("Test Logging")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(levelname)s %(module)s: %(request_id)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "logs/logs.log",
            "maxBytes": 10000000,
            "backupCount": 3,
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {"root": {"level": "INFO", "handlers": ["file", "stderr"]}},
}


def setup_logging():
    logging.config.dictConfig(logging_config)
    return logger
