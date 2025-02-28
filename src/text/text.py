from dataclasses import dataclass


@dataclass
class Text:
    text: str = "xyz"
    rot_type: str = "rot13"
    status: str = "encrypted"
