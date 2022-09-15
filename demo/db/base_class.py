from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        import re
        # 如果没有指定__tablename__  则默认使用model类名转换表名字
        names = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        names.insert(0, 't')
        # 表名格式替换成 下划线_格式 如 MallUser 替换成 mall_user
        return "_".join(names).lower()
