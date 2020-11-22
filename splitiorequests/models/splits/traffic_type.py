# -*- coding: utf-8 -*-
"""Traffic Type dataclass"""


from dataclasses import dataclass


@dataclass
class TrafficType:
    """Traffic Type model"""
    name: str
    traffic_id: str
