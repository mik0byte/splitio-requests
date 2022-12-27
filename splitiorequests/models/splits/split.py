"""Split dataclass"""


from dataclasses import dataclass
from typing import List, Optional

from .traffic_type import TrafficType
from .tag import Tag


@dataclass
class Split:
    """Split model"""
    name: str
    description: str = ''
    trafficType: Optional[TrafficType] = None
    creationTime: Optional[int] = None
    tags: Optional[List[Tag]] = None
