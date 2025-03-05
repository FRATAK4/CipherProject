from src.buffer import Buffer
from src.file_handler import FileHandler
from src.menu import MainMenu


class Manager:
    def __init__(self, file_handler: FileHandler, buffer: Buffer) -> None:
        self.file_handler = file_handler
        self.buffer = buffer

    def run(self):
        while True:
            MainMenu.show_menu(self.buffer)
