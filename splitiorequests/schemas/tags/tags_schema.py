# -*- coding: utf-8 -*-
"""Tags Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from .tag_schema import TagSchema
from splitiorequests.models.tags.tags import Tags


class TagsSchema(Schema):
    """Tags schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    objects = fields.List(fields.Nested(TagSchema), required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    totalCount = fields.Int(required=True)

    @post_load
    def load_tags(self, data, **kwargs):
        """Generates and returns Tags object"""
        return Tags(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
