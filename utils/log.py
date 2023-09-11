from __future__ import annotations
import os
from typing import TYPE_CHECKING
from pathlib import Path
from loguru import logger
from settings import settings

if TYPE_CHECKING:
    import loguru

BasePath = Path(__file__).resolve().parent.parent


class Logger:
    def __init__(self):
        self.log_path =os.path.join(BasePath,'logs')

    def log(self) -> loguru.Logger:
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)

        log_stdout_file = os.path.join(self.log_path, settings.LOG_STDOUT_FILENAME)
        log_stderr_file = os.path.join(self.log_path, settings.LOG_STDERR_FILENAME)

        log_config = dict(rotation='10 MB', retention='15 days', compression='tar.gz', enqueue=True)

        logger.add(
            log_stdout_file,
            level='INFO',
            filter=lambda record: record['level'].name == 'INFO' or record['level'].no <= 25,
            **log_config,
            backtrace=False,
            diagnose=False,
        )

        logger.add(
            log_stderr_file,
            level='ERROR',
            filter=lambda record: record['level'].name == 'ERROR' or record['level'].no >= 30,
            **log_config,
            backtrace=True,
            diagnose=True,
        )

        return logger


log = Logger().log()