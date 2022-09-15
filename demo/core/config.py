from pathlib import Path

from pydantic import BaseSettings
from urllib.parse import quote_plus as urlquote


class Settings(BaseSettings):
    API_STR: str = "/api"  # 默认url初始路径
    TITLE: str = ""  # 项目名称
    PROJECT_NAME: str = ""
    DESCRIPTION: str = "接口自动化测试项目"  # 项目说明
    BASE_PATH: str = str(Path(__file__).absolute().parents[2])  # 项目根路径
    LOCAL_URL: str = "http://127.0.0.1:7799"

    CORE_TESTCASES_PATH: Path = Path(BASE_PATH, "")
    CREATE_TASKS_PATH: Path = Path(BASE_PATH, "")
    ENV_PATH: Path = Path(BASE_PATH, "")

    REPORTS_PATH: Path = Path(BASE_PATH, "test-qa/reports")
    WAIT_RESULT_PATH: Path = Path(BASE_PATH, "templates/wait_result.html")

    SYSTEM_API_KEY = ""

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: str = ""
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = ''

    # Mysql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"


settings = Settings()
