"""Between dataclass"""

from dataclasses import dataclass


@dataclass
class Between:
    """Split Definition's Rule's Condition's Matcher's Between model"""
    from_number: int
    to: int
