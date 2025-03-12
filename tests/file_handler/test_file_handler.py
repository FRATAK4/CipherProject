import json
import os.path
from unittest.mock import patch

import pytest

from src.file_handler import FileHandler


@pytest.fixture
def mock_file_handler_instance():
    return FileHandler()


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
