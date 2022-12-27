"""Workspaces endpoint classes

Requests and Response classes for Workspaces endpoint
"""

import logging
from typing import Dict, Optional, Union, NoReturn, Iterator

from requests import Response, Session


log = logging.getLogger('splitiorequests')


class WorkspacesResponse:
    """Workspace endpoint response"""
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


class WorkspacesRequests:
    """Workspaces endpoints"""
    def __init__(self, headers: Dict[str, str], hostname: str, session: Session) -> None:
        """
        :param headers: Headers to include in requests
        :param hostname: Split.io Admin API URL
        :param session: Session object
        """
        self.__hostname = f"{hostname}/workspaces"
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

    def __list_workspaces_chunk(
            self,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> WorkspacesResponse:
        """
        Retrieving list of workspaces with specified parameters of pagination

        Will get only part of workspaces with specified limit and offset

        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: WorkspacesResponse object
        """
        log.info("Getting workspaces")
        get_resp = self.__session.get(
            f'{self.__hostname}?limit={limit}&offset={offset}',
            headers=self.__method_scope_headers_update(headers or {})
        )

        return WorkspacesResponse(get_resp)

    def get_workspaces(
            self,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> Union[NoReturn, Iterator[WorkspacesResponse]]:
        """
        Get Workspaces endpoint

        Generator that yields all workspaces

        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: WorkspacesResponse
        """
        if limit < 1 or limit > 50:
            raise ValueError("Limit should be greater than or equal to 1 and less than or equal to 50")

        if offset < 0:
            raise ValueError("Offset should be greater than or equal to 0")

        workspaces = self.__list_workspaces_chunk(offset, limit, headers)

        if not workspaces:
            log.error("Couldn't get workspaces")
            yield workspaces
            return
        else:
            yield workspaces

        workspaces_payload = workspaces.json()
        if workspaces_payload['totalCount'] > workspaces_payload['limit']:
            while workspaces_payload['offset'] < workspaces_payload['totalCount']:
                offset += limit
                workspaces = self.__list_workspaces_chunk(offset, limit, headers)
                if workspaces is None:
                    log.error("Couldn't get workspaces")
                    yield workspaces
                    return
                else:
                    yield workspaces
                workspaces_payload = workspaces.json()
