from unittest.mock import patch

import pytest

from src.buffer import Buffer
from src.file_handler import FileHandler
from src.manager.manager import Manager
from src.text.text import Text


@pytest.fixture
def manager_instance(file_handler_instance, buffer_instance):
    return Manager(file_handler_instance, buffer_instance)


@pytest.fixture
def file_handler_instance():
    return FileHandler()


@pytest.fixture
def buffer_instance():
    return Buffer()


@pytest.fixture
def example_texts():
    return [
        Text(text="djreg", rot_type="rot13", status="encrypted"),
        Text(text="lhvbc", rot_type="rot13", status="decrypted"),
        Text(text="2D578", rot_type="rot47", status="encrypted"),
        Text(text="9;<=", rot_type="rot47", status="decrypted"),
    ]


def run_simulation(manager_instance, main_menu_inputs, sub_menu_inputs):
    with (
        patch("src.menu.main_menu.MainMenu.show_menu"),
        patch("src.menu.main_menu.MainMenu.get_input", side_effect=main_menu_inputs),
        patch("builtins.input", side_effect=sub_menu_inputs),
    ):
        manager_instance.run()


class TestManager:
    def test_initialization(
        self, manager_instance, file_handler_instance, buffer_instance
    ):
        assert manager_instance.file_handler == file_handler_instance
        assert manager_instance.buffer == buffer_instance
        assert manager_instance.running

    def test_run_show_menu_and_exit(self, manager_instance):
        with patch("src.menu.main_menu.MainMenu.show_menu") as mock_show_menu:
            with patch("src.menu.main_menu.MainMenu.get_input", return_value=9):
                manager_instance.run()
                mock_show_menu.assert_called_with(manager_instance.buffer)
                assert not manager_instance.running

    def test_run_add_new_text_valid_inputs(self, manager_instance):
        main_menu_inputs = [1, 1, 1, 1, 1, 9]
        add_new_text_inputs = [
            "qwert rot13 encrypt",
            "yuiop rot13 decrypt",
            "asdfg rot47 encrypt",
            "hjkl rot47 decrypt",
            "yuiop rot13 decrypt",
        ]

        run_simulation(manager_instance, main_menu_inputs, add_new_text_inputs)

        assert manager_instance.buffer.texts == [
            Text(text="djreg", rot_type="rot13", status="encrypted"),
            Text(text="lhvbc", rot_type="rot13", status="decrypted"),
            Text(text="2D578", rot_type="rot47", status="encrypted"),
            Text(text="9;<=", rot_type="rot47", status="decrypted"),
        ]

    def test_run_add_new_text_invalid_inputs(self, manager_instance, capsys):
        main_menu_inputs = [1, 1, 1, 1, 9]
        add_new_text_inputs = [
            "qwert rot15 encrypt",
            "yuiop rot17 decrypt",
            "jklh2436# rot13 encrypt" "asdfg rot47 encpt",
            "hjkl rot47 decpt",
        ]

        run_simulation(manager_instance, main_menu_inputs, add_new_text_inputs)

        captured = capsys.readouterr().out

        assert captured.count("Invalid input value!") == len(add_new_text_inputs)
        assert manager_instance.buffer.texts == []

    def test_run_remove_text_valid_inputs(self, manager_instance, example_texts):
        manager_instance.buffer.texts = example_texts

        main_menu_inputs = [2, 2, 9]
        remove_text_inputs = [1, 2]

        run_simulation(manager_instance, main_menu_inputs, remove_text_inputs)

        assert manager_instance.buffer.texts == [
            Text(text="lhvbc", rot_type="rot13", status="decrypted"),
            Text(text="9;<=", rot_type="rot47", status="decrypted"),
        ]

    def test_run_remove_text_invalid_inputs(
        self, manager_instance, example_texts, capsys
    ):
        manager_instance.buffer.texts = example_texts

        main_menu_inputs = [2, 2, 2, 9]
        remove_text_inputs = [0, 10, "abc"]

        run_simulation(manager_instance, main_menu_inputs, remove_text_inputs)

        captured = capsys.readouterr().out

        assert captured == (
            "Given number is out of range!\n"
            "Given number is out of range!\n"
            "Invalid input value!\n"
        )
        assert manager_instance.buffer.texts == example_texts

    def test_run_empty_your_texts(self, manager_instance, example_texts):
        manager_instance.buffer.texts = example_texts

        main_menu_inputs = [3, 9]
        remove_text_inputs = []

        run_simulation(manager_instance, main_menu_inputs, remove_text_inputs)

        assert manager_instance.buffer.texts == []
