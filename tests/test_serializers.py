import pytest
import marshmallow

from splitiorequests.serializers import (
    load_split, load_splits, load_split_definition, load_split_definitions,
    load_environment, load_environments, load_workspaces, load_traffic_types,
    load_tags
)


class TestSerializers:
    def test_load_split_exclude_unknown(self, splits):
        load_split(splits['objects'][0], unknown_handler='EXCLUDE')

    def test_load_split_raise_unknown(self, splits):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_split(splits['objects'][0])

    def test_load_splits_exclude_unknown(self, splits):
        load_splits(splits, unknown_handler='EXCLUDE')

    def test_load_splits_raise_unknown(self, splits):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_splits(splits)

    def test_load_split_definition_exclude_unknown(self, split_definitions):
        load_split_definition(split_definitions['objects'][0], unknown_handler='EXCLUDE')

    def test_load_split_definition_raise_unknown(self, split_definitions):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_split_definition(split_definitions['objects'][0])

    def test_load_split_definitions_exclude_unknown(self, split_definitions):
        load_split_definitions(split_definitions, unknown_handler='EXCLUDE')

    def test_load_split_definitions_raise_unknown(self, split_definitions):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_split_definitions(split_definitions)

    def test_load_environment_raise_unknown(self, environments):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_environment(environments['environment']['with_unknown'])

    def test_load_environment_exclude_unknown(self, environments):
        load_environment(environments['environment']['with_unknown'], unknown_handler='EXCLUDE')

    def test_load_environments_raise_unknown(self, environments):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_environments(environments['environments']['with_unknown'])

    def test_load_environments_exclude_unknown(self, environments):
        load_environments(environments['environments']['with_unknown'], unknown_handler='EXCLUDE')

    def test_load_workspaces_raise_unknown(self, workspaces):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_workspaces(workspaces)

    def test_workspaces_exclude_unknown(self, workspaces):
        load_workspaces(workspaces, unknown_handler='EXCLUDE')

    def test_load_traffic_types_raise_unknown(self, traffic_types):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_traffic_types(traffic_types['with_unknown'])

    def test_load_traffic_types_exclude_unknown(self, traffic_types):
        load_traffic_types(traffic_types['with_unknown'], unknown_handler='EXCLUDE')

    def test_load_tags_raise_unknown(self, tags):
        with pytest.raises(marshmallow.exceptions.ValidationError):
            load_tags(tags)

    def test_load_tags_exclude_unknown(self, tags):
        load_tags(tags, unknown_handler='EXCLUDE')
