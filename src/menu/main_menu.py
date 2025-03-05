import os

from src.buffer import Buffer
from src.file_handler.consts import DIRECTORY_FOR_FILES_PATH


class MainMenu:
    @staticmethod
    def show_menu(buffer: Buffer) -> None:
        print("CipherMenu")
        print("==============================")  # int * "="
        print("Files:")
        files = os.listdir(DIRECTORY_FOR_FILES_PATH)
        for no, file in enumerate(files, start=1):
            print(f"{no}. {file}")
        print("---------------------------------------------")
        print("Your texts:")
        for no, text in enumerate(buffer.texts, start=1):
            print(f"{no}. {text}")
        print("==============================")
        print("What do you want to do?")
        print("1. Add new text")
        print("2. Remove text")
        print("3. Empty your texts")
        print("4. Encrypt/decrypt text")
        print("5. Save texts to file")
        print("6. Load texts from file")
        print("7. Create file")
        print("8. Delete file")
        print("9. EXIT")

    @staticmethod
    def get_input() -> int:
        user_input = int(input("\nEnter a number of option: "))
        return user_input
