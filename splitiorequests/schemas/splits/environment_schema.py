"""Split Definition's Environment Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from splitiorequests.models.splits.environment import Environment


class EnvironmentSchema(Schema):
    """Environment schema class

    Raises exception when unknown field is detected
    """
    class Meta:
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
