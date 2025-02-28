from abc import ABC
from src.text import Text


class RotCipher(ABC):
    def encrypt(self, text: Text) -> Text:
        raise NotImplementedError

    def decrypt(self, text: Text) -> Text:
        raise NotImplementedError
