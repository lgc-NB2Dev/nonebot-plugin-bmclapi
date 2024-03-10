from typing import List, Optional

from nonebot.compat import PYDANTIC_V2
from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

# import humanize  # use jinja filter is more convenient, not class property


def camel_case(string: str, upper_first: bool = False) -> str:
    pfx, *rest = string.split("_")
    if upper_first:
        pfx = pfx.capitalize()
    sfx = "".join(x.capitalize() for x in rest)
    return f"{pfx}{sfx}"


class CamelAliasModel(BaseModel):
    if PYDANTIC_V2:
        model_config = ConfigDict(alias_generator=camel_case)
    else:

        class Config:
            alias_generator = camel_case


class NodeUser(BaseModel):
    name: str


class NodeSponsor(BaseModel):
    name: str
    url: Optional[str]
    banner: Optional[str]


class NodeMetric(CamelAliasModel):
    _id: str
    cluster_id: str
    date: str
    transfer_bytes: int = Field(alias="bytes")
    hits: int


class NodeInfo(CamelAliasModel):
    # 怎么这 API 还有只有三个元素的字段，为了兼容就这样吧 #
    # use Union and different models, then
    # NodeInfo: TypeAlias = Union[Model1, Model2, ...]
    _id: str
    name: str
    full_size: Optional[bool]
    is_enabled: bool
    down_reason: Optional[str]
    downtime: Optional[str]
    user: Optional[NodeUser]
    sponsor: Optional[NodeSponsor]
    metric: Optional[NodeMetric]


class SummaryHourly(BaseModel):
    _id: int
    transfer_bytes: int = Field(alias="bytes")
    hits: int
    bandwidth: int
    nodes: int


class Summary(CamelAliasModel):
    transfer_bytes: int = Field(alias="bytes")
    hits: int
    hourly: List[SummaryHourly]
    bandwidth: int
    current_bandwidth: float
    load: float
    current_nodes: int
