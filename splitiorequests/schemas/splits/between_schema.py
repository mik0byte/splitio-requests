# -*- coding: utf-8 -*-
"""Split Definition's Rule's Matcher's Between Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from splitiorequests.models.splits.between import Between


class BetweenSchema(Schema):
    """Between schema class

    Raises exception when unknown field is detected
    """
    class Meta:
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
