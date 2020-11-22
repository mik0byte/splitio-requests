# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass
class TrafficType:
    name: str
    traffic_type_id: str
    displayAttributeId: str
