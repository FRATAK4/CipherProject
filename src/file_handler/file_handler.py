import json
import os

import src.file_handler.consts
from src.text import Text


class FileHandler:
    def __init__(self) -> None:
        self.path = ""

    def set_path(self, name: str) -> None:
        self.path = f"{src.file_handler.consts.DIRECTORY_FOR_FILES_PATH}/{name}.json"

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
            return json.load(json_file)
