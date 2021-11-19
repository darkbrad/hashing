import hashlib
import base64
import random
import typing
a = []
class PasswordHandler:

    def hash_password_raw(self,password: str) -> str:
        hash_data = hashlib.sha256(password.encode("utf-8"))
        return base64.b64encode(hash_data.digest()).decode("utf-8")



    def hash_password(self,password: str,peper="") -> str:

        salt_number = random.randint(0, 2 ** 256 - 1)
        salt=base64.b64encode(salt_number.to_bytes(32, "little")).decode("utf-8")
        a.append(self.hash_password_raw(password + ":" + salt+":"+peper) + ":" + salt+":"+peper)
        return a[0]



    def password_verify(self,password: str, hash: str) -> bool:
        raw_hash, salt,peper = hash.split(":", 3)
        return self.hash_password_raw(password + ":" + salt+":"+peper) == raw_hash


user1=PasswordHandler()
print(user1.password_verify("ayjydtdd",user1.hash_password("ayjydtdd")))