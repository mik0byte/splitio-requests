from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from .split_schema_exclude import SplitSchemaExclude
from splitiorequests.models.splits.splits import Splits


class SplitsSchemaExclude(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    objects = fields.List(fields.Nested(SplitSchemaExclude), required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    totalCount = fields.Int(required=True)

    @post_load
    def load_split_definitions(self, data, **kwargs):
        return Splits(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        return dict(data)
