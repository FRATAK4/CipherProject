import json
import os.path
from unittest.mock import patch

import pytest

from src.file_handler import FileHandler
from src.text import Text


@pytest.fixture
def mock_file_handler_instance():
    return FileHandler()


@pytest.fixture
def mock_text_objects1():
    return [
        Text(text="hello1", rot_type="rot13", status="encrypted"),
        Text(text="hello2", rot_type="rot47", status="encrypted"),
    ]


@pytest.fixture
def mock_text_objects2():
    return [
        Text(text="hello2", rot_type="rot47", status="encrypted"),
        Text(text="hello3", rot_type="rot13", status="decrypted"),
    ]


@pytest.fixture
def mock_text_objects3():
    return [
        Text(text="hello1", rot_type="rot13", status="encrypted"),
        Text(text="hello2", rot_type="rot47", status="encrypted"),
        Text(text="hello3", rot_type="rot13", status="decrypted"),
    ]


class TestFileHandler:
    def test_initialization(self, mock_file_handler_instance):
        assert mock_file_handler_instance.path == ""

    def test_set_path(self, mock_file_handler_instance):
        with patch("src.file_handler.consts.DIRECTORY_FOR_FILES_PATH", "path"):
            mock_file_handler_instance.set_path("name")
        assert mock_file_handler_instance.path == "path/name.json"

    def test_create_file(self, mock_file_handler_instance):
        mock_file_handler_instance.path = "file.json"
        mock_file_handler_instance.create_file()
        assert os.path.exists("file.json")
        if os.path.exists("file.json"):
            with open("file.json", "r") as file:
                assert json.load(file) == []
            os.remove("file.json")

    def test_delete_file(self, mock_file_handler_instance):
        with open("file.json", "w") as file:
            json.dump([], file)
        mock_file_handler_instance.path = "file.json"
        mock_file_handler_instance.delete_file()
        assert not os.path.exists("file.json")

    def test_save(
        self,
        mock_file_handler_instance,
        mock_text_objects1,
        mock_text_objects2,
        mock_text_objects3,
    ):
        with open("file.json", "w") as file:
            json.dump([], file)
        mock_file_handler_instance.path = "file.json"
        mock_file_handler_instance.save(mock_text_objects1)
        with open("file.json", "r") as json_file:
            texts = json.load(json_file)
        texts = [Text(**line) for line in texts]
        assert texts == mock_text_objects1

        mock_file_handler_instance.save(mock_text_objects2)
        with open("file.json", "r") as json_file:
            texts = json.load(json_file)
        texts = [Text(**line) for line in texts]
        assert texts == mock_text_objects3
        os.remove("file.json")
