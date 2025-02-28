import json
import os

from src.text import Text
from typing import Dict


class FileHandler:
    def __init__(self) -> None:
        self.path = ""

    def set_path(self, name: str) -> None:
        self.path = name

    def create_file(self) -> None:
        with open(self.path, "w") as json_file:
            json.dump([], json_file, indent=4)

    def delete_file(self) -> None:
        os.remove(self.path)

    def save(self, texts: list[Text]) -> None:
        pass

    def load(self) -> list[Dict[str, str]]:
        pass
