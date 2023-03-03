import sqlite3
from sqlite3 import Error

class DataBase:
    def __init__(self,name) -> None:
        self.name = name
        self.connection = sqlite3.connect("{}.db".format(self.name))
        self.cursor = self.connection.cursor()        
    def info(self) -> None:
        print("""database = DataBase() ## DataBase class'ını atayın
        Daha sonra table oluşturmak için create_table() içerisine ilk olarak 
        table ismi, sonrasında elemanların isim ve türlerini yazın""")
        
    def create_table(self,name:str,val:str) -> None:
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS {}(""".format(name)+val+");")
            self.connection.commit()
        except Error as e:
            print("An Error happened: {}".format(e))
    
    def insert_one(self,table_name:str,vals:list) -> None:
        ourstring = "("
        for i in vals:
            if not i == vals[-1]:
                ourstring += "'"+ i+"'"+"," 
            else:
                ourstring += "'"+ i+"'"
        ourstring += ")"
        try:
            self.cursor.execute("""INSERT OR IGNORE INTO {} VALUES""".format(table_name) + ourstring)
            self.connection.commit()
        except Error as e:
            print(e)

    # To find smth specific with the name of the collumn and expected value
    def search_one(self,table_name:str,val:list) -> list:
        val[1] = "'"+val[1]+"'"
        self.cursor.execute("""SELECT * FROM {} WHERE {} = {} """.format(table_name,val[0],val[1]))
        rows = self.cursor.fetchall()
        list_to_return = []
        for row in rows:
            for i in row:
                list_to_return.append(i)
        return list_to_return
    
    def remove_row(self,table_name:str,chair:str,val:str) -> None:
        val = "'"+val+"'"
        self.cursor.execute("""DELETE FROM {} WHERE {} = {} """.format(table_name,chair,val))
        self.connection.commit()

    def update_one(self,id:str,changed_val):
        pass





base = DataBase("trybase")
#x = base.search_one("Sunucu1",["gerekenler1","ceyhun"])
#print(x)
base.connection.commit()
base.connection.close()

#base.cursor.execute("""DELETE FROM Sunucu1""")
#base.insert_one("Sunucu1",["ceyhun","18","a"])
#base.remove_row("Sunucu1","gerekenler1","ceyhun")
#base.create_table("isim","""gerekenler1 text""")
