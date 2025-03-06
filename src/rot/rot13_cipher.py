from .rot_cipher import RotCipher
from src.text import Text


class Rot13Cipher(RotCipher):
    def encrypt(self, text: Text) -> None:
        encrypted_text = ""
        for char in text.text:
            if char.isupper():
                encrypted_char = chr(65 + (ord(char) - 65 + 13) % 26)
            elif char.islower():
                encrypted_char = chr(97 + (ord(char) - 97 + 13) % 26)
            else:
                encrypted_char = ""
            encrypted_text += encrypted_char

        text.text = encrypted_text
        text.status = "encrypted"

    def decrypt(self, text: Text) -> None:
        decrypted_text = ""
        for char in text.text:
            if char.isupper():
                decrypted_char = chr(65 + (ord(char) - 65 - 13) % 26)
            elif char.islower():
                decrypted_char = chr(97 + (ord(char) - 97 - 13) % 26)
            else:
                decrypted_char = ""
            decrypted_text += decrypted_char

        text.text = decrypted_text
        text.status = "decrypted"
