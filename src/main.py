from src.buffer import Buffer
from src.file_handler import FileHandler
from src.manager.manager import Manager


def main():
    file_handler = FileHandler()
    buffer = Buffer()
    manager = Manager(file_handler, buffer)
    manager.run()


if __name__ == "__main__":
    main()
