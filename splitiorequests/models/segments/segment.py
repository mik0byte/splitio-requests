# -*- coding: utf-8 -*-
"""Segment dataclass"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Segment:
    """Segment model"""
    name: str
    description: Optional[str] = None
