# -*- coding: utf-8 -*-
"""Rule dataclass"""

from typing import List
from dataclasses import dataclass

from .bucket import Bucket
from .condition import Condition


@dataclass
class Rule:
    """Split Definition's Rule model"""
    buckets: List[Bucket]
    condition: Condition
