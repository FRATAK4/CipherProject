from abc import ABC, abstractmethod


class SubMenu(ABC):
    @staticmethod
    @abstractmethod
    def get_input():
        pass
