from unittest.mock import patch

import pytest

from buffer import Buffer
from text import Text
from menu import MainMenu


@pytest.fixture
def buffer():
    buffer = Buffer()
    buffer.add_texts(
        [
            Text(text="hello1", rot_type="rot13", status="encoded"),
            Text(text="hello2", rot_type="rot47", status="decoded"),
        ]
    )
    return buffer


class TestMainMenu:
    def test_show_menu(self, buffer):
        mock_files = ["file1.json", "file2.json"]

        with patch("builtins.print") as mock_print, patch(
            "file_handler.FileHandler.files_list", return_value=mock_files
        ):
            MainMenu.show_menu(buffer)

            mock_print.assert_any_call("1. hello1: encoded with rot13")
            mock_print.assert_any_call("2. hello2: decoded with rot47")

            mock_print.assert_any_call("1. file1.json")
            mock_print.assert_any_call("2. file2.json")

    def test_get_input_valid(self):
        with patch("builtins.input", return_value=2):
            assert MainMenu.get_input() == 2

    def test_get_input_invalid(self):
        with patch("builtins.input", return_value=0):
            with pytest.raises(IndexError):
                MainMenu.get_input()

    def test_get_input_non_numeric(self):
        with patch("builtins.input", return_value="huj"):
            with pytest.raises(ValueError):
                MainMenu.get_input()
