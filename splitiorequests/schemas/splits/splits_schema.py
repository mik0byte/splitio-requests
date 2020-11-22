# -*- coding: utf-8 -*-


from marshmallow import Schema, fields, post_load, post_dump

from .split_schema import SplitSchema
from splitiorequests.models.splits.splits import Splits


class SplitsSchema(Schema):
    class Meta:
        ordered = True

    objects = fields.List(fields.Nested(SplitSchema), required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    totalCount = fields.Int(required=True)

    @post_load
    def load_split_definitions(self, data, **kwargs):
        return Splits(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        return dict(data)
