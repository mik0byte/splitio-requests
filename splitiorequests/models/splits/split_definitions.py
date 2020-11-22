# -*- coding: utf-8 -*-
"""Split Definitions dataclass"""

from typing import List
from dataclasses import dataclass

from .split_definition import SplitDefinition


@dataclass
class SplitDefinitions:
    """Split Definitions model"""
    objects: List[SplitDefinition]
    offset: int
    limit: int
    totalCount: int
