import logging, logging.config
import os
import time


class RequestIdFilter(logging.Filter):
    """
    We use this to add the aws_request_id
    """
    environment = "UNKNOWN"
    process_id = "NONE"
    request_uuid = "NONE"
    request_status = "NONE"
    table_name = "NONE"
    pipeline_name = "NONE"

    def filter(self, record):
        record.environment = self.environment
        record.process_id = self.process_id
        record.request_uuid = self.request_uuid
        record.request_status = self.request_status
        record.pipeline_name = self.pipeline_name
        record.table_name = self.table_name
        return True


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


def setup_logging(default_level=logging.INFO, log_prefix=''):
    """Setup logging configuration """
    env_name = os.getenv('ENV_NAME', 'UKNOWN')
    RequestIdFilter.environment = env_name
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        'formatters': {
            'utc': {
                '()': UTCFormatter,
                'format': '{"pipeline_name": "%(pipeline_name)s", '
                          '"request_status": "%(request_status)s", '
                          '"timestamp": "%(asctime)s", '
                          '"log_level": "%(levelname)s", '
                          '"name": "%(name)s", '
                          '"file_name": "%(filename)s:%(lineno)s", '
                          '"environment": "%(environment)s", '
                          '"message": "%(message)s"}'
            }
        },
        "filters": {
            "request_id": {"()": RequestIdFilter}
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "utc",
                "stream": "ext://sys.stdout",
                "filters": ["request_id"]
            }
        },
        "root": {
            "level": "INFO",
            "handlers": [
                "console"
            ]
        }
    }
    logging.config.dictConfig(log_config)
    return

    
def set_log_record_field(process_id=None, request_uuid=None, request_status=None, table_name=None, pipeline_name="PEGAfrica"):
    RequestIdFilter.process_id = process_id or RequestIdFilter.process_id
    RequestIdFilter.request_uuid = request_uuid or RequestIdFilter.request_uuid
    RequestIdFilter.request_status = request_status or RequestIdFilter.request_status
    RequestIdFilter.table_name = table_name or RequestIdFilter.table_name
    RequestIdFilter.pipeline_name = pipeline_name or RequestIdFilter.pipeline_name
    return


def unset_log_record_fields():
    RequestIdFilter.process_id = "NONE"
    RequestIdFilter.request_uuid = "NONE"
    RequestIdFilter.request_status = "NONE"
    RequestIdFilter.table_name = "NONE"
    RequestIdFilter.pipeline_name = "NONE"
    return




