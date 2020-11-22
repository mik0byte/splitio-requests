# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass
class Tag:
    name: str
    objectType: str
    objectName: str
