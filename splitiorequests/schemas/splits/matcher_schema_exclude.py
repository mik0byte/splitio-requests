"""Split Definition's Rule's Condition's Matcher Schema with exclude"""

from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from .between_schema_exclude import BetweenSchemaExclude
from .depends_schema_exclude import DependsSchemaExclude
from splitiorequests.models.splits.matcher import Matcher


class MatcherSchemaExclude(Schema):
    """Matcher schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    matcher_type = fields.Str(required=True, data_key='type')
    negate = fields.Bool()
    attribute = fields.Str()
    string = fields.Str()
    depends = fields.Nested(DependsSchemaExclude)
    strings = fields.List(fields.Str())
    date = fields.Int()
    between = fields.Nested(BetweenSchemaExclude)
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
