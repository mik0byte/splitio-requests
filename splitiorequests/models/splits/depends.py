# -*- coding: utf-8 -*-
"""Depends dataclass"""

from typing import List
from dataclasses import dataclass


@dataclass
class Depends:
    """Split Definition's Rule's Condition's Matcher's Depends model"""
    splitName: str
    treatments: List[str]
