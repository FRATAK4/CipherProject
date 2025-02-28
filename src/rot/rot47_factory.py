from .rot_factory import RotFactory
from .rot47_cipher import Rot47Cipher


class Rot13Factory(RotFactory):
    def create_cipher(self) -> Rot47Cipher:
        return Rot47Cipher()
