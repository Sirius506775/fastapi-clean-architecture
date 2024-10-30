"""
FastAPI 공식 문서에서 추천하는 PassLib 패키지와 Bcrypt 알고리즘을 사용하여 비밀번호를 암호화하는 클래스 작성
"""

from passlib.context import CryptContext


class Crypto:
    """
    PassLib을 이용해 평문을 암호화하고, 암호화된 비밀번호와 평문 비밀번호가 일치하는지 검증하는 모듈

    """

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, secret):
        return self.pwd_context.hash(secret)

    def verify(self, secret, hash):
        return self.pwd_context.verify(secret, hash)
