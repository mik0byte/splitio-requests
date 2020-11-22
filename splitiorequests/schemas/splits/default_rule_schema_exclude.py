# -*- coding: utf-8 -*-
"""Split Definition's Default Rule Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.default_rule import DefaultRule


class DefaultRuleSchemaExclude(Schema):
    """DefaultRule schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    treatment = fields.Str(required=True)
    size = fields.Int(required=True)

    @post_load
    def load_default_rule(self, data, **kwargs):
        """Generates and returns DefaultRule object"""
        return DefaultRule(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
