from src.buffer import Buffer
from src.file_handler import FileHandler
from src.menu import (
    NewTextMenu,
    SubMenu,
)
from typing import Type


class Manager:
    def __init__(self, file_handler: Type[FileHandler], buffer: Type[Buffer]) -> None:
        self.file_handler = file_handler
        self.buffer = buffer

        self._initialize_menu()
        #
        # self.menu_classes: dict[int, Type[SubMenu]] = {
        #     1: NewTextMenu
        # }

    def _initialize_menu(self) -> dict[int, Type[SubMenu]]:
        self.menu_classes = {1: NewTextMenu}

    @property
    def initialize_menu(self) -> dict[int, Type[SubMenu]]:
        if self._menu_classes is None:
            self._menu_classes = {1: NewTextMenu}
        return self._menu_classes

    def run(self):
        while True:
            self.main_menu.show_menu(self.buffer)
            # user_input = self.main_menu.get_input()
