from typing import Optional

from pydantic import BaseModel, Field


class SystemItem(BaseModel):
    command: str
    key: str



