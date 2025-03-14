from unittest.mock import patch

import pytest

from src.buffer import Buffer
from src.file_handler import FileHandler
from src.manager.manager import Manager


@pytest.fixture
def manager_instance(file_handler_instance, buffer_instance):
    return Manager(file_handler_instance, buffer_instance)


@pytest.fixture
def file_handler_instance():
    return FileHandler()


@pytest.fixture
def buffer_instance():
    return Buffer()


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
