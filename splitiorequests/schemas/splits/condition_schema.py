"""Split Definition's Rule's Condition Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from .matcher_schema import MatcherSchema
from splitiorequests.models.splits.condition import Condition


class ConditionSchema(Schema):
    """Condition schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    combiner = fields.Str(required=True)
    matchers = fields.List(fields.Nested(MatcherSchema), required=True)

    @post_load
    def load_condition(self, data, **kwargs):
        """Generates and returns Condition object"""
        return Condition(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
