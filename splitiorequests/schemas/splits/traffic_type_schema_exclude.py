"""Traffic Type Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.traffic_type import TrafficType


class TrafficTypeSchemaExclude(Schema):
    """TrafficType schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    traffic_id = fields.Str(required=True, data_key='id')
    name = fields.Str(required=True)

    @post_load
    def load_traffic_type(self, data, **kwargs):
        """Generates and returns TrafficType object"""
        return TrafficType(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
