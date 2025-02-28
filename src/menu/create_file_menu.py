from sub_menu import SubMenu


class CreateFileMenu(SubMenu):
    def get_input(self) -> str:
        user_input = input("Enter a name of file: ")
        return user_input
