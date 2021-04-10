from menu.base_menu import*
from menu.constant import*

class Delete_Recipe(BasseMenu):
    delete_menu_option = (
        Option('5', 'назад'),
    
    )

    def __init__(self):
        super().__init__("удаление", self.delete_menu_option)

    def show(self):
        print("_-"*5, self.title, "-_"*5)
        for option in self.options:
            print(f"[{option.index}] - {option.title}.")