import pytest

from src.rot import Rot47Factory
from src.text import Text


@pytest.fixture
def mock_encrypted_text():
    return Text(text="apple", rot_type="rot47", status="encrypted")


@pytest.fixture
def mock_decrypted_text():
    return Text(text="hello", rot_type="rot47", status="decrypted")


@pytest.fixture
def mock_rot47_cipher_instance():
    factory = Rot47Factory()
    return factory.create_cipher()


class TestRot13Cipher:
    def test_encrypt(self, mock_rot47_cipher_instance, mock_decrypted_text):
        mock_rot47_cipher_instance.encrypt(mock_decrypted_text)
        assert mock_decrypted_text == Text(
            text="96==@", rot_type="rot47", status="encrypted"
        )

    def test_decrypt(self, mock_rot47_cipher_instance, mock_encrypted_text):
        mock_rot47_cipher_instance.decrypt(mock_encrypted_text)
        assert mock_encrypted_text == Text(
            text="2AA=6", rot_type="rot47", status="decrypted"
        )
