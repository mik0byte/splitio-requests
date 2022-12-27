"""Environment Schema with exclude"""


from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from splitiorequests.models.environments.environment import Environment


class EnvironmentSchemaExclude(Schema):
    """Environment schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        ordered = True
        unknown = EXCLUDE

    name = fields.Str(required=True)
    id = fields.Str(required=True)
    production = fields.Bool(required=True)
    orgId = fields.Str(load_default=None)
    status = fields.Str(load_default=None)
    workspaceIds = fields.List(fields.Str(), load_default=None)
    creationTime = fields.Int(load_default=None)
    permissioningEnabled = fields.Bool(load_default=None)
    segments = fields.List(fields.Str(), load_default=None)
    tests = fields.List(fields.Str(), load_default=None)
    apiTokens = fields.List(fields.Str(), load_default=None)
    workspaces = fields.List(fields.Str(), load_default=None)
    integrations = fields.List(fields.Str(), load_default=None)
    permissions = fields.List(fields.Str(), load_default=None)
    settings = fields.List(fields.Str(), load_default=None)

    @post_load
    def load_environment(self, data, **kwargs):
        """Generates and returns Environment object"""
        return Environment(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if data[key] is None):
            del new_data[field_key]
        return dict(new_data)
