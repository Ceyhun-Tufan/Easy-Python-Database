import sqlite3
from sqlite3 import Error

class DataBase:
    def __init__(self,name) -> None:
        self.name = name
        self.connection = sqlite3.connect("{}.db".format(self.name))
        self.cursor = self.connection.cursor()       
        self.output = True
        self.error_outputs = True
    def create_table(self, table_name: str, columns: dict) -> None:
        """
        Create a table in the database.

        Parameters:
        - table_name (str): Name of the table.
        - columns (dict): Dictionary where keys are column names and values are column types.

        Example usage:
        db.create_table("users", {"id": "INTEGER PRIMARY KEY", "username": "TEXT", "email": "TEXT"})
        """
        try:
            column_str = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str})"
            
            self.cursor.execute(query)
            self.connection.commit()
            if self.output:
                print(f"Table '{table_name}' created successfully.")
        except Error as e:
            if self.output or self.error_outputs:
                print("An error occurred:", e)

    def delete_table(self, table_name: str) -> None:
        """
        Delete a table from the database.

        Parameters:
        - table_name (str): Name of the table to be deleted.

        Example usage:
        db.delete_table("users")
        """
        try:
            query = f"DROP TABLE IF EXISTS {table_name}"
            self.cursor.execute(query)
            self.connection.commit()
            if self.output:
                print(f"Table '{table_name}' deleted successfully.")
        except Error as e:
            if self.output or self.error_outputs:
                print("An error occurred:", e)


    def insert_one(self, table_name: str, values: list) -> None:
        """
        Insert a single record into the specified table.

        Parameters:
        - table_name (str): Name of the table.
        - values (list): List of values to be inserted into the table.

        Example usage:
        db.insert_one("users", ["John Doe", "john.doe@example.com"])
        """
        try:
            placeholders = ', '.join(['?' for _ in values])
            query = f"INSERT OR IGNORE INTO {table_name} VALUES ({placeholders})"
            
            self.cursor.execute(query, values)
            self.connection.commit()
            if self.output:
                print(f"Record inserted into '{table_name}' successfully.")
        except Error as e:
            if self.output or self.error_outputs:
                print("An error occurred:", e)

    # To find smth specific with the name of the collumn and expected value
    def search_one(self, table_name: str, column_name: str, column_value: str) -> list:
        """
        Search for a record in the specified table based on the given column and value.

        Parameters:
        - table_name (str): Name of the table.
        - column_name (str): Name of the column to search.
        - column_value (str): Value to search for in the specified column.

        Returns:
        - list: A list containing the values of the first matching record.

        Example usage:
        result = db.search_one("users", "username", "John Doe")
        print(result)
        """
        try:
            query = f"SELECT * FROM {table_name} WHERE {column_name} = ?"
            self.cursor.execute(query, (column_value,))
            
            row = self.cursor.fetchone()
            if row:
                return list(row)
            else:
                if self.output or self.error_outputs:
                    print(f"No record found in '{table_name}' with {column_name} = {column_value}.")
                return []
        except Error as e:
            if self.output or self.error_outputs:
                print("An error occurred:", e)
    
    def remove_row(self, table_name: str, column_name: str, column_value: str) -> None:
        """
        Remove a row from the specified table based on the given column and value.

        Parameters:
        - table_name (str): Name of the table.
        - column_name (str): Name of the column to check for deletion.
        - column_value (str): Value to use when checking for deletion.

        Example usage:
        db.remove_row("users", "username", "John Doe")
        """
        try:
            query = f"DELETE FROM {table_name} WHERE {column_name} = ?"
            self.cursor.execute(query, (column_value,))
            self.connection.commit()
            if self.output:
                print(f"Row removed from '{table_name}' where {column_name} = {column_value}.")
        except Error as e:
            if self.output or self.error_outputs:
                print("An error occurred:", e)

    def update_one(self, table_name: str, id_column: str, id_value: str, updated_column: str, updated_value) -> None:
        """
        Update a specific record in the specified table based on the given ID.

        Parameters:
        - table_name (str): Name of the table.
        - id_column (str): Name of the ID column.
        - id_value (str): Value of the ID to identify the record to update.
        - updated_column (str): Name of the column to update.
        - updated_value: New value for the updated column.

        Example usage:
        db.update_one("users", "id", "1", "username", "NewUsername")
        """
        try:
            query = f"UPDATE {table_name} SET {updated_column} = ? WHERE {id_column} = ?"
            self.cursor.execute(query, (updated_value, id_value))
            self.connection.commit()
            if self.output or self.error_outputs:
                print(f"Record in '{table_name}' updated where {id_column} = {id_value}.")
        except Error as e:
            if self.output or self.error_outputs:
                print("An error occurred:", e)
