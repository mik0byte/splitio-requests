# -*- coding: utf-8 -*-
"""Split Definition's Rule's Matcher Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from .between_schema import BetweenSchema
from .depends_schema import DependsSchema
from splitiorequests.models.splits.matcher import Matcher


class MatcherSchema(Schema):
    """Matcher schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    matcher_type = fields.Str(required=True, data_key='type')
    negate = fields.Bool()
    attribute = fields.Str()
    string = fields.Str()
    depends = fields.Nested(DependsSchema)
    strings = fields.List(fields.Str())
    date = fields.Int()
    between = fields.Nested(BetweenSchema)
    number = fields.Int()
    bool = fields.Bool()

    @post_load
    def load_matcher(self, data, **kwargs):
        """Generates and returns Matcher object"""
        return Matcher(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if data[key] is None):
            del new_data[field_key]
        return dict(new_data)
