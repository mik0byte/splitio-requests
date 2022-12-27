"""Workspace Serializers"""

from typing import Optional

from splitiorequests.common.utils import Utils
from splitiorequests.models.workspaces.workspaces import Workspaces
from splitiorequests.schemas.workspaces.workspaces_schema import WorkspacesSchema
from splitiorequests.schemas.workspaces.workspaces_schema_exclude import WorkspacesSchemaExclude


def load_workspaces(data: dict, unknown_handler: str = 'RAISE') -> Optional[Workspaces]:
    """
    Workspaces dict data loader

    :param data: Workspaces data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Workspaces object
    """
    loaded_workspaces = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_workspaces = WorkspacesSchema().load(data)
    elif handler == "exclude":
        loaded_workspaces = WorkspacesSchemaExclude().load(data)
    return loaded_workspaces


def dump_workspaces(workspaces_obj: Workspaces) -> dict:
    """
    Dump Workspaces object into dictionary

    :param workspaces_obj: Workspaces object
    :return: Workspaces data dictionary
    """
    dumped_workspaces = WorkspacesSchema().dump(workspaces_obj)
    return dumped_workspaces
