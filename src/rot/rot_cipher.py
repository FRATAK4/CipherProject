from abc import ABC, abstractmethod
from text import Text


class RotCipher(ABC):
    @abstractmethod
    def encrypt(self, text: Text) -> None:
        pass

    @abstractmethod
    def decrypt(self, text: Text) -> None:
        pass
