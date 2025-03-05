from abc import ABC, abstractmethod


class RotFactory(ABC):
    @abstractmethod
    def create_cipher(self) -> None:
        pass
