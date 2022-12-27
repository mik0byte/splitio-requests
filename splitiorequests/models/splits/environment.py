"""Split Definition's Environment dataclass"""

from dataclasses import dataclass


@dataclass
class Environment:
    """Split Definition's Environment model"""
    environment_id: str
    name: str
