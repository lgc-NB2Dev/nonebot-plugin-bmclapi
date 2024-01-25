from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_alconna")

from . import __main__ as __main__  # noqa: E402
from .config import ConfigModel  # noqa: E402

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-bmclapi",
    description="在聊天软件内插件 OpenBMCLAPI 状态",
    usage="",
    type="application",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-bmclapi",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={"License": "MIT", "Author": "student_2333 & XieXiLin"},
)
