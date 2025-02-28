from sub_menu import SubMenu


class DeleteFileMenu(SubMenu):
    def get_input(self) -> int:
        user_input = int(input("Enter a number of file you want to delete: "))
        return user_input
