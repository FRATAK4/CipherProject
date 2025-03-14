import pytest

from buffer import Buffer
from text import Text


@pytest.fixture
def buffer():
    return Buffer()


@pytest.fixture
def sample_texts():
    return [
        Text(text="hello1", rot_type="rot13", status="encoded"),
        Text(text="hello2", rot_type="rot47", status="decoded"),
    ]


class TestBuffer:
    def test_should_initialize_empty_buffer(self, buffer):
        assert buffer.texts == []

    def test_should_add_different_texts_to_buffer(self, buffer, sample_texts):
        buffer.add_texts(sample_texts)

        assert len(buffer.texts) == 2
        assert buffer.texts[0] == sample_texts[0]
        assert buffer.texts[1] == sample_texts[1]

    def test_should_not_add_same_text_to_buffer(self, buffer, sample_texts):
        buffer.add_texts(sample_texts)
        buffer.add_texts([Text(text="hello1", rot_type="rot13", status="encoded")])

        assert len(buffer.texts) == 2

    def test_should_remove_text_from_buffer(self, buffer, sample_texts):
        buffer.add_texts(sample_texts)
        buffer.remove_text(1)

        assert len(buffer.texts) == 1
        assert buffer.texts[0] == sample_texts[1]

    def test_should_clear_buffer(self, buffer, sample_texts):
        buffer.add_texts(sample_texts)
        buffer.empty_buffer()

        assert buffer.texts == []
