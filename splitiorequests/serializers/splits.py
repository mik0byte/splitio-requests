"""Split Serializers"""

from typing import Optional

from splitiorequests.common.utils import Utils
from splitiorequests.models.splits.split import Split
from splitiorequests.models.splits.splits import Splits
from splitiorequests.schemas.splits.split_schema import SplitSchema
from splitiorequests.schemas.splits.splits_schema import SplitsSchema
from splitiorequests.models.splits.split_definition import SplitDefinition
from splitiorequests.models.splits.split_definitions import SplitDefinitions
from splitiorequests.schemas.splits.split_schema_exclude import SplitSchemaExclude
from splitiorequests.schemas.splits.splits_schema_exclude import SplitsSchemaExclude
from splitiorequests.schemas.splits.split_definition_schema import SplitDefinitionSchema
from splitiorequests.schemas.splits.split_definitions_schema import SplitDefinitionsSchema
from splitiorequests.schemas.splits.split_definition_schema_exclude import SplitDefinitionSchemaExclude
from splitiorequests.schemas.splits.split_definitions_schema_exclude import SplitDefinitionsSchemaExclude


def load_split(data: dict, unknown_handler: str = 'RAISE') -> Optional[Split]:
    """
    Split dict data loader

    :param data: Split data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Split object
    """
    loaded_split = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_split = SplitSchema().load(data)
    elif handler == "exclude":
        loaded_split = SplitSchemaExclude().load(data)
    return loaded_split


def dump_split(split_obj: Split) -> dict:
    """
    Dump Split object into dictionary

    :param split_obj: Split object
    :return: Split data dictionary
    """
    dumped_split = SplitSchema().dump(split_obj)
    return dumped_split


def load_splits(data: dict, unknown_handler: str = 'RAISE') -> Optional[Splits]:
    """
    Splits dict data loader

    :param data: Splits data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Splits object
    """
    loaded_splits = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_splits = SplitsSchema().load(data)
    elif handler == "exclude":
        loaded_splits = SplitsSchemaExclude().load(data)
    return loaded_splits


def dump_splits(split_obj: Splits) -> dict:
    """
    Dump Splits object into dictionary

    :param split_obj: Splits object
    :return: Splits data dictionary
    """
    dumped_splits = SplitsSchema().dump(split_obj)
    return dumped_splits


def load_split_definition(data: dict, unknown_handler: str = 'RAISE') -> Optional[SplitDefinition]:
    """
    Split Definition dict data loader

    :param data: Split Definition data
    :param unknown_handler: Include or Exclude unknown fields
    :return: SplitDefinition object
    """
    loaded_split_definition = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_split_definition = SplitDefinitionSchema().load(data)
    elif handler == "exclude":
        loaded_split_definition = SplitDefinitionSchemaExclude().load(data)
    return loaded_split_definition


def dump_split_definition(split_definition_obj: SplitDefinition) -> dict:
    """
    Dump Split Definition object into dictionary

    :param split_definition_obj: Split Definition object
    :return: Split Definition data dictionary
    """
    dumped_split_definition = SplitDefinitionSchema().dump(split_definition_obj)
    return dumped_split_definition


def load_split_definitions(data: dict, unknown_handler: str = 'RAISE') -> Optional[SplitDefinitions]:
    """
    Split Definitions dict data loader

    :param data: Split Definitions data
    :param unknown_handler: Include or Exclude unknown fields
    :return: SplitDefinitions object
    """
    loaded_split_definitions = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_split_definitions = SplitDefinitionsSchema().load(data)
    elif handler == "exclude":
        loaded_split_definitions = SplitDefinitionsSchemaExclude().load(data)
    return loaded_split_definitions


def dump_split_definitions(split_definitions_obj: SplitDefinitions) -> dict:
    """
    Dump Split Definitions object into dictionary

    :param split_definitions_obj: Split Definitions object
    :return: Split Definitions data dictionary
    """
    dumped_split_definitions = SplitDefinitionsSchema().dump(split_definitions_obj)
    return dumped_split_definitions
