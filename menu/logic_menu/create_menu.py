from db.dbservice import DBService
from models.recepte import Recipe
from menu.logic_menu.product_check import *
import json
from menu.logic_menu.product_check import Check

class Create_Menu:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db

    def select_products_id(self):
        try:
            query = "SELECT * FROM products;"
            self.__db.execute(query)
            for i in self.__db.cursor.fetchall():
                return i['id']
            
        except Exception as ex:
            print(ex)

    def create_recipe(self, products_id):
        try:
            db = DBService()
            products = Check(db)
            dish = (input('Введите название блюдо: '))
            list_prod = []

            print('Enter new correct answers (# - stop): ')

            while True:
                prod = input('- ')

                if prod in ('#', ''):
                    break
                list_prod.append(prod.lower())
            product = products.select_products()

            res = [i for i in list_prod if i in product]
            print(res)

            if res == list_prod:
                query = f"INSERT INTO recipe (recipe, products_id, products) VALUES (\'{dish}\', \'{products_id}\', \'{json.dumps(list_prod)}\');"                    
                self.__db.execute(query)
                
            else:
                print('не верные ингредиенты!')

        except Exception as ex:
            print(ex)
    
 