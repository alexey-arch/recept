from db.dbservice import DBService
from models.recepte import Recipe

class List_Menu:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db

    def select_recipe(self):
        try:
            query = "SELECT * FROM recipe;"
            self.__db.execute(query)

            for i in self.__db.cursor.fetchall():
                print(f'{i["recipe"]}\n -{i["products"]}' )
                print(f"{'-'*30}\n")
                
        except Exception as ex:
            print(ex)
            