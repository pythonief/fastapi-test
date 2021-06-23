from passlib.context import CryptContext


class Hash():
    pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password: str):
        return self.pwd_cxt.hash(password)
