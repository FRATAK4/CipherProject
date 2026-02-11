import pytest

from rot import Rot13Factory, Rot13Cipher


@pytest.fixture
def rot13_factory_instance():
    return Rot13Factory()


class TestRot13Factory:
    def test_create_cipher(self, rot13_factory_instance):
        assert isinstance(rot13_factory_instance.create_cipher(), Rot13Cipher)
