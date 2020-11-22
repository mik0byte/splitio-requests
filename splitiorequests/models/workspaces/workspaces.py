# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import List

from .workspace import Workspace


@dataclass
class Workspaces:
    objects: List[Workspace]
    offset: int
    limit: int
    totalCount: int
