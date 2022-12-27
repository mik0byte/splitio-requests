"""Split Definitions Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from .split_definition_schema import SplitDefinitionSchema
from splitiorequests.models.splits.split_definitions import SplitDefinitions


class SplitDefinitionsSchema(Schema):
    """Split Definitions schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    objects = fields.List(fields.Nested(SplitDefinitionSchema), required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    totalCount = fields.Int(required=True)

    @post_load
    def load_split_definitions(self, data, **kwargs):
        """Generates and returns SplitDefinitions object"""
        return SplitDefinitions(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
