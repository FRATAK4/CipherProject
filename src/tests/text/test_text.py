from text import Text


class TestText:
    def test_text_initialization(self):
        text_instance = Text(text="hello", rot_type="rot13", status="encoded")

        assert text_instance.text == "hello"
        assert text_instance.rot_type == "rot13"
        assert text_instance.status == "encoded"

    def test_text_str_representation(self):
        text_instance = Text(text="hello", rot_type="rot13", status="encoded")

        assert str(text_instance) == "hello: encoded with rot13"
