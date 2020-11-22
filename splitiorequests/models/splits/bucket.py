# -*- coding: utf-8 -*-
"""Bucket dataclass"""

from dataclasses import dataclass


@dataclass
class Bucket:
    """Split Definition's Rule's Bucket model"""
    treatment: str
    size: int
