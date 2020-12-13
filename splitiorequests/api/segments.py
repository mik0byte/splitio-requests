# -*- coding: utf-8 -*-
"""Segments endpoint classes

Requests and Response classes for Segments endpoint
"""

import os
import logging
from typing import Dict, Optional, Union, NoReturn, Iterator

from requests import Response, Session

log = logging.getLogger('splitiorequests')


class SegmentsResponse:
    """Segments endpoint response"""

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


class SegmentsRequests:
    """Segments endpoints"""

    def __init__(self, headers: Dict[str, str], hostname: str, session: Session) -> None:
        """
        :param headers: Headers to include in requests
        :param hostname: Split.io Admin API URL
        :param session: Session object
        """
        self.__hostname = f"{hostname}/segments"
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

    def create_segment(
            self,
            wsid: str,
            traffic_type_id_or_name: str,
            payload: dict,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Create Segment endpoint

        :param wsid: workspace ID
        :param traffic_type_id_or_name: traffic type's name or ID
        :param payload: New segment's payload
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Creating segment in '{wsid}' workspace with {traffic_type_id_or_name} traffic type")
        create_resp = self.__session.post(
            f'{self.__hostname}/ws/{wsid}/trafficTypes/{traffic_type_id_or_name}',
            headers=self.__method_scope_headers_update(headers or {}),
            json=payload
        )

        return SegmentsResponse(create_resp)

    def delete_segment(
            self,
            wsid: str,
            segment_name: str,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Delete Segment endpoint

        :param wsid: workspace ID
        :param segment_name: Name of the segment to delete
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Deleting segment from '{wsid}' workspace")
        delete_resp = self.__session.delete(
            f'{self.__hostname}/ws/{wsid}/{segment_name}',
            headers=self.__method_scope_headers_update(headers or {}),
        )

        return SegmentsResponse(delete_resp)

    def enable_segment_in_environment(
            self,
            environment_id: str,
            segment_name: str,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Enable Segment in Environment endpoint

        :param environment_id: ID of Environment
        :param segment_name: Name of the segment
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Enabling segment in '{environment_id}' environment")
        create_resp = self.__session.post(
            f'{self.__hostname}/{environment_id}/{segment_name}',
            headers=self.__method_scope_headers_update(headers or {}),
        )

        return SegmentsResponse(create_resp)

    def deactivate_segment_in_environment(
            self,
            environment_id: str,
            segment_name: str,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Deactivate Segment in Environment endpoint

        :param environment_id: ID of Environment
        :param segment_name: Name of the segment
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Deactivating segment from '{environment_id}' environment")
        delete_resp = self.__session.delete(
            f'{self.__hostname}/{environment_id}/{segment_name}',
            headers=self.__method_scope_headers_update(headers or {}),
        )

        return SegmentsResponse(delete_resp)

    def __list_segments_chunk(
            self,
            wsid: str,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Retrieving list of segments with specified parameters of pagination

        Will get only part of segments from workspace with specified limit and offset

        :param wsid: Workspace ID
        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Getting list of segments from '{wsid}' workspace - offset: '{offset}' - limit: '{limit}'")
        get_resp = self.__session.get(
            f'{self.__hostname}/ws/{wsid}?limit={limit}&offset={offset}',
            headers=self.__method_scope_headers_update(headers or {})
        )
        return SegmentsResponse(get_resp)

    def list_segments(
            self,
            wsid: str,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> Union[NoReturn, Iterator[SegmentsResponse]]:
        """
        List Segments endpoint

        Generator that yields all segments from specified workspace

        :param wsid: Workspace ID
        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        if limit < 1 or limit > 50:
            raise ValueError("Limit should be greater than or equal to 1 and less than or equal to 50")

        if offset < 0:
            raise ValueError("Offset should be greater than or equal to 0")

        segments = self.__list_segments_chunk(wsid, offset, limit, headers)
        if not segments:
            log.error(f"Couldn't get segments list from '{wsid}' workspace")
            yield segments
            return
        else:
            yield segments

        segments_json = segments.json()
        if segments_json['totalCount'] > segments_json['limit']:
            while segments_json['offset'] < segments_json['totalCount']:
                offset += limit
                segments = self.__list_segments_chunk(wsid, offset, limit)
                if not segments:
                    log.error(f"Couldn't get segments list from '{wsid}' workspace")
                    yield segments
                    return
                else:
                    yield segments
                segments_json = segments.json()

    def __list_segments_in_environment_chunk(
            self,
            wsid: str,
            environment_id_or_name: str,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Retrieving list of segments with specified parameters of pagination

        Will get only part of segments from environment with specified limit and offset

        :param wsid: Workspace ID
        :param environment_id_or_name: Environment ID or name
        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Getting list of segments from '{environment_id_or_name}' environment - offset: '{offset}' - "
                 f"limit: '{limit}'")
        get_resp = self.__session.get(
            f'{self.__hostname}/ws/{wsid}/environments/{environment_id_or_name}?limit={limit}&offset={offset}',
            headers=self.__method_scope_headers_update(headers or {})
        )
        return SegmentsResponse(get_resp)

    def list_segments_in_environment(
            self,
            wsid: str,
            environment_id_or_name: str,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> Union[NoReturn, Iterator[SegmentsResponse]]:
        """
        List Segments in Environment endpoint

        Generator that yields all segments from specified environment

        :param wsid: Workspace ID
        :param environment_id_or_name: Environment ID or name
        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        if limit < 1 or limit > 50:
            raise ValueError("Limit should be greater than or equal to 1 and less than or equal to 50")

        if offset < 0:
            raise ValueError("Offset should be greater than or equal to 0")

        segments = self.__list_segments_in_environment_chunk(wsid, environment_id_or_name, offset, limit, headers)
        if not segments:
            log.error(f"Couldn't get segments list from '{environment_id_or_name}' environment")
            yield segments
            return
        else:
            yield segments

        segments_json = segments.json()
        if segments_json['totalCount'] > segments_json['limit']:
            while segments_json['offset'] < segments_json['totalCount']:
                offset += limit
                segments = self.__list_segments_in_environment_chunk(wsid, environment_id_or_name, offset, limit)
                if not segments:
                    log.error(f"Couldn't get segments list from '{environment_id_or_name}' environment")
                    yield segments
                    return
                else:
                    yield segments
                segments_json = segments.json()

    def update_segment_keys_in_environment_via_csv(
            self,
            environment_id: str,
            segment_name: str,
            csv_file_path: str,
            csv_file_name: str,
            replace: bool = False,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Update Segment Keys in Environment via CSV endpoint

        :param environment_id: ID of Environment
        :param segment_name: Name of the segment
        :param csv_file_path: Absolute path of segment keys CSV file in string format(Shouldn't include file name)
        :param csv_file_name: Name of CSV file
        :param replace: Should existing keys be replaced
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        files = [('file', (csv_file_name, open(os.path.join(csv_file_path, csv_file_name), 'rb'), 'text/csv'))]
        log.info(f"Updating segment keys in '{environment_id}' environment with CSV file")
        update_resp = self.__session.put(
            f'{self.__hostname}/{environment_id}/{segment_name}/upload?replace={replace}',
            headers=self.__method_scope_headers_update(headers or {}),
            files=files
        )

        return SegmentsResponse(update_resp)

    def update_segment_keys_in_environment_via_json(
            self,
            environment_id: str,
            segment_name: str,
            payload: dict,
            replace: bool = False,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Update Segment Keys in Environment via JSON endpoint

        :param environment_id: ID of Environment
        :param segment_name: Name of the segment
        :param payload: Keys payload to add to the segment
        :param replace: Should existing keys be replaced
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Updating segment keys in '{environment_id}' environment with JSON")
        update_resp = self.__session.put(
            f'{self.__hostname}/{environment_id}/{segment_name}/uploadKeys?replace={replace}',
            headers=self.__method_scope_headers_update(headers or {}),
            json=payload
        )

        return SegmentsResponse(update_resp)

    def __get_segment_keys_in_environment_chunk(
            self,
            environment_id: str,
            segment_name: str,
            offset: int = 0,
            limit: int = 50,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Retrieving list of segments keys with specified parameters of pagination

        Will get only part of segments keys from environment with specified limit and offset

        :param environment_id: Environment ID
        :param segment_name: Name of segment
        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Getting list of segments keys from '{environment_id}' environment - offset: '{offset}' - "
                 f"limit: '{limit}'")
        get_resp = self.__session.get(
            f'{self.__hostname}/{environment_id}/{segment_name}/keys?limit={limit}&offset={offset}',
            headers=self.__method_scope_headers_update(headers or {})
        )
        return SegmentsResponse(get_resp)

    def get_segment_keys_in_environment(
            self,
            environment_id: str,
            segment_name: str,
            offset: int = 0,
            limit: int = 100,
            headers: Optional[Dict[str, str]] = None
    ) -> Union[NoReturn, Iterator[SegmentsResponse]]:
        """
        Get Segment Keys in Environment endpoint

        :param environment_id: ID of Environment
        :param segment_name: Name of the segment
        :param offset: Pagination offset parameter
        :param limit: Pagination limit parameter
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        if limit < 1 or limit > 100:
            raise ValueError("Limit should be greater than or equal to 1 and less than or equal to 50")

        if offset < 0:
            raise ValueError("Offset should be greater than or equal to 0")

        segment_keys = self.__get_segment_keys_in_environment_chunk(environment_id, segment_name, offset,
                                                                    limit, headers)
        if not segment_keys:
            log.error(f"Couldn't get segment keys list from '{environment_id}' environment")
            yield segment_keys
            return
        else:
            yield segment_keys

        segment_keys_json = segment_keys.json()
        if segment_keys_json['count'] > segment_keys_json['limit']:
            while segment_keys_json['offset'] < segment_keys_json['count']:
                offset += limit
                segment_keys = self.__get_segment_keys_in_environment_chunk(environment_id, segment_name, offset,
                                                                            limit, headers)
                if not segment_keys:
                    log.error(f"Couldn't get segment keys list from '{environment_id}' environment")
                    yield segment_keys
                    return
                else:
                    yield segment_keys
                segment_keys_json = segment_keys.json()

    def remove_segment_keys_from_environment(
            self,
            environment_id: str,
            segment_name: str,
            payload: dict,
            headers: Optional[Dict[str, str]] = None
    ) -> SegmentsResponse:
        """
        Remove Segment Keys from Environment endpoint

        :param environment_id: ID of Environment
        :param segment_name: Name of the segment
        :param payload: List of keys to remove
        :param headers: Headers to append to this request
        :return: SegmentsResponse object
        """
        log.info(f"Removing segment keys from '{environment_id}' environment")
        del_resp = self.__session.put(
            f'{self.__hostname}/{environment_id}/{segment_name}/removeKeys',
            headers=self.__method_scope_headers_update(headers or {}),
            json=payload
        )

        return SegmentsResponse(del_resp)
