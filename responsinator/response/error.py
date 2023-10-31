from starlette import status
from responsinator.core.error import ErrorResponse


class OAuthException(ErrorResponse):
    def __init__(
            self,
            message='Invalid OAuth access token',
            locale='en',
            headers=None,
            background=None
    ) -> None:
        super().__init__(
            message,
            type='OAuthException',
            code=status.HTTP_400_BAD_REQUEST,
            error_subcode=190,
            headers=headers,
            background=background
        )
