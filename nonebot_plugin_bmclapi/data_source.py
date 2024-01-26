from typing import List

import httpx
from pydantic import parse_obj_as

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
    return parse_obj_as(Summary, resp.json())


async def get_nodes_info() -> List[NodeInfo]:
    async with httpx.AsyncClient(
        base_url=OPENBMCLAPI_METRIC,
        follow_redirects=True,
    ) as client:
        resp = await client.get("/rank")
        resp.raise_for_status()
    return parse_obj_as(List[NodeInfo], resp.json())
