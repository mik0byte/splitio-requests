"""Workspaces Schema"""

from marshmallow import Schema, fields, post_load, post_dump

from .workspace_schema import WorkspaceSchema
from splitiorequests.models.workspaces.workspaces import Workspaces


class WorkspacesSchema(Schema):
    """Workspaces schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    objects = fields.List(fields.Nested(WorkspaceSchema), required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    totalCount = fields.Int(required=True)

    @post_load
    def load_split_definitions(self, data, **kwargs):
        """Generates and returns Workspaces object"""
        return Workspaces(**data)

    @post_dump
    def convert_to_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
