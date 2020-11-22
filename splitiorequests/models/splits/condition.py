# -*- coding: utf-8 -*-
"""Condition dataclass"""

from typing import List
from dataclasses import dataclass

from .matcher import Matcher


@dataclass
class Condition:
    """Split Definition's Rule's Condition model"""
    combiner: str
    matchers: List[Matcher]
