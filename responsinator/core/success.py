import typing
from starlette import status
import uuid
from starlette.background import BackgroundTask
from responsinator.utils.media_type import MediaTypeEnum
from .base import (
    JSONResponse,
    XMLResponse,
    HTMLResponse,
    PlainTextResponse,
    # FileResponse,
    # StreamingResponse,
    RedirectResponse
)


class SuccessResponse():
    def __init__(
        self,
        type: str = None,
        data: typing.Any = None,
        code: int = status.HTTP_200_OK,
        headers: typing.Optional[typing.Mapping[str, str]] = None,
        background: typing.Optional[BackgroundTask] = None,
        **kwargs: typing.Optional[typing.Mapping[str, str]]
    ) -> None:
        if data is not None:
            if isinstance(data, list):
                self.content = {
                    type: {
                        'data': data,
                        'paging': {
                            'cursors': {
                                'before': kwargs.get('before', None),
                                'after': kwargs.get('after', None),
                            },
                            'next': kwargs.get('next', None),
                        }
                    },
                    'id': str(uuid.uuid4())
                }
            elif isinstance(data, dict):
                self.content = {
                    'data': data,
                    'id': str(uuid.uuid4())
                }
            else:
                self.content = data
        else:
            pass
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

    def file(self):
        pass
        # return FileResponse(
        #     content=self.content,
        #     status_code=self.status_code,
        #     headers=self.headers,
        #     media_type=MediaTypeEnum.JSON,
        #     background=self.background
        # )

    def stream(self):
        pass
        # return StreamingResponse(
        #     content=self.content,
        #     status_code=self.status_code,
        #     headers=self.headers,
        #     media_type=MediaTypeEnum.JSON,
        #     background=self.background
        # )

    def text(self):
        return PlainTextResponse(
            content=self.content,
            status_code=self.status_code,
            headers=self.headers,
            media_type=MediaTypeEnum.TEXT,
            background=self.background
        )

    def redirect(self):
        return RedirectResponse(
            url=self.content,
            status_code=self.status_code,
            headers=self.headers,
            background=self.background
        )
