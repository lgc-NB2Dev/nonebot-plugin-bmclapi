# from typing import Optional

from nonebot import get_plugin_config
from pydantic import BaseModel


class ConfigModel(BaseModel):
    # bmclapi_cookie: Optional[str] = None
    pass


config = get_plugin_config(ConfigModel)
