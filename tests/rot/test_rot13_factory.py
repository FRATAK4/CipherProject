import pytest

from src.rot import Rot13Factory, Rot13Cipher


@pytest.fixture
def mock_rot13_factory_instance():
    return Rot13Factory()


class TestRot13Factory:
    def test_create_cipher(self, mock_rot13_factory_instance):
        assert isinstance(mock_rot13_factory_instance.create_cipher(), Rot13Cipher)
