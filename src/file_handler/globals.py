import os

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)


DIRECTORY_FOR_FILES_PATH = os.path.join(script_dir, "files_for_texts")


files_list = [
    file_name.removesuffix(".json")
    for file_name in os.listdir(DIRECTORY_FOR_FILES_PATH)
]
