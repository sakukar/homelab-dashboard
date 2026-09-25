from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
Percentage = Annotated[float, Field(ge=0, le=100, allow_inf_nan=False)]
LoadValue = Annotated[float, Field(ge=0, allow_inf_nan=False)]


class ServerStatus(StrEnum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class LoadAverage(BaseModel):
    """System load averages, not percentages or normalized by CPU count."""

    one_minute: LoadValue
    five_minutes: LoadValue
    fifteen_minutes: LoadValue


class Server(BaseModel):
    """A server snapshot; unavailable measurements are None, not zero."""

    name: NonEmptyString
    hostname: NonEmptyString
    status: ServerStatus = ServerStatus.UNKNOWN
    cpu_usage: Percentage | None = Field(default=None, description="CPU usage (%)")
    load: Annotated[int, Field(ge=0, strict=True)] | None = Field(
        default=None, description="Current count of runnable tasks"
    )
    load_average: LoadAverage | None = None
    memory_usage: Percentage | None = Field(default=None, description="Memory used (%)")
    disk_usage: Percentage | None = Field(default=None, description="Disk space used (%)")
