from .rot_factory import RotFactory
from .rot47_cipher import Rot47Cipher


class Rot47Factory(RotFactory):
    def create_cipher(self) -> Rot47Cipher:
        return Rot47Cipher()
