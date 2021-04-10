from menu.mainmenu import Main_Menu
from menu.create_recipe import Create_Recipe
from menu.list_recipe import List_Recipe
from menu.delete_recipe import *
from menu.constant import*
from menu.logic_menu.list_menu import List_Menu
from menu.logic_menu.create_menu import Create_Menu
from db.dbservice import DBService
from menu.base_menu import *
from utils import get_input_function
from models.recepte import Recipe
from models.products import Products
from menu.logic_menu.product_check import *
from menu.logic_menu.delete_menu import Delete_Menu
from menu.logic_menu.add_menu import Add_Menu
from menu.add_ingredient import Add_Ingredients

def get_user_input(options):
    available_inputs = [
        option[0]
        for option in options
    ]

    while True:
        user_option = input('введите id: ')
        print()
        if user_option in available_inputs:
            break
        else:
            print(
                'не верная опция'
            )
    return user_option


def main():
    db = DBService()
    main_menu = Main_Menu()
    list_menu = List_Menu(db)
    list_recipe = List_Recipe()
    create_recipe = Create_Recipe()
    create = Create_Menu(db)
    delete_recipe = Delete_Recipe()
    delete = Delete_Menu(db)
    add_ingredients = Add_Ingredients()
    add_ing = Add_Menu(db)


    main_menu.show()
    user_input = get_user_input(main_menu_options)

    if user_input == RECIPE_LIST:
        list_menu.select_recipe()
        list_recipe.show()
        user_input = get_user_input(list_menu_options)
        if user_input == BACK:
            main()

    if user_input == CREATE_RECIPE:
        sel_id = create.select_products_id()
        productsid = create.create_recipe(sel_id)
        create_recipe.show()

        user_input = get_user_input(create_menu_options)
        if user_input == BACK:
            main()
    if user_input == DELETE_RECIPE:
        delete.select_recipe()
        delete.delete_recipe()
        delete_recipe.show()
        user_input = get_user_input(delete_menu_option)
        if user_input == BACK:
            main()

    if user_input == ADD_ING:
        add_ing.create_ing()
        add_ingredients.show()
        user_input = get_user_input(add_menu_option)
        if user_input == BACK:
            main()
    
    if user_input == EXIT:
        print('Отключение от БД ...')
        print('до свидания! ')
        exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        db = DBService()
        db.close()