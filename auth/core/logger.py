import logging
import logging.config
from logstash_async.formatter import LogstashFormatter

from .config import Settings

SETTINGS = Settings()


def setup_logger():
    handlers = ['console']
    if SETTINGS.LOGSTASH_SERVER != '' and SETTINGS.LOGSTASH_PORT != 0:
        handlers.append('logstash')

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'logstash': {
                '()': LogstashFormatter,
                'message_type': SETTINGS.APP_NAME,
                'extra': {
                    'application': SETTINGS.APP_NAME,
                },
            },
        },
        'handlers': {
            'console': {
                'level': SETTINGS.LOG_LEVEL,
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'logstash': {
                'level': SETTINGS.LOG_LEVEL,
                'class': 'logstash_async.handler.AsynchronousLogstashHandler',
                'host': SETTINGS.LOGSTASH_SERVER,
                'port': SETTINGS.LOGSTASH_PORT,
                'transport': 'logstash_async.transport.TcpTransport',
                'formatter': 'logstash',
                'database_path': f'logstash.{SETTINGS.APP_NAME}.db',
            },
        },
        'loggers': {
            '': {
                'handlers': handlers,
                'level': SETTINGS.LOG_LEVEL,
                'propagate': True,
            },
        },
    }

    logging.config.dictConfig(logging_config)
