# -*- coding: utf-8 -*-
"""Tags Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from .tag_schema_exclude import TagSchemaExclude
from splitiorequests.models.tags.tags import Tags


class TagsSchemaExclude(Schema):
    """Tags schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        ordered = True
        unknown = EXCLUDE

    objects = fields.List(fields.Nested(TagSchemaExclude), required=True)
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
