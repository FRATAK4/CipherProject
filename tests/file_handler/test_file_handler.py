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
