from sub_menu import SubMenu


class SaveTextsMenu(SubMenu):
    @staticmethod
    def get_input() -> int:
        user_input = int(
            input("Enter a number of file you want to save your texts to: ")
        )
        return user_input
