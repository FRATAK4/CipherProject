from sub_menu import SubMenu


class EncryptDecryptMenu(SubMenu):
    def get_input(self) -> int:
        user_input = int(input("Enter a number of word you want to change status of: "))
        return user_input
