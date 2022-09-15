import time
from loguru import logger
from pathlib import Path
from demo.core.config import settings

# 拼接log文件路径
base_path = settings.BASE_PATH
log_path = Path(base_path, "logs")
t = time.strftime("%Y_%m_%d")


class Loggings:
    __instance = None
    logger.add(f"{log_path}/aicc_log_{t}.log", rotation="500MB", encoding="utf-8", enqueue=True,
               retention="10 days", backtrace=True, diagnose=True)

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    @staticmethod
    def info(msg):
        return logger.info(msg)

    @staticmethod
    def debug(msg):
        return logger.debug(msg)

    @staticmethod
    def warning(msg):
        return logger.warning(msg)

    @staticmethod
    def error(msg):
        return logger.error(msg)

    @staticmethod
    def exception(msg):
        return logger.exception(msg)


logs = Loggings()
