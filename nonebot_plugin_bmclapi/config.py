# from typing import Optional

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    # bmclapi_cookie: Optional[str] = None
    pass


config: ConfigModel = ConfigModel.parse_obj(get_driver().config)
