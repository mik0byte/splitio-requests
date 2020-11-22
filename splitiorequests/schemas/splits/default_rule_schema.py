# -*- coding: utf-8 -*-
"""Split Definition's Default Rule Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from splitiorequests.models.splits.default_rule import DefaultRule


class DefaultRuleSchema(Schema):
    """DefaultRule schema class

    Raises exception when unknown field is detected
    """
    class Meta:
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
