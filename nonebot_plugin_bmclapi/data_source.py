from typing import List

import httpx
from nonebot.compat import type_validate_python

from .models import NodeInfo, Summary

OPENBMCLAPI_BASE = "https://bd.bangbang93.com/openbmclapi"
OPENBMCLAPI_METRIC = f"{OPENBMCLAPI_BASE}/metric"


async def get_summary() -> Summary:
    async with httpx.AsyncClient(
        base_url=OPENBMCLAPI_METRIC,
        follow_redirects=True,
    ) as client:
        resp = await client.get("/dashboard")
        resp.raise_for_status()
    return type_validate_python(Summary, resp.json())


async def get_nodes_info() -> List[NodeInfo]:
    async with httpx.AsyncClient(
        base_url=OPENBMCLAPI_METRIC,
        follow_redirects=True,
    ) as client:
        resp = await client.get("/rank")
        resp.raise_for_status()
    return type_validate_python(List[NodeInfo], resp.json())
