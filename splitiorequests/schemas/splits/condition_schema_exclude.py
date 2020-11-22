# -*- coding: utf-8 -*-
"""Split Definition's Rule's Condition Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from .matcher_schema_exclude import MatcherSchemaExclude
from splitiorequests.models.splits.condition import Condition


class ConditionSchemaExclude(Schema):
    """Condition schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    combiner = fields.Str(required=True)
    matchers = fields.List(fields.Nested(MatcherSchemaExclude), required=True)

    @post_load
    def load_condition(self, data, **kwargs):
        """Generates and returns Condition object"""
        return Condition(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
