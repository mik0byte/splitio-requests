# -*- coding: utf-8 -*-
"""Split Definition Schema"""

from marshmallow import Schema, fields, post_dump, post_load

from .rule_schema import RuleSchema
from .treatment_schema import TreatmentSchema
from .environment_schema import EnvironmentSchema
from .traffic_type_schema import TrafficTypeSchema
from .default_rule_schema import DefaultRuleSchema
from splitiorequests.models.splits.split_definition import SplitDefinition


class SplitDefinitionSchema(Schema):
    """Split Definition schema class

    Raises exception when unknown field is detected
    """
    class Meta:
        ordered = True

    name = fields.Str()
    environment = fields.Nested(EnvironmentSchema)
    trafficType = fields.Nested(TrafficTypeSchema)
    killed = fields.Bool()
    treatments = fields.List(fields.Nested(TreatmentSchema), required=True)
    defaultTreatment = fields.Str(required=True)
    baselineTreatment = fields.Str()
    trafficAllocation = fields.Int()
    rules = fields.List(fields.Nested(RuleSchema))
    defaultRule = fields.List(fields.Nested(DefaultRuleSchema), required=True)
    creationTime = fields.Int()
    lastUpdateTime = fields.Int()
    comment = fields.Str()

    @post_load
    def load_split_definition(self, data, **kwargs):
        """Generates and returns SplitDefinition object"""
        return SplitDefinition(**data)

    @post_dump
    def clean_empty(self, data, **kwargs):
        """Converts Schema object into dictionary and removes empty fields"""
        new_data = data.copy()
        for field_key in (key for key in data if data[key] is None):
            del new_data[field_key]
        return dict(new_data)
