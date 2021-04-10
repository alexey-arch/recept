from menu.base_menu import*
from menu.constant import*

class Main_Menu(BasseMenu):
    main_menu_option = (
        Option('1', 'Список рецептов'),
        Option('2', 'Создать рецепт'),
        Option('3', 'Удалить рецепт'),
        Option('4', 'Добавить ингредиент'),
        Option('0', 'Выход')
    )

    def __init__(self):
        super().__init__("Добро пожаловать!", self.main_menu_option)

    def show(self):
        print("_-"*5, self.title, "-_"*5)
        for option in self.options:
            print(f"[{option.index}] - {option.title}.")