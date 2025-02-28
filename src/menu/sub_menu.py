from abc import ABC


class SubMenu(ABC):
    def get_input(self):
        raise NotImplementedError
