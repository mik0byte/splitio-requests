# -*- coding: utf-8 -*-
"""Environment Serializers"""

from typing import Optional, List, Dict, Union

from splitiorequests.common.utils import Utils
from splitiorequests.models.environments.environment import Environment
from splitiorequests.schemas.environments import environment_schema, environment_schema_exclude


def load_environment(data: dict, unknown_handler: str = 'RAISE') -> Optional[Environment]:
    """
    Environment dict data loader

    :param data: Environment data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Environment object
    """
    loaded_environment = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_environment = environment_schema.EnvironmentSchema().load(data)
    elif handler == "exclude":
        loaded_environment = environment_schema_exclude.EnvironmentSchemaExclude().load(data)
    return loaded_environment


def dump_environment(environment_obj: Environment) -> dict:
    """
    Dump Environment object into dictionary

    :param environment_obj: Environment object
    :return: Environment data dictionary
    """
    dumped_environment = environment_schema.EnvironmentSchema().dump(environment_obj)
    return dumped_environment


def load_environments(
        data: List[Dict[str, Union[str, bool]]],
        unknown_handler: str = 'RAISE'
) -> Optional[List[Environment]]:
    """
    Environments dict data loader

    :param data: Environments data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Environments object
    """
    loaded_environments = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_environments = environment_schema.EnvironmentSchema(many=True).load(data)
    elif handler == "exclude":
        loaded_environments = environment_schema_exclude.EnvironmentSchemaExclude(many=True).load(data)
    return loaded_environments


def dump_environments(environments_obj: List[Environment]) -> dict:
    """
    Dump Environments object into dictionary

    :param environments_obj: Environments object
    :return: Environments data dictionary
    """
    dumped_environments = environment_schema.EnvironmentSchema(many=True).dump(environments_obj)
    return dumped_environments
