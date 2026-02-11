import pytest

from rot import Rot13Factory
from text import Text


@pytest.fixture
def encrypted_text():
    return Text(text="apple", rot_type="rot13", status="encrypted")


@pytest.fixture
def decrypted_text():
    return Text(text="hello", rot_type="rot13", status="decrypted")


@pytest.fixture
def rot13_cipher_instance():
    factory = Rot13Factory()
    return factory.create_cipher()


class TestRot13Cipher:
    def test_encrypt(self, rot13_cipher_instance, decrypted_text):
        rot13_cipher_instance.encrypt(decrypted_text)
        assert decrypted_text == Text(
            text="uryyb", rot_type="rot13", status="encrypted"
        )

    def test_decrypt(self, rot13_cipher_instance, encrypted_text):
        rot13_cipher_instance.decrypt(encrypted_text)
        assert encrypted_text == Text(
            text="nccyr", rot_type="rot13", status="decrypted"
        )
