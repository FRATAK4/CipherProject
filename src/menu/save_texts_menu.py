from sub_menu import SubMenu


class SaveTextsMenu(SubMenu):
    def get_input(self) -> int:
        user_input = int(
            input("Enter a number of file you want to save your texts to: ")
        )
        return user_input
