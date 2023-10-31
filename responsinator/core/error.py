import uuid
import typing
from starlette.background import BackgroundTask
from starlette import status
from .base import (
    JSONResponse,
    HTMLResponse,
    XMLResponse
)
from responsinator.utils.media_type import MediaTypeEnum


class ErrorResponse():
    def __init__(
        self,
        message: typing.Any,
        type: str = None,
        code: int = status.HTTP_200_OK,
        error_subcode: int = 0,
        trace_id: str = str(uuid.uuid4()),
        headers: typing.Optional[typing.Mapping[str, str]] = None,
        background: typing.Optional[BackgroundTask] = None,
    ) -> None:
        self.content = {
            "error": {
                "message": message,
                "type": type,
                "code": code,
                "error_subcode": error_subcode,
                "trace_id": trace_id
            }
        }
        self.status_code = code
        self.headers = headers
        self.background = background

    def json(self):
        return JSONResponse(
            content=self.content,
            status_code=self.status_code,
            headers=self.headers,
            media_type=MediaTypeEnum.JSON,
            background=self.background
        )

    def xml(self):
        return XMLResponse(
            content=self.content,
            status_code=self.status_code,
            headers=self.headers,
            media_type=MediaTypeEnum.XML,
            background=self.background
        )

    def html(self):
        return HTMLResponse(
            content=self.content,
            status_code=self.status_code,
            headers=self.headers,
            media_type=MediaTypeEnum.HTML,
            background=self.background
        )
