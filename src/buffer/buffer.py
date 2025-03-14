from text import Text


class Buffer:
    def __init__(self) -> None:
        self.texts: list[Text] = []

    def add_texts(self, texts: list[Text]) -> None:
        for text in texts:
            if text not in self.texts:
                self.texts.append(text)

    def remove_text(self, number: int) -> None:
        self.texts.pop(number - 1)

    def empty_buffer(self) -> None:
        self.texts.clear()
