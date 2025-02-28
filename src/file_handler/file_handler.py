from src.text import Text
from typing import Dict


class FileHandler:
    def __init__(self) -> None:
        self.path = ""

    def set_path(self, name: str) -> None:
        self.path = name

    def create_file(self) -> None:
        pass

    def delete_file(self) -> None:
        pass

    def save(self, texts: list[Text]) -> None:
        pass

    def load(self) -> list[Dict[str, str]]:
        pass
