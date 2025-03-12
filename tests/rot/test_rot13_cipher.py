import pytest

from src.rot import Rot13Factory
from src.text import Text


@pytest.fixture
def mock_encrypted_text():
    return Text(text="apple", rot_type="rot13", status="encrypted")


@pytest.fixture
def mock_decrypted_text():
    return Text(text="hello", rot_type="rot13", status="decrypted")


@pytest.fixture
def mock_rot13_cipher_instance():
    factory = Rot13Factory()
    return factory.create_cipher()


class TestRot13Cipher:
    def test_encrypt(self, mock_rot13_cipher_instance, mock_decrypted_text):
        mock_rot13_cipher_instance.encrypt(mock_decrypted_text)
        assert mock_decrypted_text == Text(
            text="uryyb", rot_type="rot13", status="encrypted"
        )

    def test_decrypt(self, mock_rot13_cipher_instance, mock_encrypted_text):
        mock_rot13_cipher_instance.decrypt(mock_encrypted_text)
        assert mock_encrypted_text == Text(
            text="nccyr", rot_type="rot13", status="decrypted"
        )
