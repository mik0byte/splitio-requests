"""Traffic Types endpoint classes

Requests and Response classes for Traffic Types endpoint
"""

import logging
from typing import Dict, Optional

from requests import Response, Session


log = logging.getLogger('splitiorequests')


class TrafficTypesResponse:
    """Traffic Type endpoint response"""
    def __init__(self, response: Response) -> None:
        """
        :param response: Request's response object
        """
        self.url = response.url
        self.status_code = response.status_code
        self.headers = response.headers
        self.json = response.json

    def __bool__(self):
        """Truthiness depends on response's status code"""
        if self.status_code == 200:
            return True
        else:
            return False


class TrafficTypesRequests:
    """Traffic Types endpoints"""
    def __init__(self, headers: Dict[str, str], hostname: str, session: Session) -> None:
        """
        :param headers: Headers to include in requests
        :param hostname: Split.io Admin API URL
        :param session: Session object
        """
        self.__hostname = f"{hostname}/trafficTypes"
        self.__headers = {**headers, **{'Content-Type': 'application/json'}}
        self.__session = session

    def __method_scope_headers_update(self, new_headers: Dict[str, str]) -> Dict[str, str]:
        """
        Allows to update request headers per endpoint

        :param new_headers: dictionary of new headers to append to existing ones
        :return: dictionary of headers
        """
        updated_headers = {**self.__headers, **new_headers}
        return updated_headers

    def get_traffic_types(self, wsid: str, headers: Optional[Dict[str, str]] = None) -> TrafficTypesResponse:
        """
        Get Traffic Types endpoint

        :param wsid: workspace ID
        :param headers: Headers to append to this request
        :return: TrafficTypesResponse object
        """
        log.info(f"Getting traffic types from '{wsid}' workspace")
        get_resp = self.__session.get(
            f'{self.__hostname}/ws/{wsid}',
            headers=self.__method_scope_headers_update(headers or {})
        )

        return TrafficTypesResponse(get_resp)
