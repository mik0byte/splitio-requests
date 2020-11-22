# -*- coding: utf-8 -*-
"""Split Definition's Environment Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from splitiorequests.models.splits.environment import Environment


class EnvironmentSchemaExclude(Schema):
    """Environment schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    environment_id = fields.Str(data_key='id', required=True)
    name = fields.Str(required=True)

    @post_load
    def load_environment(self, data, **kwargs):
        """Generates and returns Environment object"""
        return Environment(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
