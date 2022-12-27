"""Matcher dataclass"""

from dataclasses import dataclass
from typing import List, Optional

from .depends import Depends
from .between import Between


@dataclass
class Matcher:
    """Split Definition's Rule's Condition's Matcher model"""
    matcher_type: str
    string: Optional[str] = None
    negate: Optional[bool] = None
    depends: Optional[Depends] = None
    attribute: Optional[str] = None
    strings: Optional[List[str]] = None
    date: Optional[int] = None
    between: Optional[Between] = None
    number: Optional[int] = None
    bool: Optional[bool] = None
