from src.buffer import Buffer
from src.file_handler import FileHandler
import src.file_handler.consts
from src.menu import MainMenu
from src.rot import Rot13Factory, Rot47Factory
from src.text import Text


class Manager:
    def __init__(self, file_handler: FileHandler, buffer: Buffer) -> None:
        self.file_handler = file_handler
        self.buffer = buffer
        self.running: bool = True

        self._initialize_factories_dict()
        self._initialize_functions_dict()

    def _initialize_factories_dict(self) -> None:
        self.factories_dict = {"rot13": Rot13Factory, "rot47": Rot47Factory}

    def _initialize_functions_dict(self) -> None:
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
            try:
                user_input = MainMenu.get_input()
                self.functions_dict.get(user_input)()
            except ValueError:
                print("Invalid input value!")
            except IndexError:
                print("Given number is out of range!")
            except FileExistsError:
                print("File with this name already exists!")

    def _add_new_text(self) -> None:
        user_input = input(
            "Enter a text (format: 'text' 'rot13/rot47' 'encrypt/decrypt'): "
        )
        text, rot_type, functionality = user_input.split()

        if rot_type not in ["rot13", "rot47"] or functionality not in [
            "encrypt",
            "decrypt",
        ]:
            raise ValueError

        if rot_type == "rot13":
            for char in text:
                if ord(char) not in range(65, 91) and ord(char) not in range(97, 123):
                    raise ValueError

        text_object = None

        cipher_factory = self.factories_dict.get(rot_type)()
        cipher = cipher_factory.create_cipher()

        match functionality:
            case "encrypt":
                text_object = Text(text, rot_type, "decrypted")
                cipher.encrypt(text_object)
            case "decrypt":
                text_object = Text(text, rot_type, "encrypted")
                cipher.decrypt(text_object)

        self.buffer.add_texts([text_object])

    def _remove_text(self) -> None:
        user_input = int(input("Enter a number of word: "))

        if user_input not in range(1, len(self.buffer.texts) + 1):
            raise IndexError

        self.buffer.remove_text(user_input)

    def _empty_your_texts(self) -> None:
        self.buffer.empty_buffer()

    def _encrypt_decrypt_text(self) -> None:
        user_input = int(input("Enter a number of word you want to change status of: "))

        if user_input not in range(1, len(self.buffer.texts) + 1):
            raise IndexError

        text_object = self.buffer.texts[user_input - 1]

        cipher_factory = self.factories_dict.get(text_object.rot_type)()
        cipher = cipher_factory.create_cipher()

        match text_object.status:
            case "encrypted":
                cipher.decrypt(text_object)
            case "decrypted":
                cipher.encrypt(text_object)

    def _save_texts_to_file(self) -> None:
        user_input = int(
            input("Enter a number of file you want to save your texts to: ")
        )

        if user_input not in range(1, len(src.file_handler.globals.files_list) + 1):
            raise IndexError

        self.file_handler.set_path(src.file_handler.globals.files_list[user_input - 1])
        self.file_handler.save(self.buffer.texts)

    def _load_texts_from_file(self) -> None:
        user_input = int(input("Enter a number of file you want to load texts from: "))

        if user_input not in range(1, len(src.file_handler.globals.files_list) + 1):
            raise IndexError

        self.file_handler.set_path(src.file_handler.globals.files_list[user_input - 1])
        texts = [Text(**line) for line in self.file_handler.load()]
        self.buffer.add_texts(texts)

    def _create_file(self) -> None:
        user_input = input("Enter a name of file: ")

        if user_input in src.file_handler.globals.files_list:
            raise FileExistsError
        if user_input == "":
            raise ValueError

        self.file_handler.set_path(user_input)
        self.file_handler.create_file()
        src.file_handler.globals.files_list.append(user_input)

    def _delete_file(self) -> None:
        user_input = int(input("Enter a number of file you want to delete: "))

        if user_input not in range(1, len(src.file_handler.globals.files_list) + 1):
            raise IndexError

        self.file_handler.set_path(src.file_handler.globals.files_list[user_input - 1])
        self.file_handler.delete_file()
        src.file_handler.globals.files_list.pop(user_input - 1)

    def _exit(self) -> None:
        self.running = False
