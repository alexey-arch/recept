from menu.constant import *


main_menu_options = (
    (RECIPE_LIST, 'список рецептов'),
    (CREATE_RECIPE, 'создать рецепт'),
    (DELETE_RECIPE, 'удалить рецепт'),
    (ADD_ING, 'Добавить ингредиент'),
    (EXIT, 'выход')
)
list_menu_options = (
    (BACK, 'назад')
)
create_menu_options = (
    (BACK, 'назад')
)
delete_menu_option= (
    (BACK, 'назад')
)
add_menu_option= (
    (BACK, 'назад')
)

class Option:
    def __init__(self, index, title):
        self.index = index
        self.title = title


class ActiveOption(Option):
    def __init__(self, index, title, action):
        super().__init__(index, option)
        self.action = action

    def perform_action(self):
        self.action


class BasseMenu:
    def __init__(self, title, options=None):
        self.title = title
        self.options = options
    
    def show(self):
        return NotImplementedError