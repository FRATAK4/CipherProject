from abc import ABC


class RotFactory(ABC):
    def create_cipher(self) -> None:
        raise NotImplementedError
