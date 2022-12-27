"""Segment Keys dataclass"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SegmentKeys:
    """Segment Keys model"""
    keys: List[str]
    comment: Optional[str] = None
