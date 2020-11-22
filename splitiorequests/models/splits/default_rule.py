# -*- coding: utf-8 -*-
"""Default Rule dataclass"""

from dataclasses import dataclass


@dataclass
class DefaultRule:
    """Split definition's DefaultRule model"""
    treatment: str
    size: int
