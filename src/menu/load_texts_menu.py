from sub_menu import SubMenu


class LoadTextsMenu(SubMenu):
    def get_input(self) -> int:
        user_input = int(input("Enter a number of file you want to load texts from: "))
        return user_input
