"""TrafficType Serializers"""

from typing import Optional, List, Dict

from splitiorequests.common.utils import Utils
from splitiorequests.models.traffictypes.traffic_type import TrafficType
from splitiorequests.schemas.traffictypes import traffic_type_schema, traffic_type_schema_exclude


def load_traffic_types(data: List[Dict[str, str]], unknown_handler: str = 'RAISE') -> Optional[List[TrafficType]]:
    """
    TrafficType dict data loader

    :param data: TrafficType data
    :param unknown_handler: Include or Exclude unknown fields
    :return: TrafficType object
    """
    loaded_traffic_types = None
    handler = Utils.get_unknown_field_handler(unknown_handler)
    if handler == "raise":
        loaded_traffic_types = traffic_type_schema.TrafficTypeSchema(many=True).load(data)
    elif handler == "exclude":
        loaded_traffic_types = traffic_type_schema_exclude.TrafficTypeSchemaExclude(many=True).load(data)
    return loaded_traffic_types


def dump_traffic_types(traffic_types_obj: List[TrafficType]) -> dict:
    """
    Dump TrafficType object into dictionary

    :param traffic_types_obj: TrafficType object
    :return: TrafficType data dictionary
    """
    dumped_traffic_types = traffic_type_schema.TrafficTypeSchema(many=True).dump(traffic_types_obj)
    return dumped_traffic_types
