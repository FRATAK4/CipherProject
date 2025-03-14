from unittest.mock import patch

import pytest

from buffer import Buffer
from file_handler import FileHandler
from manager.manager import Manager
from text.text import Text


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
        patch("menu.main_menu.MainMenu.show_menu"),
        patch("menu.main_menu.MainMenu.get_input", side_effect=main_menu_inputs),
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
        with patch("menu.main_menu.MainMenu.show_menu") as mock_show_menu:
            with patch("menu.main_menu.MainMenu.get_input", return_value=9):
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

    def test_run_encrypt_decrypt_text_valid_inputs(
        self, manager_instance, example_texts
    ):
        manager_instance.buffer.texts = example_texts

        main_menu_inputs = [4, 4, 9]
        encrypt_decrypt_text_inputs = [1, 4]

        run_simulation(manager_instance, main_menu_inputs, encrypt_decrypt_text_inputs)

        assert manager_instance.buffer.texts == [
            Text(text="qwert", rot_type="rot13", status="decrypted"),
            Text(text="lhvbc", rot_type="rot13", status="decrypted"),
            Text(text="2D578", rot_type="rot47", status="encrypted"),
            Text(text="hjkl", rot_type="rot47", status="encrypted"),
        ]

    def test_run_encrypt_decrypt_text_invalid_inputs(
        self, manager_instance, example_texts, capsys
    ):
        manager_instance.buffer.texts = example_texts

        main_menu_inputs = [4, 4, 4, 9]
        remove_text_inputs = [0, 10, "abc"]

        run_simulation(manager_instance, main_menu_inputs, remove_text_inputs)

        captured = capsys.readouterr().out

        assert captured == (
            "Given number is out of range!\n"
            "Given number is out of range!\n"
            "Invalid input value!\n"
        )
        assert manager_instance.buffer.texts == example_texts

    def test_run_save_text_to_file_valid_inputs(self, manager_instance):
        main_menu_inputs = [5, 9]
        save_text_to_file_inputs = [3]
        files_list = ["file1", "file2", "file3", "file4"]

        with (
            patch.object(manager_instance.file_handler, "set_path") as mock_set_path,
            patch.object(manager_instance.file_handler, "save") as mock_save,
            patch("file_handler.globals.files_list", files_list),
        ):
            run_simulation(manager_instance, main_menu_inputs, save_text_to_file_inputs)

            mock_set_path.assert_called_with("file3")
            mock_save.assert_called_with(manager_instance.buffer.texts)

    def test_run_save_text_to_file_invalid_inputs(self, manager_instance, capsys):
        main_menu_inputs = [5, 5, 5, 9]
        save_text_to_file_inputs = [0, 10, "abc"]
        files_list = ["file1", "file2", "file3", "file4"]

        with (
            patch.object(manager_instance.file_handler, "set_path"),
            patch.object(manager_instance.file_handler, "save"),
            patch("file_handler.globals.files_list", files_list),
        ):
            run_simulation(manager_instance, main_menu_inputs, save_text_to_file_inputs)

        captured = capsys.readouterr().out

        assert captured == (
            "Given number is out of range!\n"
            "Given number is out of range!\n"
            "Invalid input value!\n"
        )

    def test_run_load_texts_from_file_valid_inputs(
        self, manager_instance, example_texts
    ):
        main_menu_inputs = [6, 9]
        load_texts_from_file_inputs = [3]
        files_list = ["file1", "file2", "file3", "file4"]
        example_texts_as_dicts = [text.__dict__ for text in example_texts]

        with (
            patch.object(manager_instance.file_handler, "set_path") as mock_set_path,
            patch.object(
                manager_instance.file_handler,
                "load",
                return_value=example_texts_as_dicts,
            ) as mock_load,
            patch("file_handler.globals.files_list", files_list),
        ):
            run_simulation(
                manager_instance, main_menu_inputs, load_texts_from_file_inputs
            )

            mock_set_path.assert_called_with("file3")
            mock_load.assert_called_once()

        assert manager_instance.buffer.texts == example_texts

    def test_run_load_texts_from_file_invalid_inputs(self, manager_instance, capsys):
        main_menu_inputs = [6, 6, 6, 9]
        load_texts_from_file_inputs = [0, 10, "abc"]
        files_list = ["file1", "file2", "file3", "file4"]

        with patch("file_handler.globals.files_list", files_list):
            run_simulation(
                manager_instance, main_menu_inputs, load_texts_from_file_inputs
            )

        captured = capsys.readouterr().out

        assert captured == (
            "Given number is out of range!\n"
            "Given number is out of range!\n"
            "Invalid input value!\n"
        )

    def test_run_create_file_valid_inputs(self, manager_instance):
        main_menu_inputs = [7, 9]
        create_file_inputs = ["file5"]
        files_list = ["file1", "file2", "file3", "file4"]

        with (
            patch.object(manager_instance.file_handler, "set_path") as mock_set_path,
            patch.object(
                manager_instance.file_handler,
                "create_file",
            ) as mock_create_file,
            patch("file_handler.globals.files_list", files_list),
        ):
            run_simulation(manager_instance, main_menu_inputs, create_file_inputs)

            mock_set_path.assert_called_with("file5")
            mock_create_file.assert_called_once()

        assert files_list == ["file1", "file2", "file3", "file4", "file5"]

    def test_run_create_file_invalid_inputs(self, manager_instance, capsys):
        main_menu_inputs = [7, 7, 9]
        create_file_inputs = ["file3", ""]
        files_list = ["file1", "file2", "file3", "file4"]

        with patch("file_handler.globals.files_list", files_list):
            run_simulation(manager_instance, main_menu_inputs, create_file_inputs)

        captured = capsys.readouterr().out

        assert captured == (
            "File with this name already exists!\n" "Invalid input value!\n"
        )

    def test_run_delete_file_valid_inputs(self, manager_instance):
        main_menu_inputs = [8, 9]
        create_file_inputs = [3]
        files_list = ["file1", "file2", "file3", "file4"]

        with (
            patch.object(manager_instance.file_handler, "set_path") as mock_set_path,
            patch.object(
                manager_instance.file_handler,
                "delete_file",
            ) as mock_delete_file,
            patch("file_handler.globals.files_list", files_list),
        ):
            run_simulation(manager_instance, main_menu_inputs, create_file_inputs)

            mock_set_path.assert_called_with("file3")
            mock_delete_file.assert_called_once()

        assert files_list == ["file1", "file2", "file4"]

    def test_run_delete_file_invalid_inputs(self, manager_instance, capsys):
        main_menu_inputs = [8, 8, 8, 9]
        delete_file_inputs = [0, 10, "abc"]
        files_list = ["file1", "file2", "file3", "file4"]

        with patch("file_handler.globals.files_list", files_list):
            run_simulation(manager_instance, main_menu_inputs, delete_file_inputs)

        captured = capsys.readouterr().out

        assert captured == (
            "Given number is out of range!\n"
            "Given number is out of range!\n"
            "Invalid input value!\n"
        )
