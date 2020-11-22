# -*- coding: utf-8 -*-
"""Tag Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from splitiorequests.models.splits.tag import Tag


class TagSchema(Schema):
    """Tag schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str(required=True)

    @post_load
    def load_tag(self, data, **kwargs):
        """Generates and returns Tag object"""
        return Tag(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
