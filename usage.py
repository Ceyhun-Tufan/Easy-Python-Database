from database import DataBase

db = DataBase("trybase")

db.output = False # if you dont want ANY type of output in the terminal
db.error_outputs = False # if you only want to have error outputs

db.create_table("users", {"id": "INTEGER PRIMARY KEY", "username": "TEXT", "github": "TEXT"})
db.insert_one("users",[111111,"Ceyhun Tufan","https://github.com/Ceyhun-Tufan/"])
print(db.search_one("users","id",111111))