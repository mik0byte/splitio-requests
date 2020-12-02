# -*- coding: utf-8 -*-
"""Segment and Segment Keys Serializers"""

from typing import Optional

from splitiorequests.common.utils import Utils
from splitiorequests.models.segments.segment import Segment
from splitiorequests.models.segments.segment_keys import SegmentKeys
from splitiorequests.schemas.segments import (
    segment_schema, segment_schema_exclude,
    segment_keys_schema, segment_keys_schema_exclude
)


def load_segment(data: dict, unknown_handler: str = 'RAISE') -> Optional[Segment]:
    """
    Segment dict data loader

    :param data: Segment data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Segment object
    """
    loaded_segment = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_segment = segment_schema.SegmentSchema().load(data)
    elif handler == "exclude":
        loaded_segment = segment_schema_exclude.SegmentSchemaExclude().load(data)
    return loaded_segment


def dump_segment(segment_obj: Segment) -> dict:
    """
    Dump Segment object into dictionary

    :param segment_obj: Segment object
    :return: Segment data dictionary
    """
    dumped_segment = segment_schema.SegmentSchema().dump(segment_obj)
    return dumped_segment


def load_segment_keys(data: dict, unknown_handler: str = 'RAISE') -> Optional[SegmentKeys]:
    """
    Segment Keys dict data loader

    :param data: Segment Keys data
    :param unknown_handler: Include or Exclude unknown fields
    :return: Segment Keys object
    """
    loaded_segment_keys = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_segment_keys = segment_keys_schema.SegmentKeysSchema().load(data)
    elif handler == "exclude":
        loaded_segment_keys = segment_keys_schema_exclude.SegmentKeysSchemaExclude().load(data)
    return loaded_segment_keys


def dump_segment_keys(segment_keys_obj: SegmentKeys) -> dict:
    """
    Dump Segment Keys object into dictionary

    :param segment_keys_obj: Segment Keys object
    :return: Segment Keys data dictionary
    """
    dumped_segment_keys = segment_keys_schema.SegmentKeysSchema().dump(segment_keys_obj)
    return dumped_segment_keys
