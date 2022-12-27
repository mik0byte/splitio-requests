"""Split Definition's Rule Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.rule import Rule
from .bucket_schema_exclude import BucketSchemaExclude
from .condition_schema_exclude import ConditionSchemaExclude


class RuleSchemaExclude(Schema):
    """Rule schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    buckets = fields.List(fields.Nested(BucketSchemaExclude), required=True)
    condition = fields.Nested(ConditionSchemaExclude, required=True)

    @post_load
    def load_rule(self, data, **kwargs):
        """Generates and returns Rule object"""
        return Rule(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
