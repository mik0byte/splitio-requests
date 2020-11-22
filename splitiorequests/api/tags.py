# -*- coding: utf-8 -*-
"""Tags endpoint classes

Requests and Response classes for Tags endpoint
"""

import logging
from typing import Dict, Optional, List

from requests import Response, Session


log = logging.getLogger('splitiorequests')


class TagsResponse:
    """Tag endpoint response"""
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


class TagsRequests:
    """Tags endpoints"""
    def __init__(self, headers: Dict[str, str], hostname: str, session: Session) -> None:
        """
        :param headers: Headers to include in requests
        :param hostname: Split.io Admin API URL
        :param session: Session object
        """
        self.__hostname = f"{hostname}/tags"
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

    def associate_tags(
            self,
            wsid: str,
            object_name: str,
            object_type: str,
            payload: List[str],
            headers: Optional[Dict[str, str]] = None
    ) -> TagsResponse:
        """
        Associate Tags endpoint

        :param wsid: workspace ID
        :param object_name: Name of object(split) to associate tags with
        :param object_type: Currently only 'Split' obejct is supported
        :param payload: Tags list payload
        :param headers: Headers to append to this request
        :return: TagsResponse object
        """
        if object_type != 'Split':
            raise ValueError("Currently only supported object type: Split")

        log.info(f"Associating tags with '{object_name}' '{object_type}' in '{wsid}' workspace")
        post_resp = self.__session.post(
            f'{self.__hostname}/ws/{wsid}/object/{object_name}/objecttype/{object_type}',
            headers=self.__method_scope_headers_update(headers or {}),
            json=payload
        )

        return TagsResponse(post_resp)
