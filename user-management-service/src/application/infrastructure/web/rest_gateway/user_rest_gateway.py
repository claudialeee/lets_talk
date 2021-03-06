from abc import ABCMeta, abstractmethod
from typing import Union, Tuple, Dict, Any, NamedTuple, Optional

from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.user import User


class UserJson(NamedTuple):
    userId: str
    userName: str
    userAge: int
    userEmail: str
    url: str

    @staticmethod
    def from_user(*, user: User) -> 'UserJson':
        return UserJson(
            userId=user.id,
            userName=user.name,
            userAge=user.age,
            userEmail=user.email,
            url=f"/users/{user.id}"
        )


class ValidityOfUserCredentials(NamedTuple):
    valid: bool


Status = int
UserRegistrationResponse = Union[Tuple[Error, Status], Tuple[UserJson, Status]]
UserCheckCredentialsResponse = Tuple[ValidityOfUserCredentials, Status]


class UserRestApiGateway:
    class Post(metaclass=ABCMeta):
        @abstractmethod
        def __init__(self, *,
                     create_user_usecase: Optional[CreateUserUseCase],
                     check_user_credentials_usecase: Optional[CheckUserCredentialsUseCase]) -> None: pass

        @abstractmethod
        def register_user(self, *, data: Dict[str, Any]) -> UserRegistrationResponse: pass

        @abstractmethod
        def check_user_credentials(self, *, data: Dict[str, Any]) -> UserCheckCredentialsResponse: pass
