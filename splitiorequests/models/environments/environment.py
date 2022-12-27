"""Environment dataclass"""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Environment:
    """Environment model"""
    name: str
    id: str
    production: bool
    orgId: Optional[str] = None
    status: Optional[str] = None
    workspaceIds: Optional[List[str]] = None
    creationTime: Optional[int] = None
    permissioningEnabled: Optional[bool] = None
    segments: Optional[List[str]] = None
    tests: Optional[List[str]] = None
    apiTokens: Optional[List[str]] = None
    workspaces: Optional[List[str]] = None
    integrations: Optional[List[str]] = None
    permissions: Optional[List[str]] = None
    settings: Optional[List[str]] = None
