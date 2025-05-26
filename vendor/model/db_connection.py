import mysql.connector
from mysql.connector import Error


class MySQLConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='docverse',
                user='root',
                password='root'
            )
            if not self.connection.is_connected():
                raise ValueError("Não foi possível efetuar a conexão")
        except Error as e:
            print(f"Erro: {e}")

    def get_cursor(self):
        if self.connection.is_connected():
            return self.connection.cursor()

    def commit(self):
        if self.connection.is_connected():
            self.connection.commit()

    def rollback(self):
        # Método para desfazer a transação
        if self.connection.is_connected():
            self.connection.rollback()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
