# -*- coding: utf-8 -*-
"""Split Definition's Rule's Bucket Schema"""


from marshmallow import Schema, fields, post_load, post_dump

from splitiorequests.models.splits.bucket import Bucket


class BucketSchema(Schema):
    """Bucket schema class

    Raises exception when unknown field is detected
    """
    class Meta:
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
