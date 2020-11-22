# -*- coding: utf-8 -*-
"""Split Definition's Rule's Condition's Matcher's Between Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.between import Between


class BetweenSchemaExclude(Schema):
    """Between schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    from_number = fields.Int(data_key='from', required=True)
    to = fields.Int(required=True)

    @post_load
    def load_between(self, data, **kwargs):
        """Generates and returns Between object"""
        return Between(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
