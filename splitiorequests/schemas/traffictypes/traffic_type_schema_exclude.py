# -*- coding: utf-8 -*-
"""Traffic Type Schema with exclude"""

from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from splitiorequests.models.traffictypes.traffic_type import TrafficType


class TrafficTypeSchemaExclude(Schema):
    """TrafficType schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        ordered = True
        unknown = EXCLUDE

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
