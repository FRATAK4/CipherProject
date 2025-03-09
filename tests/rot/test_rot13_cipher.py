import pytest

from src.text import Text


@pytest.fixture
def mock_encoded_text():
    return Text(text="hello1", rot_type="rot13", status="encoded")


@pytest.fixture
def mock_decoded_text():
    return Text(text="hello2", rot_type="rot47", status="decoded")


class TestRot13Cipher:
    def test_encrypt(self, mock_decoded_text):
        pass
