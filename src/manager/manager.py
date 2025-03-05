from src.buffer import Buffer
from src.file_handler import FileHandler
from src.menu import MainMenu


class Manager:
    def __init__(self, file_handler: FileHandler, buffer: Buffer) -> None:
        self.file_handler = file_handler
        self.buffer = buffer
        self.running = True

        self._initialize_functions_dict()

    def _initialize_functions_dict(self):
        self.functions_dict = {
            1: self._add_new_text,
            2: self._remove_text,
            3: self._empty_your_texts,
            4: self._encrypt_decrypt_text,
            5: self._save_texts_to_file,
            6: self._load_texts_from_file,
            7: self._create_file,
            8: self._delete_file,
            9: self._exit,
        }

    def run(self) -> None:
        while self.running:
            MainMenu.show_menu(self.buffer)
            user_input = MainMenu.get_input()
            self.functions_dict.get(user_input)()

    def _add_new_text(self):
        pass

    def _remove_text(self):
        pass

    def _empty_your_texts(self):
        pass

    def _encrypt_decrypt_text(self):
        pass

    def _save_texts_to_file(self):
        pass

    def _load_texts_from_file(self):
        pass

    def _create_file(self):
        pass

    def _delete_file(self):
        pass

    def _exit(self):
        pass
