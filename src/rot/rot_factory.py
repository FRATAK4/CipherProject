from abc import ABC, abstractmethod

from . import RotCipher


class RotFactory(ABC):
    @abstractmethod
    def create_cipher(self) -> RotCipher:
        pass
