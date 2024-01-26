from typing import List, Optional

import humanize
from pydantic import BaseModel
from pydantic.fields import Field


class NodeUser(BaseModel):
    name: str


class NodeSponsor(BaseModel):
    name: str
    url: Optional[str]
    banner: Optional[str]


class NodeMetric(BaseModel):
    _id: str
    clusterId: str  # noqa: N815
    date: str
    transfor_bytes: int = Field(alias="bytes")
    hits: int

    @property
    def transfor_bytes_converted(self) -> str:
        return humanize.naturalsize(self.transfor_bytes)


class NodeInfo(BaseModel):
    # 怎么这 API 还有只有三个元素的字段，为了兼容就这样吧 #
    _id: str
    name: str
    fullSize: Optional[bool]  # noqa: N815
    isEnabled: bool  # noqa: N815
    downReason: Optional[str]  # noqa: N815
    downtime: Optional[str]
    user: Optional[NodeUser]
    sponsor: Optional[NodeSponsor]
    metric: Optional[NodeMetric]


class SummaryHourly(BaseModel):
    _id: int
    transfor_bytes: int = Field(alias="bytes")
    hits: int
    bandwidth: int
    nodes: int

    @property
    def transfor_bytes_converted(self) -> str:
        return humanize.naturalsize(self.transfor_bytes)


class Summary(BaseModel):
    transfor_bytes: int = Field(alias="bytes")
    hits: int
    hourly: List[SummaryHourly]
    bandwidth: int
    currentBandwidth: float  # noqa: N815
    load: float
    currentNodes: int  # noqa: N815

    @property
    def transfor_bytes_converted(self) -> str:
        return humanize.naturalsize(self.transfor_bytes)
