"""Segment Keys Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from splitiorequests.models.segments.segment_keys import SegmentKeys


class SegmentKeysSchema(Schema):
    """Segment Keys schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    keys = fields.List(fields.Str(), required=True)
    comment = fields.Str(load_default=None)

    @post_load
    def load_segment_keys(self, data, **kwargs):
        """Generates and returns Segment Keys object"""
        return SegmentKeys(**data)

    @post_dump
    def return_dict(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if data[key] is None):
            del new_data[field_key]
        return dict(new_data)
