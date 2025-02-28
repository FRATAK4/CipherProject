from .rot_factory import RotFactory
from .rot13_cipher import Rot13Cipher


class Rot13Factory(RotFactory):
    def create_cipher(self) -> Rot13Cipher:
        return Rot13Cipher()
