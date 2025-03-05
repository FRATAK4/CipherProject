import json
import os

from src.text import Text


class FileHandler:
    def __init__(self) -> None:
        self.path = ""

    def set_path(self, name: str) -> None:
        self.path = f"../files_for_texts/{name}.json"

    def create_file(self) -> None:
        with open(self.path, "w") as json_file:
            json.dump([], json_file, indent=4)

    def delete_file(self) -> None:
        os.remove(self.path)

    def save(self, texts: list[Text]) -> None:
        with open(self.path, "r") as json_file:
            load_texts = json.load(json_file)

        texts_as_dicts = [text.__dict__ for text in texts]
        data = list(set(load_texts).union(set(texts_as_dicts)))

        with open(self.path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def load(self) -> list[dict[str, str]]:
        with open(self.path, "r") as json_file:
            return json.load(json_file)
