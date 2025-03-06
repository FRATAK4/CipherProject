from .rot_cipher import RotCipher
from src.text import Text


class Rot47Cipher(RotCipher):
    def encrypt(self, text: Text) -> None:
        encrypted_text = ""
        for char in text.text:
            encrypted_char = chr(33 + (ord(char) - 33 + 47) % 94)
            encrypted_text += encrypted_char

        text.text = encrypted_text
        text.status = "encrypted"

    def decrypt(self, text: Text) -> None:
        decrypted_text = ""
        for char in text.text:
            decrypted_char = chr(33 + (ord(char) - 33 - 47) % 94)
            decrypted_text += decrypted_char

        text.text = decrypted_text
        text.status = "decrypted"
