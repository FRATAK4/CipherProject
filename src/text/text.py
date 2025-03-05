from dataclasses import dataclass


@dataclass
class Text:
    text: str
    rot_type: str
    status: str

    def __str__(self) -> str:
        return f"{self.text}: {self.status} with {self.rot_type}"
