from db.dbservice import DBService

class Check:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db

    def select_products(self):
        try:
            prod = []
            query = "SELECT * FROM products;"
            self.__db.execute(query)
            for i in self.__db.cursor.fetchall():
                prod.append(i['products'])
            # print(prod)
            return prod
            
        except Exception as ex:
            print(ex)