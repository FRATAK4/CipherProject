import json
import os

from .consts import DIRECTORY_FOR_FILES_PATH
from text import Text


class FileHandler:
    def __init__(self) -> None:
        self.path = ""
        FileHandler._initialize_files_for_texts()

    @staticmethod
    def _initialize_files_for_texts():
        if not os.path.exists("files_for_texts"):
            os.mkdir("files_for_texts")

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
            return json.load(json_file)
