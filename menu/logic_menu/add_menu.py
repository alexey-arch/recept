from db.dbservice import DBService
from models.recepte import Recipe
from menu.logic_menu.product_check import *
import json
from menu.logic_menu.product_check import Check

class Add_Menu:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db


    def create_ing(self):
        try:
            db = DBService()
            ingr = input('введите ингредиент: ')

            query = f"INSERT INTO products (products, quantity, weight) VALUES (\'{ingr}\', 1, 1);"                    
            self.__db.execute(query)
            

        except Exception as ex:
            print(ex)
    
 