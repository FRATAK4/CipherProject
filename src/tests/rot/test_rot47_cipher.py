import pytest

from rot import Rot47Factory
from text import Text


@pytest.fixture
def encrypted_text():
    return Text(text="apple", rot_type="rot47", status="encrypted")


@pytest.fixture
def decrypted_text():
    return Text(text="hello", rot_type="rot47", status="decrypted")


@pytest.fixture
def rot47_cipher_instance():
    factory = Rot47Factory()
    return factory.create_cipher()


class TestRot13Cipher:
    def test_encrypt(self, rot47_cipher_instance, decrypted_text):
        rot47_cipher_instance.encrypt(decrypted_text)
        assert decrypted_text == Text(
            text="96==@", rot_type="rot47", status="encrypted"
        )

    def test_decrypt(self, rot47_cipher_instance, encrypted_text):
        rot47_cipher_instance.decrypt(encrypted_text)
        assert encrypted_text == Text(
            text="2AA=6", rot_type="rot47", status="decrypted"
        )
