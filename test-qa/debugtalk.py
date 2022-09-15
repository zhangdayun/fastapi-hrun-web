import time
from pathlib import Path

import requests
import yaml
from httprunner import __version__

BASE_PATH: str = str(Path(__file__).absolute().parents[1])
ENV_PATH: Path = Path(BASE_PATH, "test-qa/ENV.yml")


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


# 读取yaml文件, .env文件不好改写，换成yaml文件
def get_yaml(key: str):
    with open(ENV_PATH) as f:
        content = yaml.load(f, Loader=yaml.FullLoader)

    if key in content.keys():
        # logs.info(f'env.yml 获取 {key}')
        return content[key]

    # logs.warning(f'env.yml 未获取 {key}')
    return 'NotFound'
