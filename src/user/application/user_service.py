from datetime import datetime
from fastapi import BackgroundTasks, HTTPException, status
from ulid import ULID

from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository
from util.crypto import Crypto


class UserService:
    def __init__(self):
        self.user_repo: IUserRepository = UserRepository()
        self.ulid = ULID()
        self.crypto = Crypto()

    def create_user(
        self,
        name: str,
        email: str,
        password: str,
    ):

        # 데이터베이스에서 찾은 유저 변수
        _user = None

        try:
            _user = self.user_repo.find_by_email(email)
        except HTTPException as e:
            if e.status_code != 422:
                raise e

        # 이미 가입 된 이메일인 경우
        if _user:
            raise HTTPException(status_code=422)

        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=self.crypto.hash_password(password),
            password=password,
            created_at=now,
            updated_at=now,
        )
        self.user_repo.save(user)

        return user
