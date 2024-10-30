from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User


class UserRepository(IUserRepository):
    """User 도메인을 영속하기 위한 Repository 구현체

    Args:
        IUserRepository (_type_): User 도메인을 영속하기 위한 Repository Interface
    """

    def save(self, user: User):
        pass
