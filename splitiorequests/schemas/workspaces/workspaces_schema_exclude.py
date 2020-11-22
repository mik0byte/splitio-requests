# -*- coding: utf-8 -*-
"""Workspaces Schema with exclude"""

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE

from .workspace_schema_exclude import WorkspaceSchemaExclude
from splitiorequests.models.workspaces.workspaces import Workspaces


class WorkspacesSchemaExclude(Schema):
    """Workspaces schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    objects = fields.List(fields.Nested(WorkspaceSchemaExclude), required=True)
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
