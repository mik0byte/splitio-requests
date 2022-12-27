"""Split Definition dataclass"""

from dataclasses import dataclass
from typing import Optional, List

from .rule import Rule
from .treatment import Treatment
from .environment import Environment
from .default_rule import DefaultRule
from .traffic_type import TrafficType


@dataclass
class SplitDefinition:
    """Split Definition model"""
    treatments: List[Treatment]
    defaultTreatment: str
    defaultRule: List[DefaultRule]
    name: Optional[str] = None
    environment: Optional[Environment] = None
    trafficType: Optional[TrafficType] = None
    killed: Optional[bool] = None
    baselineTreatment: Optional[str] = None
    trafficAllocation: Optional[int] = None
    rules: Optional[List[Rule]] = None
    creationTime: Optional[int] = None
    lastUpdateTime: Optional[int] = None
    comment: Optional[str] = None
