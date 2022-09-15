import os
import time
from typing import Generator
from subprocess import Popen

import requests
import yaml


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def use_sql(sql, db_link=""):
    """
    利用SQL语句对数据库进行增删改查
    :param sql:
    :param db_link:
    :return:
    """
    import records
    db = records.Database(db_link)
    return db.query(sql)
