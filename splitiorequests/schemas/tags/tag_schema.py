# -*- coding: utf-8 -*-
"""Tag Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from splitiorequests.models.tags.tag import Tag


class TagSchema(Schema):
    """Tag schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    objectType = fields.Str(required=True)
    objectName = fields.Str(required=True)

    @post_load
    def load_tag(self, data, **kwargs):
        """Generates and returns Tag object"""
        return Tag(**data)

    @post_dump
    def return_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
