# -*- coding: utf-8 -*-
"""Split Definition's Treatment Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from splitiorequests.models.splits.treatment import Treatment


class TreatmentSchema(Schema):
    """Treatment schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    description = fields.Str()
    keys = fields.List(fields.Str())
    segments = fields.List(fields.Str())
    configurations = fields.Str()

    @post_load
    def load_treatment(self, data, **kwargs):
        """Generates and returns Treatment object"""
        return Treatment(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if data[key] is None):
            del new_data[field_key]
        return dict(new_data)
