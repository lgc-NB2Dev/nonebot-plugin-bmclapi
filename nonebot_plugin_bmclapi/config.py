from nonebot import get_driver
from pydantic import BaseModel
from typing import Optional


class ConfigModel(BaseModel):
    bmclapi_cookie: Optional[str] = None


config: ConfigModel = ConfigModel.parse_obj(get_driver().config)
