import pytest

from src.rot import Rot47Factory, Rot47Cipher


@pytest.fixture
def mock_rot47_factory_instance():
    return Rot47Factory()


class TestRot47Factory:
    def test_create_cipher(self, mock_rot47_factory_instance):
        assert isinstance(mock_rot47_factory_instance.create_cipher(), Rot47Cipher)
