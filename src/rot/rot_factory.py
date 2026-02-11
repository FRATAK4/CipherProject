from abc import ABC, abstractmethod

from .rot_cipher import RotCipher


class RotFactory(ABC):
    @abstractmethod
    def create_cipher(self) -> RotCipher:
        pass
