import os

from src.buffer import Buffer


class MainMenu:
    def show_menu(self, buffer: Buffer) -> None:
        print("CipherMenu")
        print("==============================")
        print("Files:")
        directory_path = "../files_for_texts"
        files = os.listdir(directory_path)
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        print("---------------------------------------------")
        print("Your texts:")
        for i, text in enumerate(buffer.texts, 1):
            print(f"{i}. {text.text}: {text.status} with {text.rot_type}")
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

    def get_input(self) -> int:
        user_input = int(input("\nEnter a number of option: "))
        return user_input
