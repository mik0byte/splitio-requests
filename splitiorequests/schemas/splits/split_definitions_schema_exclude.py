"""Split Definitions Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from .split_definition_schema_exclude import SplitDefinitionSchemaExclude
from splitiorequests.models.splits.split_definitions import SplitDefinitions


class SplitDefinitionsSchemaExclude(Schema):
    """SplitDefinitions schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    objects = fields.List(fields.Nested(SplitDefinitionSchemaExclude), required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    totalCount = fields.Int(required=True)

    @post_load
    def load_split_definitions(self, data, **kwargs):
        """Generates and returns SplitDefinitions object"""
        return SplitDefinitions(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
