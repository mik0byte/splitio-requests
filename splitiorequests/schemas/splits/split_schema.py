"""Split Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from .tag_schema import TagSchema
from .traffic_type_schema import TrafficTypeSchema
from splitiorequests.models.splits.split import Split


class SplitSchema(Schema):
    """Split schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    description = fields.Str()
    trafficType = fields.Nested(TrafficTypeSchema)
    creationTime = fields.Integer()
    tags = fields.List(fields.Nested(TagSchema), load_default=None)

    @post_load
    def load_split(self, data, **kwargs):
        """Generates and returns Split object"""
        return Split(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields

        Removes all empty keys except tags and description
        """
        new_data = data.copy()
        for field_key in (key for key in data if key != 'tags' and key != 'description' and data[key] is None):
            del new_data[field_key]
        return dict(new_data)
