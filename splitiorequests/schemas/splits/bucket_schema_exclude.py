# -*- coding: utf-8 -*-
"""Split Definition's Rule's Bucket Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.bucket import Bucket


class BucketSchemaExclude(Schema):
    """Bucket schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    treatment = fields.Str(required=True)
    size = fields.Int(required=True)

    @post_load
    def load_bucket(self, data, **kwargs):
        """Generates and returns Bucket object"""
        return Bucket(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
