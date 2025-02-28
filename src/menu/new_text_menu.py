from sub_menu import SubMenu


class NewTextMenu(SubMenu):
    def get_input(self) -> str:
        user_input = input(
            "Enter a text (format: 'text' 'rot13/rot47' 'encrypt/decrypt'): "
        )
        return user_input
