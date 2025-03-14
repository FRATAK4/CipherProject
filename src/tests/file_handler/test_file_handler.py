import json
import os.path
from unittest.mock import patch

import pytest

from file_handler import FileHandler
from text import Text


@pytest.fixture
def file_handler_instance():
    return FileHandler()


@pytest.fixture
def text_objects1():
    return [
        Text(text="hello1", rot_type="rot13", status="encrypted"),
        Text(text="hello2", rot_type="rot47", status="encrypted"),
    ]


@pytest.fixture
def text_objects2():
    return [
        Text(text="hello2", rot_type="rot47", status="encrypted"),
        Text(text="hello3", rot_type="rot13", status="decrypted"),
    ]


@pytest.fixture
def text_objects3():
    return [
        Text(text="hello1", rot_type="rot13", status="encrypted"),
        Text(text="hello2", rot_type="rot47", status="encrypted"),
        Text(text="hello3", rot_type="rot13", status="decrypted"),
    ]


class TestFileHandler:
    def test_initialization(self, file_handler_instance):
        assert file_handler_instance.path == ""

    def test_set_path(self, file_handler_instance):
        with patch("file_handler.file_handler.DIRECTORY_FOR_FILES_PATH", "path"):
            file_handler_instance.set_path("name")
        assert file_handler_instance.path == "path/name.json"

    def test_create_file(self, file_handler_instance):
        file_handler_instance.path = "file.json"
        file_handler_instance.create_file()
        assert os.path.exists("file.json")
        if os.path.exists("file.json"):
            with open("file.json", "r") as file:
                assert json.load(file) == []
            os.remove("file.json")

    def test_delete_file(self, file_handler_instance):
        with open("file.json", "w") as file:
            json.dump([], file)
        file_handler_instance.path = "file.json"
        file_handler_instance.delete_file()
        assert not os.path.exists("file.json")

    def test_save(
        self,
        file_handler_instance,
        text_objects1,
        text_objects2,
        text_objects3,
    ):
        with open("file.json", "w") as file:
            json.dump([], file)
        file_handler_instance.path = "file.json"
        file_handler_instance.save(text_objects1)
        with open("file.json", "r") as json_file:
            texts = json.load(json_file)
        texts = [Text(**line) for line in texts]
        assert texts == text_objects1

        file_handler_instance.save(text_objects2)
        with open("file.json", "r") as json_file:
            texts = json.load(json_file)
        texts = [Text(**line) for line in texts]
        assert texts == text_objects3
        os.remove("file.json")

    def test_load(self, file_handler_instance, text_objects1):
        texts_as_dicts = [text.__dict__ for text in text_objects1]
        with open("file.json", "w") as file:
            json.dump(texts_as_dicts, file)
        file_handler_instance.path = "file.json"
        texts = file_handler_instance.load()
        texts = [Text(**line) for line in texts]
        assert texts == text_objects1
        os.remove("file.json")
