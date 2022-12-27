"""AdminAPI class

Main class for interacting with Split.io public API.
"""

from abc import ABC
from typing import Optional, Dict, Tuple, NoReturn, Union

from requests import Session
from urllib3.util.retry import Retry

from .tags import TagsRequests
from .splits import SplitsRequests
from .segments import SegmentsRequests
from .workspaces import WorkspacesRequests
from .environments import EnvironmentsRequests
from .traffic_types import TrafficTypesRequests
from ..common.http_adapter import TimeoutHTTPAdapter


class APIRequestsBase(ABC):
    """Abstract API requests class"""
    def __init__(
            self,
            token: str,
            hostname: Optional[str] = None
    ) -> None:
        self._hostname = hostname or 'https://api.split.io/internal/api/v2'
        self._headers = {'Authorization': f"Bearer {token}"}

    def _super_session(
            self,
            retries: int,
            backoff_factor: float,
            status_forcelist: Tuple[int, ...],
            session: Optional[Session]
    ) -> Union[NoReturn, Session]:
        """Creates session with wait and backoff factor mechanism"""
        raise NotImplementedError


class AdminAPI(APIRequestsBase):
    """Main class to interact with Split.io admin API"""
    def __init__(
            self,
            token: str,
            headers: Optional[Dict[str, str]] = None,
            hostname: Optional[str] = None,
            retries: int = 10,
            backoff_factor: float = 0.3,
            status_forcelist=(429, 500, 502, 503, 504),
            session: Optional[Session] = None,
    ) -> None:
        """
        :param token: Split.io admin API token
        :param headers: Headers to be included during API requests
        :param hostname: Split.io Admin API URL
        :param retries: Number of retries during request failures
        :param backoff_factor: Backoff factor number to be used for polling
        :param status_forcelist: List of statuses to do retries and polling
        :param session: Session class
        """
        super().__init__(token, hostname)
        self._headers.update(headers or {})
        self.__session = self._super_session(retries, backoff_factor, status_forcelist, session)
        self.__splits = SplitsRequests(self._headers, self._hostname, self.__session)
        self.__environments = EnvironmentsRequests(self._headers, self._hostname, self.__session)
        self.__workspaces = WorkspacesRequests(self._headers, self._hostname, self.__session)
        self.__traffic_types = TrafficTypesRequests(self._headers, self._hostname, self.__session)
        self.__tags = TagsRequests(self._headers, self._hostname, self.__session)
        self.__segments = SegmentsRequests(self._headers, self._hostname, self.__session)

    def _super_session(
            self,
            retries: int,
            backoff_factor: float,
            status_forcelist: Tuple[int, ...],
            session: Optional[Session]
    ) -> Session:
        """
        Session method with adapter mounted

        :param retries: Number of retries
        :param backoff_factor: backoff factor for pulling
        :param status_forcelist: Tuple of statuses to apply retry on
        :param session: Already existing session object
        :return: Session object
        """
        session = session or Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "PATCH", "POST"]
        )
        adapter = TimeoutHTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        return session

    @property
    def splits(self):
        """
        Manager class object for splits endpoints
        :return: SplitsRequests
        """

        return self.__splits

    @property
    def environments(self):
        """
        Manager class object for environments endpoints
        :return: EnvironmentsRequests
        """

        return self.__environments

    @property
    def workspaces(self):
        """
        Manager class object for workspaces endpoints
        :return: WorkspacesRequests
        """

        return self.__workspaces

    @property
    def traffic_types(self):
        """
        Manager class object for traffic types endpoints
        :return: TrafficTypesRequests
        """

        return self.__traffic_types

    @property
    def tags(self):
        """
        Manager class object for tags endpoints
        :return: TagsRequests
        """

        return self.__tags

    @property
    def segments(self):
        """
        Manager class object for segments endpoints
        :return: SegmentsRequests
        """

        return self.__segments
