# -*- coding: utf-8 -*-
"""Segment Schema with exclude"""

from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from splitiorequests.models.segments.segment import Segment


class SegmentSchemaExclude(Schema):
    """Segment schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        ordered = True
        unknown = EXCLUDE

    name = fields.Str(required=True)
    description = fields.Str(missing=None)

    @post_load
    def load_segment(self, data, **kwargs):
        """Generates and returns Segment object"""
        return Segment(**data)

    @post_dump
    def return_dict(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if data[key] is None):
            del new_data[field_key]
        return dict(new_data)
