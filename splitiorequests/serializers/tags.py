# -*- coding: utf-8 -*-
"""Tag Serializers"""

from typing import Optional, List, Dict

from splitiorequests.common.utils import Utils
from splitiorequests.models.tags.tags import Tags
from splitiorequests.schemas.tags import tags_schema, tags_schema_exclude


def load_tags(data: List[Dict[str, str]], unknown_handler: str = 'RAISE') -> Optional[List[Tags]]:
    """
    Tags dict data loader

    :param data: Tags data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Tags object
    """
    loaded_tags = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_tags = tags_schema.TagsSchema().load(data)
    elif handler == "exclude":
        loaded_tags = tags_schema_exclude.TagsSchemaExclude().load(data)
    return loaded_tags


def dump_tags(tags_obj: List[Tags]) -> dict:
    """
    Dump Tags object into dictionary

    :param tags_obj: Tags object
    :return: Tags data dictionary
    """
    dumped_tags = tags_schema.TagsSchema().dump(tags_obj)
    return dumped_tags
