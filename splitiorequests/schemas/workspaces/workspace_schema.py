# -*- coding: utf-8 -*-
"""Workspace Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from splitiorequests.models.workspaces.workspace import Workspace


class WorkspaceSchema(Schema):
    """Workspace schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    wsid = fields.Str(required=True, data_key='id')

    @post_load
    def load_workspace(self, data, **kwargs):
        """Generates and returns Workspace object"""
        return Workspace(**data)

    @post_dump
    def return_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
