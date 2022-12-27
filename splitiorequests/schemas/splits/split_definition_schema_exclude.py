"""Split Definition Schema with exclude"""

from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from .rule_schema_exclude import RuleSchemaExclude
from .treatment_schema_exclude import TreatmentSchemaExclude
from .environment_schema_exclude import EnvironmentSchemaExclude
from .traffic_type_schema_exclude import TrafficTypeSchemaExclude
from .default_rule_schema_exclude import DefaultRuleSchemaExclude
from splitiorequests.models.splits.split_definition import SplitDefinition


class SplitDefinitionSchemaExclude(Schema):
    """SplitDefinition schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        unknown = EXCLUDE
        ordered = True

    name = fields.Str()
    environment = fields.Nested(EnvironmentSchemaExclude)
    trafficType = fields.Nested(TrafficTypeSchemaExclude)
    killed = fields.Bool()
    treatments = fields.List(fields.Nested(TreatmentSchemaExclude), required=True)
    defaultTreatment = fields.Str(required=True)
    baselineTreatment = fields.Str()
    trafficAllocation = fields.Int()
    rules = fields.List(fields.Nested(RuleSchemaExclude))
    defaultRule = fields.List(fields.Nested(DefaultRuleSchemaExclude), required=True)
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
