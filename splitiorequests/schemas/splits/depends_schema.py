# -*- coding: utf-8 -*-
"""Split Definition's Rule's Matcher's Depends Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from splitiorequests.models.splits.depends import Depends


class DependsSchema(Schema):
    """Depends schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    splitName = fields.Str(required=True)
    treatments = fields.List(fields.Str(), required=True)

    @post_load
    def load_depends(self, data, **kwargs):
        """Generates and returns Depends object"""
        return Depends(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
