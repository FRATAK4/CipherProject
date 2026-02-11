import json
import os
from typing import cast

from .consts import DIRECTORY_FOR_FILES_PATH
from text import Text


class FileHandler:
    def __init__(self) -> None:
        self.path = ""

    def set_path(self, name: str) -> None:
        self.path = f"{DIRECTORY_FOR_FILES_PATH}/{name}.json"

    def create_file(self) -> None:
        with open(self.path, "w") as json_file:
            json.dump([], json_file, indent=4)

    def delete_file(self) -> None:
        os.remove(self.path)

    def save(self, texts: list[Text]) -> None:
        with open(self.path, "r") as json_file:
            load_texts = json.load(json_file)

        texts_as_dicts = [text.__dict__ for text in texts]
        data = []
        for text in load_texts + texts_as_dicts:
            if text not in data:
                data.append(text)

        with open(self.path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def load(self) -> list[dict[str, str]]:
        with open(self.path, "r") as json_file:
            return cast(list[dict[str, str]], json.load(json_file))

    @staticmethod
    def files_list() -> list[str]:
        return [
            file_name.removesuffix(".json")
            for file_name in os.listdir(DIRECTORY_FOR_FILES_PATH)
            if file_name != ".gitkeep"
        ]
