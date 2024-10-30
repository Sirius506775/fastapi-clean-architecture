from abc import ABCMeta, abstractmethod
from user.domain.user import User


# 추상 클래스
class IUserRepository(metaclass=ABCMeta):
    """User 도메인을 영속하기 위한 Repository Interface

    Args:
        metaclass (_type_, optional): 객체지향 인터페이스로 선언하기 위해 ABCMeta 클래스를 상속받는다. Defaults to ABCMeta.

    Raises:
        NotImplementedError: save 메서드가 구현되지 않았을 경우 예외를 발생시킨다.
    """

    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """
        이메일로 유저를 찾는다.
        검색한 유저가 없을 경우 422 예외를 발생시킨다.
        """

        raise NotImplementedError
