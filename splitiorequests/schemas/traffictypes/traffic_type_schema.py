# -*- coding: utf-8 -*-
"""Traffic Type Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from splitiorequests.models.traffictypes.traffic_type import TrafficType


class TrafficTypeSchema(Schema):
    """TrafficType schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    traffic_type_id = fields.Str(required=True, data_key='id')
    displayAttributeId = fields.Str(required=True)

    @post_load
    def load_traffic_type(self, data, **kwargs):
        """Generates and returns TrafficType object"""
        return TrafficType(**data)

    @post_dump
    def return_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
