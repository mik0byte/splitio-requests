"""Split Schema with exclude"""

from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from .tag_schema_exclude import TagSchemaExclude
from splitiorequests.models.splits.split import Split
from .traffic_type_schema_exclude import TrafficTypeSchemaExclude


class SplitSchemaExclude(Schema):
    """Split schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    name = fields.Str(required=True)
    description = fields.Str(load_default=None)
    trafficType = fields.Nested(TrafficTypeSchemaExclude)
    creationTime = fields.Integer()
    tags = fields.List(fields.Nested(TagSchemaExclude), load_default=None)

    @post_load
    def load_split(self, data, **kwargs):
        """Generates and returns Split object"""
        return Split(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if key != 'tags' and key != 'description' and data[key] is None):
            del new_data[field_key]
        return dict(new_data)
