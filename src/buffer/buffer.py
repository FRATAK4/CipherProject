from src.text import Text


class Buffer:
    def __init__(self) -> None:
        self.texts: list[Text] = []

    def add_text(self, text) -> None:
        if text not in self.texts:
            self.texts.append(text)

    def empty_buffer(self) -> None:
        self.texts.clear()
