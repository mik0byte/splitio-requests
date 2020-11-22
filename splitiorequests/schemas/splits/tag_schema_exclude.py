# -*- coding: utf-8 -*-
"""Tag Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.tag import Tag


class TagSchemaExclude(Schema):
    """Tag schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
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
