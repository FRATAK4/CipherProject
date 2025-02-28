from sub_menu import SubMenu


class RemoveTextMenu(SubMenu):
    def get_input(self) -> int:
        user_input = int(input("Enter a number of word: "))
        return user_input
