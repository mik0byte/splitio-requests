# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import List

from .tag import Tag


@dataclass
class Tags:
    objects: List[Tag]
    offset: int
    limit: int
    totalCount: int
