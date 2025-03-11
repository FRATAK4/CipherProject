import pytest

from src.text import Text


@pytest.fixture
def mock_encrypted_text():
    return Text(text="hello1", rot_type="rot13", status="encrypted")


@pytest.fixture
def mock_decrypted_text():
    return Text(text="hello2", rot_type="rot47", status="decrypted")


class TestRot13Cipher:
    def test_encrypt(self, mock_decrypted_text):
        pass
