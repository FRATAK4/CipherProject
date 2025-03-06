import os

from src.file_handler.consts import DIRECTORY_FOR_FILES_PATH

files_list = [
    file_name.removesuffix(".json")
    for file_name in os.listdir(DIRECTORY_FOR_FILES_PATH)
]
